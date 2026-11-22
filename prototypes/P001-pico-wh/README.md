# P001 — Raspberry Pi Pico WH retrieval bench prototype

- **Controller:** Raspberry Pi Pico WH (owner reports purchased; received/inspected/working state not yet recorded).
- **Status:** **Planned**, not assembled, tested or safe for dog exposure.
- **First revision:** [v01](v01/build.md) — simple off-dog LED plus simulated contact input, with optional external capacitive breakout.
- **Related evaluations:** [EV005 Pico WH](../../docs/evaluations/EV005-raspberry-pi-pico-wh.md) and [EV008 gentle grip sensing](../../docs/evaluations/EV008-light-grip-retrieval-sensing.md).
- **Requirements:** [Canonical requirements and reported retrieval considerations](../../docs/requirements.md).
- **Tests:** No completed runs. [Testing guidance](../../tests/README.md).
- **Next:** Inspect recycled LED and battery hardware, confirm component polarity/current/voltage, build v01, collect off-dog traces before choosing or integrating a final sensor.

Hardware sensor changes (e.g. a later IMU stack), LED circuitry changes, or mechanical integration should create a new **vNN** revision under P001; firmware-only changes remain traceable by commit.
