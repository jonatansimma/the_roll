# Project ROLL — Safety Assessment and Dog-Exposure Gate

This is the single authoritative location for **hazards, proposed mitigations, and the prerequisites for any supervised dog testing**. It is not evidence that a prototype is safe. The current entries are **unverified considerations**, not completed inspections. Actual inspection results belong in [test runs](../tests/README.md); build-specific controls belong in the applicable [prototype revision](../prototypes/README.md).

## Hazard review (open until evaluated)

| Hazard | What must be investigated | Possible mitigation to assess |
| --- | --- | --- |
| Battery access or failure | Bite damage, battery retention, short circuit, leaks, heat | Protected, securely retained power source; appropriate circuit protection |
| Loose electronics or fragments | Parts, fasteners, wiring or lenses escaping after impact or bite | Captive fastening, strong internal mounts, no accessible small components |
| Sharp edges and damaged enclosure | Cutting, splintering, or mouth injury | Smooth geometry and inspection after damage/handling |
| Temperature and electrical faults | Overheating during operation, charging (if applicable), or faults | Correct ratings, current limiting, insulation, fault and temperature checks |
| Moisture / saliva / rain | Ingress, electrical malfunction, corrosion and sensing changes | Enclosure sealing strategy; controlled exposure and post-test inspections |
| Mechanical loads and impacts | Cracking, loosened parts, or loss of enclosure integrity | Practical impact, retention and handling inspections |
| Neck attachment | Snagging, entanglement, unintended loading or release failure | Attachment assessment based on the existing Roll and handling conditions |
| Altered dog behavior | Interference with trained retrieval, comfort, or handling | Only a supervised assessment after physical/electrical clearance |

These mitigations are suggestions to investigate, **not approved or tested solutions**. Selected controls and remaining risks must be linked to the actual configuration.

## Required progression

1. **Off-dog work first.** Investigate electronics and simulated retrieval on the workbench. Never expose the dog to breadboard assemblies or loose, accessible electronics.
2. **Integrated build inspection.** Inspect the assembled, enclosed unit and attachment for retention, bite/impact exposure, sharp edges, moisture vulnerability, wiring, battery containment, and heat/electrical faults.
3. **Record the assessment.** Use a [test procedure and test run](../tests/README.md), identify the exact prototype revision and Git commit, and record results, outstanding hazards, and any conditions/limitations.
4. **Go/no-go decision.** If a significant hazard is unresolved, **do not test on the dog**. Rework and repeat the relevant inspection. Record the responsible human's decision and supporting evidence.
5. **Supervised evaluation only after clearance.** Limit animal evaluation to an appropriately supervised setting; stop and reassess if unexpected behavior, damage, or discomfort occurs.

A passed bench functional test is not a substitute for physical and electrical safety clearance. No prototype is currently documented here as cleared for dog exposure.
