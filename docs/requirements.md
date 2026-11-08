# Project ROLL — Requirements and Acceptance Targets

This is the authoritative location for **what the prototype needs to achieve** and how success is judged. The [README](../README.md) defines overall purpose; [design.md](../design.md) handles implementation; [tests](../tests/README.md) contain methods and evidence. These requirements are **not validated**. Some numeric thresholds have now been specified by the project owner, while other acceptance conditions remain **TBD**.

## Functional and practical requirements

| ID | Requirement | Acceptance target / open question | Verification area |
| --- | --- | --- | --- |
| REQ001 | Detect intentional mouth retrieval of the Roll. | Detection success criterion and response time: **TBD**. | Controlled detection tests |
| REQ002 | Limit unintended activations during ordinary movement, impact, contact, and wet conditions. | Allowable false-activation rate and conditions: **TBD**. | False-activation tests |
| REQ003 | Provide an LED indication visible to the handler. | Required lighting conditions, brightness, activation duration, and reset behavior: **TBD**. | Visibility and timing tests |
| REQ004 | Run on a compact battery for the required duration between recharging or battery replacement. | See [operating time requirements](#operating-time-requirements); battery form factor, operating profile and power consumption remain **TBD**. | Current and operating-duration tests |
| REQ005 | Fit the functional electronics into the specified external body envelope while preserving the attachment-loop function. | Follow the [dimensional and mass targets](#dimensional-and-mass-targets). The maximum mass is a **target with unverified feasibility**, not a tested result. | Dimensional, mass and attachment checks |
| REQ006 | Remain functional under relevant handling and environmental exposure. | Impact, vibration, rain/saliva exposure conditions and limits: **TBD**. | Handling/environmental tests |
| REQ007 | Supplement, rather than interfere with, the trained retrieval behavior. | Observation criteria for supervised evaluation: **TBD**; safety gate applies. | Supervised behavioral evaluation, only if cleared |
| REQ008 | Support economical, modifiable DIY experimentation. | Parts availability, budget ceiling, serviceability targets: **TBD**. | Build review |
| REQ009 | Meet the prerequisites for any supervised dog exposure. | Follow the mandatory assessment and gate in [safety.md](safety.md). | Recorded safety inspection |

## Dimensional and mass targets

These figures were **supplied by the project owner on 2026-11-08**. They describe the physical reference and intended design limits; they are not independent measurements or validated prototype outcomes.

### Existing non-electronic Roll — physical reference

- **Shape:** oval cylinder (not circular in cross-section).
- **Body length:** 120 mm.
- **Widest cross-sectional dimension:** 35 mm. The other oval axis has not been reported.
- **Mass:** 8 g.
- **Attachment:** textile loop at one end, protruding approximately 10 mm beyond the body; the attachment function must carry over to the electronic prototype.
- **Photographic reference:** [existing non-electronic Roll](images/original-roll-reference.webp). This image is for visual/attachment reference and is not a calibrated dimensional measurement.

### Working electronic prototype — stated design limits

- **Body shape:** round cylinder, replacing the oval cross-section of the original.
- **Nominal maximum external body dimensions:** 120 mm length and 35 mm diameter. Treat these as **hard design limits** for the default build, not merely preferred dimensions.
- **Exception policy:** Exceeding a stated body dimension requires a compelling design justification documented before adopting the change; any permitted dimensional change must stay within **±10%** of its stated nominal value. This means an exceptional increase cannot exceed **132 mm body length** or **38.5 mm outer diameter**. These exceptional limits are **not** automatic allowances or build tolerances.
- **Attachment:** provide a textile attachment loop at an end that retains the existing Roll's attachment function, with a nominal **10 mm projection beyond the cylinder body**. The 120 mm body-length figure excludes this external loop projection.
- **Prototype mass:** target **no more than 50 g total** (including enclosure, electronics, power source, and attachment). Whether this limit is physically achievable or appropriate for handling by the dog is **unverified**; investigate through component budgeting, assembly measurements, and [safety assessment](safety.md).

### Still to establish

- Independent measurement of the original Roll, including the oval's shorter axis, attachment dimensions, and retention.
- Dimensional feasibility once the electronics, battery, enclosure, and LED visibility strategy are selected.
- Actual prototype mass and safe/acceptable handling characteristics before any dog exposure.

## Operating time requirements

These values were **specified by the project owner on 2026-11-08** for the electronic prototype. The requirements have not yet been demonstrated in testing.

- **Mandatory minimum (hard limit):** The prototype **must operate for at least 1 hour** without recharging or replacing its battery. A design that cannot meet this threshold is unacceptable.
- **Preferred operating-time target (not a hard limit):** Aim for **at least 12 hours** of operation without recharging or replacing its battery. Feasibility is **not yet established**; failure to reach this preferred target does not by itself violate the mandatory 1-hour requirement.
- **Verification to define:** Specify the representative operating profile (including idle/sensing time, LED activation frequency and duration), battery starting condition, criteria for the end of usable operation, and test conditions before measuring whether a build satisfies the hard limit and approaches the target. Record actual results in [test runs](../tests/README.md); no runtime has been measured yet.

## Inputs needed to define targets

- Confirmation of the user-provided reference dimensions and the original Roll's attachment, including relevant handling loads.
- Expected retrieval, routine activity, impact, and moisture scenarios; these define realistic trial conditions.
- Handler viewing distance/lighting and desired start, duration, and reset of the indication.
- Representative duty cycle and power budget needed to assess [operating time requirements](#operating-time-requirements) and feasibility of the [physical/weight targets](#dimensional-and-mass-targets).
- Test sample sizes and numeric thresholds for misses, false activations, response time, and any environmental tests.
- Criteria for detecting interference with trained behavior, to be applied only after safety clearance.

## Managing changes

Give every requirement a stable ID. Mark proposed thresholds as such until adopted in `main`; do not assign values from estimates alone. Link supporting evidence from [test runs](../tests/README.md) and record decisions with rationale in [decisions.md](decisions.md). Update this file when targets change, rather than restating numerical requirements in the design, roadmap, or prototype notes.
