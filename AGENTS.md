# AGENTS.md — UNICORN Binance Local Depth Cache

> **End-user cheatsheet for AI-assisted consumption:** [`llms.txt`](llms.txt) — use that one if you're writing code *against* this library.
> **This file** is for AI agents working *on* this repo itself.

## Why things are the way they are

See [`context/index.md`](context/index.md) before making non-trivial changes — it points to the reasoning behind design decisions, rejected alternatives, and constraints that aren't visible in the code. If `AGENTS.local.md` exists in this repo, that's personal/local notes, not relevant to anyone else.

## Planning & Backlog

Open development tasks and decisions are tracked in **[TASKS.md](TASKS.md)**.

---

## Project Overview

Python SDK (MIT License) for building and managing multiple local Binance order book depth caches. Subscribes to Binance WebSocket diff streams, initializes via REST snapshots, and maintains a synchronized in-process order book (asks/bids) per market.

**Current Version:** 2.14.0
**Python Compatibility:** 3.9 – 3.14  
**Author:** Oliver Zehentleitner  
**PyPI:** `unicorn-binance-local-depth-cache`  
**Abbreviation used in Suite:** UBLDC

---

## Directory Structure

```
unicorn_binance_local_depth_cache/     # Main package
    manager.py                         # Core class BinanceLocalDepthCacheManager (~1312 lines)
    cluster.py                         # Cluster client for UBDCC (Kubernetes mode)
    cluster_endpoints.py               # REST endpoint definitions for UBDCC
    exceptions.py                      # Custom exceptions (4 classes)
    __init__.py                        # Package exports

unittest_binance_local_depth_cache.py  # Unit tests (main test file, run in CI)
dev/                                   # Local dev/integration tests — NOT run in CI
examples/                              # Usage examples (8 directories)
docs/                                  # Pre-built HTML documentation (Sphinx)
```

---

## Supported Exchanges

Configured via the `exchange` constructor parameter:

| Exchange String | Notes |
|---|---|
| `binance.com` | Spot (default) |
| `binance.com-testnet` | Spot testnet |
| `binance.com-futures` | USD-M Futures |
| `binance.com-futures-testnet` | Futures testnet |
| `binance.us` | US exchange |

---

## Dependencies

Managed in `requirements.txt`, `setup.py`, and `pyproject.toml` — **all three must be kept in sync manually**:

- `unicorn-binance-websocket-api>=2.13.0` — WebSocket stream management (UBWA)
- `unicorn-binance-rest-api>=2.10.0` — REST snapshot fetching (UBRA)
- `orjson` — fast JSON serialization
- `aiohttp` — Async HTTP for cluster communication
- `requests>=2.32.3` — Sync HTTP
- `Cython>=3.0.10` — C extension compilation (release builds only)

---

## Running Tests

```bash
# Unit tests with coverage (this is what CI runs)
coverage run --source unicorn_binance_local_depth_cache unittest_binance_local_depth_cache.py

# Unit tests without coverage
python -m unittest unittest_binance_local_depth_cache.py
```

Tests connect to **binance.us** (live, unauthenticated public data). Tests in `dev/` are local integration tests — **not run in CI**.

---

## Build & Packaging

Development and testing use **plain Python** — no Cython compilation needed during development.

Cython compilation only for **release builds**:

```bash
python setup.py bdist_wheel
```

**Version bump** — done manually before each release. Update in all three locations:
1. `setup.py` (line 65)
2. `pyproject.toml`
3. `unicorn_binance_local_depth_cache/manager.py` (`__version__` near top)

Version management helper: `dev/set_version.py`

**CI/CD:** GitHub Actions in `.github/workflows/`
- `unit-tests.yml` — Python 3.9–3.14, Codecov upload
- `build_wheels.yml` — Manual trigger, Linux/macOS/Windows wheels + PyPI release
- `codeql.yml` — Security scanning

No in-repo conda build — conda-forge's own feedstock is the only conda source (see [`context/history.md`](context/history.md)).

---

## Code Conventions

