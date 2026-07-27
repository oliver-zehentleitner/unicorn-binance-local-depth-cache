# Sync / resync

## Options depth cache: endless resync from a stale REST snapshot

**Status:** active
**Evidence:** confirmed
**Source:** commit `f57089f`

Binance's `/eapi/v1/depth` REST endpoint (used for `binance.com-vanilla-options` snapshots) can serve a cached response whose `lastUpdateId` lags the live WebSocket diff stream by up to ~25–30 seconds. The standard Binance sync algorithm requires finding a diff event where `U <= lastUpdateId <= u`; with a snapshot that stale, that predicate could never match, and the old code discarded the init buffer on every resync attempt — producing an endless "out of sync" loop for options markets specifically.

**Fix:** keep the init buffer across resync attempts instead of discarding it, prune buffered events older than the snapshot (`u < lastUpdateId`), and cap the buffer at 10,000 entries. See the inline comment at `manager.py` (~line 729), which matches the commit message.

**Reason:** this is a REST-endpoint-specific staleness window on Binance's side (options snapshots, not spot/futures), not something that could be fixed by retrying faster — the buffer needs to survive long enough to still contain the events the stale snapshot needs to reconcile against.

## Init-race: buffer WS events instead of dropping them

**Status:** active
**Evidence:** confirmed
**Source:** commit `fc7afdd`

During the snapshot-fetch window (before `last_update_id` is known), WebSocket diff events arriving in that gap were previously dropped rather than buffered — risking a missed sync point, especially on fast-moving markets where several diffs can arrive before the REST snapshot response comes back.

**Reason:** Binance's documented sync algorithm requires: open the WS stream first, buffer events, fetch the snapshot, then replay buffered events from the correct point. Dropping events during that window violates the algorithm's own ordering guarantee — buffering is the algorithm, not an optimization on top of it.

## Margin/isolated-margin: falling through to the wrong path in four places

**Status:** active
**Evidence:** confirmed
**Source:** commit `106b73c`

Margin and isolated-margin exchanges were falling through to an `else` branch in four separate places: `_get_order_book_from_rest()`, live-update gap detection, post-sync replay gap detection, and `_process_init_event()` — none of which routed them into the actual sync logic.

**Fix:** route all margin variants through the same code path as `binance.com`, since margin uses the same spot REST snapshot endpoint and spot WS diff format.

**Reason:** this was a gap-in-coverage bug, not a design choice — margin markets need the same sync algorithm as spot, just weren't wired into all four branch points when margin support was added.
