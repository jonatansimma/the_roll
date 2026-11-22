# EV008 — Light-grip retrieval detection approaches

- **Status:** Research proposal; no sensors tested
- **Date:** 2026-11-22
- **Requirements:** [REQ001, REQ002, REQ006, REQ007](../requirements.md#functional-and-practical-requirements)
- **Context:** [Owner-reported retrieval behavior](../requirements.md#reported-retrieval-behavior--design-consideration-not-a-requirement)
- **Prototype:** [P001](../../prototypes/P001-pico-wh/README.md)

## Objective

Identify a sensing arrangement that can recognize intentional mouth retrieval despite an unusually gentle reported grip, occasional drop and re-pickup, and ordinary running/impact. No bite force is known. No sensor choice is validated or approved for dog exposure.

## Candidate comparison (engineering hypotheses)

| Approach | Strength | Limit / false-positive concern | First off-dog experiment |
| --- | --- | --- | --- |
| **Capacitive electrode under insulating body** (AT42QT1010 digital-output touch IC or comparable 3.3 V-compatible capacitive breakout) | May register contact without needing force; easy GPIO interface | Capacitive coupling through coating; water/saliva, wet ground, and hand/body proximity can cause false activations; one electrode cannot reliably tell a dog's mouth from other contact | Compare insulated electrode touch, light gloved contact, hovering, wet enclosure, handling and impacts |
| **Compliant pressure / force sensor** (thin FSR or custom flexure + switch) | Response can be tied to applied gripping load | An extremely gentle or shifting bite may not reach a reproducible threshold; point loads, hysteresis, mounting and moisture matter | Apply increasing calibrated tiny loads at several positions; compare grip vs bumps |
| **6-axis IMU** (LIS3DH accelerometer or LSM6DSOX accelerometer/gyro breakout) | All electronics can stay sealed inside body; detects movement transitions / drops | Motion does not uniquely identify mouth retrieval; running and falls can dominate; algorithm and placement demand trials | Log accelerations in pickup/run/drop/re-pickup vs normal collar/body movement |
| **Piezo/vibration** | Simple impact/touch cue; inexpensive | Mainly detects changes/impacts, not sustained light hold; prone to running and collisions | Compare bite-like taps with impacts; do not treat standalone result as retrieval |
| **Two independent sensing channels** | Contact plus movement sequence may reduce ambiguity | Extra electronics, algorithm tuning, power and false-negative risk | Collect synchronized raw records, then compare single-channel vs combined classification |

## Research conclusion and priority

**Preferred first experiment, not a final design selection:** capacitive contact sensor under a thin insulating layer, because it does not rely on high jaw force. Use a simple button as a controlled substitute for checking controller/software/LED operation. Add independent acceleration logging only if needed after testing contact sensing. Try force sensing if light-force mechanical coupling is practical. Do not assume that capacitive touch establishes dog-mouth identity, or that a drop should automatically end the indication.

**Unresolved firmware policy:** distinguish touch onset, release, brief lost contact, re-pickup, and normal running. Initial bench code may use a clearly labeled provisional hold-time; final LED latch/reset timing and scoring thresholds remain TBD in [requirements](../requirements.md).

## Electrical / mechanical considerations

- Raspberry Pi Pico WH GPIO is 3.3 V logic and not 5 V tolerant. Verify sensor breakout actual operating voltage and output high before wiring; avoid bare capacitive electrodes accessible to an animal.
- AT42QT1010-family touch boards commonly provide a digital trigger output and require an appropriate remote or onboard electrode; exact breakout pin polarity, quiescent current and timeout features depend on the board, so check its datasheet.
- Any electrode geometry, coating and proximity to grounded batteries affect sensitivity; characterize the actual enclosure rather than assuming free-air tests transfer.
- A low-cost I²C IMU such as LIS3DH can log acceleration; any board-specific I²C pull-ups, voltage rails, power consumption and dimensions require verification.
- Plan paired wet/dry, gentle/firm, held/released, repeat pickup, shaking, impact and ordinary handling comparisons using the same fixture. Record trial counts, raw data, timing, misses and false activations in [tests](../../tests/README.md); none are measured yet.
- Do all tests off-dog. The eventual integrated unit needs mechanical and electrical clearance per [safety](../safety.md) before supervised dog exposure.

## References

- [Microchip AT42QT1010 product/datasheet entry](https://www.microchip.com/en-us/product/AT42QT1010) — capacitive single-key digital sensing
- [Adafruit AT42QT1010 capacitive touch breakout guide](https://learn.adafruit.com/adafruit-at42qt1010-capacitive-touch-breakout) — example breakout interface and limitations
- [Adafruit LIS3DH accelerometer guide](https://learn.adafruit.com/adafruit-lis3dh-triple-axis-accelerometer-breakout) — external 3-axis motion sensor and I²C
- [Interlink FSR integration guide](https://www.interlinkelectronics.com/fsr-400-series) — force-sensitive resistor family; sensitivity depends on mechanical assembly
- [Pico W documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) and [Pico W datasheet](https://pip-assets.raspberrypi.com/categories/686-raspberry-pi-pico-w/documents/RP-008312-DS/pico-w-datasheet.pdf) — controller voltage, pins and power
