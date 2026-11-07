# Tests — Procedures, Runs, and Observations

This directory owns **repeatable test methods and recorded evidence**, including unexpected observations and raw data. A test procedure says **how to test**; a test run records **what happened**. Keep them separate so different prototype revisions can be compared under the same method.

## Directory roles and identifiers

- `procedures/TP###-short-name.md` — reusable procedure. A procedure can be used for several prototype IDs and revisions. If the method changes materially, record its method revision and use it in subsequent runs; do not silently rewrite the meaning of old results.
- `runs/YYYY-MM-DD-TR###.md` — unique, dated execution record. Record each performed run separately, including failures and inconclusive results; never turn a planned run into invented evidence.
- Use the [test-run template](../templates/test_run.md) for actual runs. For procedures, follow the structure below.
- Optional raw data (`.csv`), photographs, or media references should be stored or linked next to the relevant run with unambiguous filenames. Avoid unnecessary large binary files in Git.

## Test procedure: what to document

| Field | Purpose |
| --- | --- |
| Procedure ID and revision | Stable reusable method reference |
| Objective and requirement IDs | What behavior or constraint is being evaluated |
| Required equipment | Instruments, fixtures, tools, environmental setup |
| Setup and conditions | Sensor/fixture placement, supply, handling conditions |
| Steps | Reproducible sequence, including number of trials |
| Measurements and recording | What data, units, event definitions, and sample size to capture |
| Acceptance criteria | Link to [requirements](../docs/requirements.md); do not invent thresholds |
| Precautions and limitations | Relevant [safety](../docs/safety.md) constraints and sources of error |

## Test run: what to document

| Field | Purpose |
| --- | --- |
| Run ID, date and operator | Identify when/by whom the test was performed |
| Procedure ID and method revision | Exact method followed, deviations explicitly noted |
| Prototype ID and hardware revision | For example `P001-v01`; identify actual built configuration |
| Git commit and firmware settings | **Full SHA**, toolchain if relevant, sensor thresholds/config |
| Setup and conditions | Instruments, power source, environment, fixture, lighting |
| Trials and raw measurements | Counts and values with units; links to raw files |
| Expected / acceptance target | Link requirement IDs; mark `TBD` if not yet defined |
| Actual result | Measured outcome; pass/fail/inconclusive only when justified |
| Field notes | Unexpected activations, failures, observations, anomalies, deviations |
| Follow-up | Hypothesis, proposed change, new test, linked decision or revision |

**Field notes belong in the relevant run**, not in a separate miscellaneous notes directory. Keep measurements separate from estimates and explanations. Record observed failures even if no acceptance criterion exists.

## Proposed test coverage

Document procedures as testing actually begins. Relevant areas, carried over from the original design notes, include:

| Area | Observations or measurements to plan |
| --- | --- |
| Retrieval detection | Hits, misses, delay, sensitivity, repeated trials |
| False activations | Responses to normal motion, contact, knocks, and moisture |
| LED behavior | Visibility, brightness, duration, reset, lighting conditions |
| Power | Standby/active current and measured battery runtime |
| Mechanical | Retention, enclosure integrity, vibration, impacts |
| Environment | Relevant wet handling, rain/saliva-like exposure, post-test operation |
| Safety | Inspection results and evidence for the [dog-exposure gate](../docs/safety.md) |

Acceptance thresholds belong only in [requirements](../docs/requirements.md) and are presently **TBD**. A safety or dog-behavior test may occur only within the prerequisites in [docs/safety.md](../docs/safety.md).

## Data integrity and iteration

- Preserve completed run records and raw evidence; append a clearly marked correction instead of rewriting observed history.
- Link tests to the exact [prototype configuration](../prototypes/README.md) and code commit, so firmware-only edits do not become ambiguous.
- Compare runs under equivalent methods and conditions; note differences that could affect interpretation.
- Link findings to [evaluations](../docs/evaluations/README.md), [decisions](../docs/decisions.md), or the next prototype revision without copying full tables of results.
- Only count a roadmap milestone as completed with traceable implementation or test evidence.
