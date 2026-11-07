# Project ROLL

Project ROLL explores a visible LED signal for a trained scent-detection dog's existing retrieval indication. The dog wears a cylinder (the **Roll**) around its neck and retrieves it into its mouth after finding a target scent. The intended LED signal should supplement, not disrupt, that trained behavior.

## Goal and scope

Build and evaluate **one working, battery-powered DIY prototype**, not a commercial product. Success means detecting deliberate retrieval, providing a clearly visible indication, avoiding unacceptable false signals, and fitting the electronics into a practical cylinder without unacceptable risk to the dog. Measurable acceptance criteria remain to be established in [requirements](docs/requirements.md).

## Development approach

**Build → test → troubleshoot → improve.** Start with affordable, simple off-dog experiments; integrate only after basic function is demonstrated. Read the [safety assessment and dog-exposure gate](docs/safety.md) before planning animal evaluation.

Four linked engineering records make the work traceable:

| Record | Question answered | Home |
| --- | --- | --- |
| Evaluations | Which technologies are plausible, and what evidence supports them? | [Technology evaluations](docs/evaluations/README.md) |
| Prototypes | What was built, and how did the hardware evolve? | [Prototypes](prototypes/README.md) |
| Tests | How was it tested, and what happened? | [Tests](tests/README.md) |
| Decisions | Why was an approach chosen or changed? | [Decision register](docs/decisions.md) |

Follow the evidence chain: **requirements → evaluation → prototype revision → test procedure → test run → decision → next revision**. Link records to each other; keep each substantive fact in its designated source file. Document enough to reproduce an experiment and understand its outcome, but no more than necessary.

## Repository navigation

- [Requirements and measurable targets](docs/requirements.md) — what the Roll must achieve; unresolved thresholds.
- [Design reference](design.md) — architecture, subsystem interfaces, and integration questions.
- [Roadmap](roadmap.md) — phases, milestones, and pending work, not evidence of completion.
- [Safety](docs/safety.md) — hazards, mitigations, and prerequisites for supervised dog testing.
- [Technology evaluations](docs/evaluations/README.md) — investigation process and current candidate approaches.
- [Prototypes](prototypes/README.md) — IDs, revision rules, reproducible builds, and firmware tracking.
- [Tests](tests/README.md) — reusable procedures, actual runs, measurements, and field notes.
- [Decisions](docs/decisions.md) — decision status, rationale, and supporting evidence.
- [Illustrative target structure](docs/target_structure.md) — examples only; not a statement of completed work.
- [Contributor/agent rules](AGENTS.md) — documentation ownership and the mandatory agent branch policy.

The repository's `main` branch is the source of canonical project state. Agent-authored changes on `agent_main` remain proposals until a human incorporates them into `main`.
