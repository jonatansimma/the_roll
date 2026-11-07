# Technology Evaluations

This directory is the authoritative home for **investigating technologies before choosing how to build them**. An evaluation may start with datasheet research and continue with reproducible bench experiments. It is not a prototype build record or a test result.

**Evaluation asks:** Could the technology meet the need, what are its trade-offs, and what evidence do we have?

**Prototype work asks:** How was a particular circuit or arrangement constructed? See [prototypes](../../prototypes/README.md).

**Testing asks:** How did it behave under defined conditions? See [tests](../../tests/README.md).

## Initial retrieval-sensing candidates

These are **unselected approaches**, migrated from the earlier design notes. Their advantages are hypotheses, not verified findings.

| Candidate | Potential advantage | Key evaluation question |
| --- | --- | --- |
| Pressure-sensitive or mechanical switch | Direct response to a grip or applied load | Can it distinguish mouth grip from incidental contact while remaining protected? |
| Capacitive sensing | May not require an exposed moving mechanism | Is it reliable around saliva, rain, and enclosure materials? |
| Accelerometer | Can operate inside a closed enclosure | Can deliberate retrieval be distinguished from ordinary motion? |
| Sensor combination | Could reduce ambiguous detections | Does the benefit justify additional circuitry, complexity, and power use? |

**Selection principle:** Decide from comparable, repeatable evidence; motion alone does not prove retrieval. No candidate is currently selected or validated.

## Creating an evaluation

Use [the technology-evaluation template](../../templates/technology_evaluation.md). Assign a permanent `EV###` identifier (for example, `EV001`) and a descriptive filename: `EV001-short-name.md`. Do not create an entry solely to reserve a number.

Each evaluation should cover:

1. **Objective and problem:** What detection or engineering question could this method address?
2. **Operating principle:** What is measured and how could it indicate retrieval?
3. **Candidate components and references:** Datasheets, ratings, availability, and source links.
4. **Advantages and limitations:** Expected benefits and likely failure modes; identify hypotheses.
5. **Integration considerations:** Power consumption, cost, wiring, controller interfaces, size, enclosure and environmental interactions.
6. **Evaluation experiments:** What would discriminate between options? Link reusable [test procedures](../../tests/README.md).
7. **Findings:** Separate measured observations (linked to test runs), calculations/estimates, and unresolved unknowns.
8. **Conclusion and status:** Promising / unsuitable / needs further evidence; explain why.
9. **References and next actions:** Evidence links, follow-up experiments, and related decision entries.

Use SI units. Compare technologies using similar test conditions where practical, and do not transplant numerical results into this README or [design.md](../../design.md): link to the run that measured them. Record final selections and rationale in [decisions](../decisions.md).
