# Project ROLL — Requirements and Acceptance Targets

This is the authoritative location for **what the prototype needs to achieve** and how success is judged. The [README](../README.md) defines overall purpose; [design.md](../design.md) handles implementation; [tests](../tests/README.md) contain methods and evidence. These targets are **not validated**. Numeric thresholds and final acceptance conditions remain **TBD**.

## Functional and practical requirements

| ID | Requirement | Acceptance target / open question | Verification area |
| --- | --- | --- | --- |
| REQ001 | Detect intentional mouth retrieval of the Roll. | Detection success criterion and response time: **TBD**. | Controlled detection tests |
| REQ002 | Limit unintended activations during ordinary movement, impact, contact, and wet conditions. | Allowable false-activation rate and conditions: **TBD**. | False-activation tests |
| REQ003 | Provide an LED indication visible to the handler. | Required lighting conditions, brightness, activation duration, and reset behavior: **TBD**. | Visibility and timing tests |
| REQ004 | Run on a compact battery. | Battery form factor, standby/active current, and minimum runtime: **TBD**. | Current and runtime tests |
| REQ005 | Fit electronics into a practical cylinder based on the existing Roll. | Length, diameter, mass, attachment geometry and allowable changes: **TBD**, pending measurement. | Dimensional/build checks |
| REQ006 | Remain functional under relevant handling and environmental exposure. | Impact, vibration, rain/saliva exposure conditions and limits: **TBD**. | Handling/environmental tests |
| REQ007 | Supplement, rather than interfere with, the trained retrieval behavior. | Observation criteria for supervised evaluation: **TBD**; safety gate applies. | Supervised behavioral evaluation, only if cleared |
| REQ008 | Support economical, modifiable DIY experimentation. | Parts availability, budget ceiling, serviceability targets: **TBD**. | Build review |
| REQ009 | Meet the prerequisites for any supervised dog exposure. | Follow the mandatory assessment and gate in [safety.md](safety.md). | Recorded safety inspection |

## Inputs needed to define targets

- Measurements of the current Roll and its neck attachment, including relevant handling loads.
- Expected retrieval, routine activity, impact, and moisture scenarios; these define realistic trial conditions.
- Handler viewing distance/lighting and desired start, duration, and reset of the indication.
- Runtime goal, power and weight/space budget.
- Test sample sizes and numeric thresholds for misses, false activations, response time, and any environmental tests.
- Criteria for detecting interference with trained behavior, to be applied only after safety clearance.

## Managing changes

Give every requirement a stable ID. Mark proposed thresholds as such until adopted in `main`; do not assign values from estimates alone. Link supporting evidence from [test runs](../tests/README.md) and record decisions with rationale in [decisions.md](decisions.md). Update this file when targets change, rather than restating numerical requirements in the design, roadmap, or prototype notes.
