# Project ROLL — Engineering Decision Register

Record engineering choices **and the reason for each choice**, with references to evaluations, exact prototype builds, and test evidence. Keep approved decisions, proposed changes, and untested hypotheses distinct. This register owns the decision rationale; source documents retain detailed implementation and results.

**Canonical-status reminder:** entries added on `agent_main` are proposed repository changes until a human incorporates them into `main`. A decision agreed in conversation alone is not yet established on `main`.

## DEC001 — Microcontroller-based control

- **Status:** User-agreed proposal, pending incorporation into `main`.
- **Date recorded:** 2026-11-07.
- **Context:** The Roll needs configurable sensing and LED control in a DIY build.
- **Choice:** Use a microcontroller-based design (Arduino-family boards or comparable controllers). The specific board is not selected.
- **Reasoning:** The approach is familiar, configurable and suited to iterative sensing experiments.
- **Consequence:** Design and prototypes should document board/pin choices and firmware. A different main controller defines a different prototype under the [prototype identification policy](../prototypes/README.md).
- **Supporting evidence:** User design direction; no component-level evaluation or validation yet.

## DEC002 — Prototype identification and revision policy

- **Status:** User-agreed proposal, pending incorporation into `main`.
- **Date recorded:** 2026-11-07.
- **Decision and operational rules:** [Prototype identification and revision policy](../prototypes/README.md#prototype-identity-and-revisions) (authoritative; do not duplicate here).
- **Reasoning:** Preserve the history of tested hardware configurations while avoiding revision inflation from ordinary firmware iteration.
- **Supporting evidence:** Development workflow preference; no prototype builds or test runs yet.

## Future decisions

For each subsequent decision, record: **ID · status · date · context · options considered · selection · evidence links · rationale · consequences · superseded-by (if applicable)**. Do not treat pending options as selections or mark validation without corresponding [test evidence](../tests/README.md).
