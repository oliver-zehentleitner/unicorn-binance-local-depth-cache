# TASKS.md — UNICORN Binance Local Depth Cache

Open development tasks, ideas, and decisions.

---

## In Progress

*(none)*

---

## Backlog

*(none)*

---

## Done

### [x] Audit and fix all silent except/pass blocks
- Audited codebase — no silent except/pass blocks found
- Suite-wide initiative

### [x] Fix stale copyright/author in setup.py
- Updated `author` to "Oliver Zehentleitner", removed LUCIT email

### [x] Add mocked unit tests for Cluster class
- Added `TestCluster` in `unittest_binance_local_depth_cache.py`
- All HTTP calls mocked via `unittest.mock.patch` — no real UBDCC required
