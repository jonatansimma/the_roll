This is an illustrative target structure, not the current repository contents. The prototype names, technology evaluations, and test files shown are examples rather than completed project work.

# Project ROLL — Illustrative target repository structure

```text
the_roll/
│
├── README.md
├── AGENTS.md
├── design.md
├── roadmap.md
│
├── docs/
│   ├── requirements.md
│   ├── decisions.md
│   ├── safety.md
│   │
│   └── evaluations/
│       ├── EV001-pressure-switch.md
│       ├── EV002-capacitive-sensing.md
│       └── EV003-accelerometer.md
│
├── prototypes/
│   │
│   ├── P001-sensor-bench/
│   │   ├── README.md
│   │   │
│   │   ├── v01/
│   │   │   ├── build.md
│   │   │   ├── bom.csv
│   │   │   ├── wiring.svg
│   │   │   └── firmware/
│   │   │
│   │   └── v02/
│   │       ├── build.md
│   │       ├── bom.csv
│   │       ├── wiring.svg
│   │       └── firmware/
│   │
│   └── P002-integrated-roll/
│       ├── README.md
│       └── v01/
│           ├── build.md
│           ├── bom.csv
│           ├── wiring.svg
│           ├── mechanical/
│           └── firmware/
│
└── tests/
    │
    ├── procedures/
    │   ├── TP001-retrieval-detection.md
    │   ├── TP002-false-activation.md
    │   ├── TP003-power-consumption.md
    │   └── TP004-safety-inspection.md
    │
    └── runs/
        ├── YYYY-MM-DD-TR001.md
        └── YYYY-MM-DD-TR002.md
```
