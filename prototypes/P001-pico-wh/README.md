# P001 — Raspberry Pi Pico WH retrieval bench prototype

- **Controller:** Raspberry Pi Pico WH (owner reports purchased; received/inspected/working state not yet recorded).
- **Status:** **Planned**, not assembled, tested or safe for dog exposure.
- **Revisions:** [v01](v01/build.md) — simulated-contact design, superseded before build; [v02](v02/build.md) — dual-sensor battery-capable design with external test LED, superseded before build; [v03](v03/build.md) — USB-only dual-sensor design with onboard LED, intended first physical build. All remain unbuilt.
- **Related evaluations:** [EV005 Pico WH](../../docs/evaluations/EV005-raspberry-pi-pico-wh.md), [EV008 gentle grip sensing](../../docs/evaluations/EV008-light-grip-retrieval-sensing.md), [EV009 LIS3DH](../../docs/evaluations/EV009-electrokit-ekm029-lis3dh.md), [EV010 AT42QT1010](../../docs/evaluations/EV010-adafruit-1374-at42qt1010.md).
- **Requirements:** [Canonical requirements and reported retrieval considerations](../../docs/requirements.md).
- **Tests:** No completed runs. [Testing guidance](../../tests/README.md).
- **Next:** Inspect purchased sensors and commission v03 off-dog using its linked USB-only procedure. Defer battery and external LED integration to later hardware revisions.

Hardware sensor changes (e.g. a later IMU stack), LED circuitry changes, or mechanical integration should create a new **vNN** revision under P001; firmware-only changes remain traceable by commit.
