# Project ROLL — Technical Design Reference

This document owns **system architecture and integration considerations**, not detailed requirements, safety assessments, candidate evaluations, prototype build histories, or test results. See the [project purpose](README.md), [requirements](docs/requirements.md), [safety assessment](docs/safety.md), and [decision register](docs/decisions.md) for those records. The design remains experimental; no specific board, sensor, LED, enclosure, or battery has been selected or validated on `main`.

## Functional architecture

```text
Roll retrieval
      ↓
Sensor / sensing interface
      ↓
Microcontroller (Arduino-class or similar)
      ↓
LED output / driver
      ↓
Visible indication
```

A compact battery powers the electronics. Signal timing and reset behavior require further definition in [requirements](docs/requirements.md). The commitment to a microcontroller-based approach is recorded in [DEC001](docs/decisions.md#dec001--microcontroller-based-control).

## Electrical and firmware integration

- Choose a controller board and interfaces that can read the selected sensor configuration and drive the LED output safely.
- Check sensor logic levels, supply voltages, LED current, power protection, and battery capacity against actual component data.
- Provide LED current limiting and any suitable driver or electrical protection required by the selected parts.
- Begin with straightforward on/off behavior; only add timing, flashing, latching, or filtering when a testable need is identified.
- Keep firmware readable and configurable for sensing thresholds, filtering, indication duration/reset, and low-power operation.
- Document the actual controller, BOM, wiring, pin assignments, firmware revision, and configuration in the relevant [prototype revision](prototypes/README.md).

## Mechanical integration

- Use the [physical reference, body envelope, attachment requirement, and mass target](docs/requirements.md#dimensional-and-mass-targets) when planning the enclosure; assess feasibility before finalizing geometry.
- Reserve space for sensing modules, controller, battery, LEDs, wiring, and secure internal mounting.
- Explore simple modifiable enclosure techniques, including 3D printing if useful.
- Account for how mounting, housing materials, sealing, and LED windows affect sensing and visibility.
- Repeat functional tests after enclosing the electronics; integration can change sensor response.
- Keep build-specific drawings, dimensions, and assembly instructions with the [prototype revision](prototypes/README.md). Safety hazards and prerequisites belong in [docs/safety.md](docs/safety.md).

## Open integration questions

- Which electrical interfaces and available pins are needed by the selected sensor modules?
- What controller form factor and internal packing scheme can meet the [specified body envelope](docs/requirements.md#dimensional-and-mass-targets)?
- How should the circuit implement the indication and reset behavior defined in requirements?
- What mounting geometry preserves sensor performance and LED visibility?
- What practical power and maintenance interfaces are needed for the final enclosure?

Use [technology evaluations](docs/evaluations/README.md) for competing sensor approaches; [test records](tests/README.md) for evidence; [decisions](docs/decisions.md) for selected solutions and rationale; and the [roadmap](roadmap.md) for the work plan.
