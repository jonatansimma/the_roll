# Project ROLL — DIY Prototype Roadmap

This is a **proposed plan**, not a record of completed work. Milestones should be marked complete only when supported by linked build or [test evidence](tests/README.md). The overall objective is defined in [README.md](README.md); detailed acceptance targets belong in [requirements](docs/requirements.md).

## 1. Define use case and constraints

- [x] Record the owner's initial dimensions, mass and attachment description of the existing Roll in [requirements](docs/requirements.md#dimensional-and-mass-targets) (user-reported; not independently verified).\n- [ ] Confirm reference dimensions and attachment details as needed, and evaluate whether the proposed body and mass limits are feasible.
- [ ] Observe the existing trained retrieval behavior without putting an electronic prototype on the dog.
- [ ] Document exposure conditions and intended LED activation/reset behavior in [requirements](docs/requirements.md).
- [ ] Define measurable targets and proposed pass/fail conditions before validation.

**Deliverable:** completed initial requirements and known unknowns.

## 2. Evaluate retrieval detection

- [ ] Compare candidate sensing methods in [evaluations](docs/evaluations/README.md).
- [ ] Plan and conduct repeatable bench experiments with simulated retrieval and ordinary handling.
- [ ] Document observations and measurements as [test runs](tests/README.md).
- [ ] Record the evidence-based approach selection in [decisions](docs/decisions.md).

**Deliverable:** linked evaluation and test evidence supporting a proposed sensing choice.

## 3. Build basic electronics

- [ ] Select an appropriate microcontroller board, sensor modules, LED output, and power arrangement.
- [ ] Document the circuit, BOM, firmware, and build method in a [prototype revision](prototypes/README.md).
- [ ] Assemble an accessible bench prototype.
- [ ] Demonstrate basic sensor-to-LED operation away from the dog and record the result.

**Deliverable:** reproducible bench build with a linked test run.

## 4. Troubleshoot and refine

- [ ] Execute repeatable detection, false-activation, and power tests using documented procedures.
- [ ] Investigate failures and adjust hardware or code as needed.
- [ ] Preserve relevant configurations and results; apply the [prototype identity/revision rules](prototypes/README.md).
- [ ] Compare new runs against the defined acceptance criteria.

**Deliverable:** documented improvements and evidence for the current bench prototype.

## 5. Integrate

- [ ] Package the electronics in a modifiable cylinder within the [defined physical limits](docs/requirements.md#dimensional-and-mass-targets) and record the build artifacts.
- [ ] Resolve attachment, assembly, sealing, and maintainability questions.
- [ ] Re-run applicable procedures with the assembled enclosure.

**Deliverable:** integrated prototype revision with assembly records and associated runs.

## 6. Validate

- [ ] Perform bench, handling, environmental, performance, and power checks against [requirements](docs/requirements.md).
- [ ] Complete and record the [safety gate](docs/safety.md) before considering any supervised dog evaluation.
- [ ] If the gate is met, evaluate in carefully supervised training, recording behavioral interference and any unexpected events.
- [ ] Record limitations, findings, decisions, and necessary follow-up revisions.

**Deliverable:** traceable validation runs and remaining issues, not an unsupported claim of completion.

Use [test procedures and test runs](tests/README.md) for methods, record formats, and results; do not embed a competing test template in this roadmap.