- **File header:** Full MIT license block with author/copyright (2019-2026)
- **Encoding:** UTF-8, UNIX line endings
- **Logging:** `logging.getLogger("unicorn_binance_local_depth_cache")`
- **Type hints:** Present throughout; `typing` stdlib
- **Cython:** Core modules compile to C extensions — no `#cython:` directives needed
- **Versioning:** Keep in sync across `setup.py`, `pyproject.toml`, `manager.py` manually

---

## Key Classes

| Class | File | Purpose |
|---|---|---|
| `BinanceLocalDepthCacheManager` | `manager.py` | Main class, inherits `threading.Thread` |
| `Cluster` | `cluster.py` | HTTP client for UBDCC remote cluster |
| `DepthCacheOutOfSync` | `exceptions.py` | Cache lost sync with exchange |
| `DepthCacheNotFound` | `exceptions.py` | Requested cache doesn't exist |
| `DepthCacheAlreadyStopped` | `exceptions.py` | Operation on stopped cache |
| `DepthCacheClusterNotReachableError` | `exceptions.py` | UBDCC connection failure |

---

## Architecture

**High-level flow:**
1. `create_depthcache(markets)` — subscribes via UBWA WebSocket + fetches REST snapshot via UBRA
2. REST snapshot applied; pending WebSocket diff updates buffered during init
3. Once synced, updates applied continuously from WebSocket diff stream — see [`context/sync.md`](context/sync.md) for why the init buffer works the way it does (options-endpoint staleness, margin routing)
4. `get_asks(market)` / `get_bids(market)` — return sorted order book slices
5. `stop_depthcache(markets)` / `stop_manager()` — cleanup

**Threading model:**
- `_manage_depthcaches()` — background thread for refresh/stop requests
- UBWA thread — delivers WebSocket stream updates
- Per-market `threading.Lock` — protects asks/bids dicts during concurrent access

**Stream multiplexing:** One WebSocket stream handles multiple markets up to Binance's subscription limit.

**Cluster mode (UBDCC):** If `ubdcc_address` is set, requests are delegated to a remote Kubernetes cluster instead of managing local caches.

---

## Usage Patterns (Quick Reference)

```python
from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager, DepthCacheOutOfSync

# Basic
ubldc = BinanceLocalDepthCacheManager(exchange="binance.com")
ubldc.create_depthcache("BTCUSDT")

try:
    asks = ubldc.get_asks("BTCUSDT")
    bids = ubldc.get_bids("BTCUSDT")
except DepthCacheOutOfSync:
    pass  # cache is re-syncing

ubldc.stop_manager()

# Context manager (auto-cleanup)
with BinanceLocalDepthCacheManager(exchange="binance.com") as ubldc:
    ubldc.create_depthcache(["BTCUSDT", "ETHUSDT"])
    asks = ubldc.get_asks("BTCUSDT", limit_count=10)
    bids = ubldc.get_bids("BTCUSDT", threshold_volume=300_000)

# With shared UBRA instance (reduces REST API connections)
from unicorn_binance_rest_api import BinanceRestApiManager
ubra = BinanceRestApiManager(exchange="binance.com")
ubldc = BinanceLocalDepthCacheManager(exchange="binance.com", ubra_manager=ubra)
```

---

## Notes & Gotchas

- `get_asks()` returns asks sorted **ascending** (lowest price first); `get_bids()` **descending**
- `DepthCacheOutOfSync` is expected during re-initialization — callers must handle it
- `get_list_of_depth_caches()` is deprecated since 2.8.0 → use `get_list_of_depthcaches()`
- `stop_depthcache()` clears asks/bids but retains metadata (restart count, timestamps)
- `high_performance=True` disables REST rate limiting — use carefully
- `print_summary_to_png()` only works on Linux
- Stub files (`.pyi`) generated by `setup.py` during build for IDE autocomplete

<!-- keep-the-why:config -->
- context: `context/`
- init: complete
- context-schema: 0.8.0
- capture-confirmation: confirm-when-unsure
<!-- /keep-the-why:config -->
