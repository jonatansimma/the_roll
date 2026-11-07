# Prototypes — Builds and Hardware Evolution

This directory owns **reproducible hardware builds and their evolution**. A prototype record describes exactly what was built; it does not replace a [technology evaluation](../docs/evaluations/README.md), a [test run](../tests/README.md), or a [decision](../docs/decisions.md). No actual hardware prototypes have yet been documented in this directory.

## Prototype identity and revisions

- **Prototype ID — `P001`, `P002`, ...:** A distinct design centered on a particular **main microcontroller/controller board**. Changing the main controller model or board (for example, **Arduino Pro Mini → Arduino Uno**) creates a **new prototype ID**, even if sensing and LEDs are otherwise similar.
- **Hardware revision — `v01`, `v02`, ...:** A meaningful hardware/configuration evolution **within the same main controller**, such as changed sensor stack, sensor module, LED module, relevant circuitry, or mechanical integration. Preserve earlier tested revisions.
- **Firmware-only edit:** **Does not automatically create a new prototype or hardware revision.** Track source and configuration changes with Git commits and record the exact commit/configuration used for each test. A later hardware revision is still warranted if hardware changes as described above.
- **Controller firmware changes:** A change in software behavior alone remains under the existing revision, even if substantial. A controller **hardware** change creates a new prototype ID.
- **Experimental status:** Keep `planned`, `built`, `bench tested`, `integrated`, and `retired` distinct. Do not label anything tested without a linked run.

Example (naming only, **not built**):

```text
prototypes/
└── P001-sensor-bench/
    ├── README.md
    ├── v01/
    │   ├── build.md
    │   ├── bom.csv
    │   ├── wiring.svg
    │   └── firmware/
    └── v02/
        ├── build.md
        ├── bom.csv
        ├── wiring.svg
        └── firmware/
```

Use `P###-short-name/` and `vNN/`. Start at `v01`; do not renumber historical IDs. When replacing the main controller, create a new `P###` and link the predecessor rather than overwriting its records.

## Prototype-level README

Create a `README.md` in each real `P###` directory to track:

| Field | What to record |
| --- | --- |
| Prototype ID and name | Main controller board/model; objective of this build |
| Status | Planned, built, tested, integrated, retired; link supporting evidence |
| Revisions | Revision IDs and concise change descriptions |
| Related records | Evaluation IDs, test runs, decisions and predecessor/successor prototype |
| Known limitations / next actions | Links to evidence or tasks rather than copied test data |

## Each revision: reproducible configuration

Use [the prototype-revision template](../templates/prototype_revision.md) as the starting point for `vNN/build.md`. Include or link:

- **Main controller:** exact board/model, hardware version if relevant, operating voltage, and pin assignments.
- **Components:** a `bom.csv` with parts, quantities, relevant ratings and identifying references.
- **Wiring:** schematic or `wiring.svg` where useful; supply, grounds, signals and LED drive.
- **Firmware:** source location, toolchain/libraries, build/flash instructions, configuration/thresholds, and the relevant Git commit.
- **Mechanical:** actual dimensions, sensor mounting, enclosure drawings or CAD files under `mechanical/` when relevant.
- **Build log:** configuration changes, identified issues, and how to reproduce the tested assembly.
- **Evidence:** links to [test runs](../tests/README.md); do not duplicate measurements here.

For firmware-only iteration, keep source history in Git; each test run must cite the **full commit SHA** plus configuration/thresholds. Avoid overwriting an earlier tested hardware revision's build specification; create a new revision when the hardware changes. Old firmware states remain reproducible through commits.

Use metric/SI units. Do not place a prototype on a dog before the [safety gate](../docs/safety.md) is satisfied and documented.
