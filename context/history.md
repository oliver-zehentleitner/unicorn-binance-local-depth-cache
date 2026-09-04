# History

## LUCIT-Systems-and-Development origin

> Superseded — repo now lives under `oliver-zehentleitner`, MIT-licensed.

**Type:** decision
**Status:** superseded
**Evidence:** confirmed
**Source:** git history; old LUCIT-org issue URLs in early commits, e.g. `1282d45`, `005b68f`

Same origin and cleanup pattern as the rest of the suite: de-branded from `LUCIT-Systems-and-Development`, moved to `oliver-zehentleitner`, conda distribution switched to conda-forge with the in-repo `build_conda.yml` workflow removed (commit `eb0ca0f`, 2026-04-18: "Switch conda references to conda-forge, clean meta.yaml, sync deps").

**Reason:** LUCIT is no longer part of how this project is licensed, distributed, or supported.

## Cluster-client method rename (2.14.0)

**Type:** decision
**Status:** active
**Evidence:** confirmed
**Source:** commit `4b29780`

`ubdcc_*_credentials` methods on the cluster client had the `ubdcc_` prefix dropped, paired with matching endpoint renames on the UBDCC side (requires `ubdcc >= 0.7.0`).

**Reason:** explicit consistency cleanup — "for consistency with rest of API" (commit message). This is a breaking change for anyone calling the old `ubdcc_*_credentials` names directly against an older UBDCC.

**Revisit when:** touching the cluster client again — confirm the paired UBDCC version floor (`ubdcc >= 0.7.0`) is still accurate if UBDCC's endpoint names change again.
