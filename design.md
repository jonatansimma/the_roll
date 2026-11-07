# Project ROLL — Prototype Design Notes

These notes expand the [baseline instructions](baseline_instructions.md) into a working design reference for **one experimental DIY prototype**. They describe requirements and options, **not a finalized design**. No component, sensor, dimension, or performance specification has been selected or validated here.

## Intended behavior

A scent-detection dog wears the Roll around its neck. When the dog finds a target scent, it retrieves the Roll in its mouth and returns to its handler. The electronics should recognize deliberate retrieval and illuminate LEDs, adding a visible indication without changing the dog's trained behavior.

Proposed functional flow:

```text
Dog retrieves Roll
        ↓
Retrieval sensor / detection circuit
        ↓
Simple logic or microcontroller (if needed)
        ↓
LEDs illuminate
        ↓
Reset / return to standby (behavior TBD)
```

A compact battery powers the system. Power protection and current limiting must be appropriate to the selected parts.

## Design constraints

| Area | Requirement or current position |
| --- | --- |
| Form | Practical cylinder, with dimensions derived from the existing Roll. |
| Detection | Recognize mouth retrieval; avoid unacceptable triggers from ordinary movement, impacts, contact, or moisture. |
| Visual signal | Clearly visible LEDs; color, count, brightness, timing, and reset TBD. |
| Power | Compact battery; standby/active current and runtime to be measured. |
| Build | Affordable, available parts; simple wiring, modification, and troubleshooting. |
| Environment | Evaluate saliva, rain, vibration, impacts, and enclosure integrity. |
| Dog safety | No accessible battery/electronics, loose small parts, sharp edges, overheating, or hazardous neck attachment. |
| Scope | DIY proof of concept; no commercial finish or manufacturing optimization. |

## Candidate detection methods

| Method | Potential advantage | Main question to test |
| --- | --- | --- |
| Pressure-sensitive or mechanical switch | Direct response to an applied grip/load | Can it distinguish a mouth grip from other contact while staying protected? |
| Capacitive sensing | Potentially no external moving mechanism | How reliably does it work around saliva, rain, and nearby materials? |
| Accelerometer | Entire sensor can sit inside a closed enclosure | Can ordinary motion be separated from deliberate retrieval? |
| Combined sensors | May reduce ambiguous triggers | Is any improvement worth the added complexity and power draw? |

**Decision rule:** select through simple repeatable bench tests. Motion alone should not be assumed to prove retrieval.

## Electronics and LED subsystem

- Choose the simplest controller or non-programmable logic that meets the detection and signaling requirements.
- Check sensor interface levels, supply voltage, LED current, and battery capacity using component datasheets.
- Include suitable LED current limiting and necessary electrical/battery protection.
- Begin with straightforward on/off signaling; test whether a timed, flashing, or latched signal is useful before adding it.
- If firmware is needed, keep it readable and adjustable for detection thresholds, filtering, LED duration/reset, and low-power operation.
- Produce a parts list, wiring diagram, relevant calculations, and a documented build before integration.

No specific board, LED, chemistry, or sensor is designated as the default.

## Mechanical integration

- Measure the existing Roll before choosing enclosure dimensions.
- Plan internal space for the sensor, battery, controller (if needed), LEDs, wiring, and secure mounts.
- Explore DIY materials and 3D printing for a simple, modifiable cylindrical enclosure.
- Consider how the housing affects sensing, light visibility, sealing, attachment, and access for modifications.
- Evaluate bite exposure, impacts, saliva/rain ingress, snagging, and whether any components could loosen or become accessible.
- Test electrical behavior again after enclosure assembly: packaging can change sensor performance.

## Verification plan

Use repeatable bench and handling tests before any supervised dog training.

| Test area | Measurements or observations | Acceptance threshold |
| --- | --- | --- |
| Detection | Successful activations, misses, response delay, false alarms, sensitivity | TBD |
| LEDs | Visibility, brightness, activation timing, reset behavior | TBD |
| Power | Standby/active current, estimated and measured runtime | TBD |
| Mechanical | Attachment security, impact tolerance, integrity, vibration effects | TBD |
| Environment | Effects of moisture, saliva-like exposure, and rain on operation | TBD |
| Safety | Battery retention, component security, fault/heat checks, bite and attachment hazards | Safety review required before dog exposure |

Record the prototype version, setup, number of trials, results, deviations, and changes. Use basic tools such as a multimeter where practical. Treat measured outcomes separately from estimates.

## Open decisions

1. Existing Roll dimensions, attachment method, and actual handling loads.
2. Chosen retrieval sensor and how to reject false triggers.
3. LED placement and required visibility in different lighting.
4. Activation duration and reset behavior.
5. Battery choice and target runtime.
6. Enclosure material, sealing strategy, and safe access for maintenance.
7. Quantitative test criteria and conditions for supervised dog evaluation.

Next actions are tracked in the [roadmap](roadmap.md). Changes to these notes should reflect measurements and tested choices rather than assumptions.
