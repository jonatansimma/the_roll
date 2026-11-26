# P001 — Raspberry Pi Pico WH retrieval bench prototype

- **Controller:** Raspberry Pi Pico WH (owner reports purchased; received/inspected/working state not yet recorded).
- **Status:** **Planned**, not assembled, tested or safe for dog exposure.
- **Revisions:** [v01](v01/build.md) — simulated-contact bench design, preserved; [v02](v02/build.md) — purchased capacitive and accelerometer modules, synchronized logging and provisional contact-driven LED. Both planned, not built.
- **Related evaluations:** [EV005 Pico WH](../../docs/evaluations/EV005-raspberry-pi-pico-wh.md), [EV008 gentle grip sensing](../../docs/evaluations/EV008-light-grip-retrieval-sensing.md), [EV009 LIS3DH](../../docs/evaluations/EV009-electrokit-ekm029-lis3dh.md), [EV010 AT42QT1010](../../docs/evaluations/EV010-adafruit-1374-at42qt1010.md).
- **Requirements:** [Canonical requirements and reported retrieval considerations](../../docs/requirements.md).
- **Tests:** No completed runs. [Testing guidance](../../tests/README.md).
- **Next:** Inspect purchased hardware and recycled LED/battery parts, commission v02 off-dog, collect comparative traces using its linked procedure before choosing a final sensing strategy.

Hardware sensor changes (e.g. a later IMU stack), LED circuitry changes, or mechanical integration should create a new **vNN** revision under P001; firmware-only changes remain traceable by commit.
