# EV009 — Electrokit EKM029 LIS3DH three-axis accelerometer breakout

- **Status:** Researching — desk evaluation only; **not bench-tested, validated, selected as the final sensing solution, or approved for dog exposure**. Acquisition and experimental integration status: [P001-v02](../../prototypes/P001-pico-wh/v02/build.md)
- **Problem / requirement IDs:** [REQ001–REQ003, REQ004–REQ006, REQ008–REQ009](../requirements.md#functional-and-practical-requirements)
- **Author and date:** ChatGPT research, 2026-11-22
- **Related evaluations:** [EV005 Pico WH](EV005-raspberry-pi-pico-wh.md), [EV007 Arduino Modulino Movement](EV007-arduino-modulino-movement.md), [EV008 light-grip approaches](EV008-light-grip-retrieval-sensing.md), [EV010 capacitive breakout](EV010-adafruit-1374-at42qt1010.md)
- **Test evidence:** No test runs. Follow [tests](../../tests/README.md); decisions remain unrecorded on `main`.

## Objective and operating principle

Investigate whether **Electrokit EKM029, fitted with STMicroelectronics LIS3DH**, is useful for recognizing motion patterns associated with retrieving, carrying, dropping and re-picking up the Roll. This is a **3-axis accelerometer**, **not** a 6-axis accelerometer/gyroscope: it measures linear acceleration including gravity, but **does not directly measure angular velocity**. Motion by itself cannot identify intentional mouth contact. The owner's report of a very gentle grip with occasional mid-run drops is a **design consideration**, documented as an unmerged proposal on `agent_main` in [requirements](../requirements.md), not a quantitative force requirement.

## Candidate components and sources

| Candidate | Published specification / observation | Source | Sweden price / availability checked 2026-11-22 |
| --- | --- | --- | --- |
| **Electrokit EKM029 - LIS3DH - 3DOF**, article **4103 6175** | Board **23 × 18 mm**; **1.7–3.6 V** board supply (3.3 V nominal); I²C on two Qwiic/JST-SH connectors and header pads; SPI via pads; header strip included **not pre-soldered**; 2 programmable interrupt outputs; **I²C 7-bit 0x19 default**, optionally **0x18** by the `I2C ADR` solder jumper; I²C line pull-ups **4.7 kΩ**, cuttable `I2C PU` jumper | [Electrokit product](https://www.electrokit.com/3-axlig-accelerometer-qwiic), [EKM029 board documentation](https://docs.electrokit.com/en/modules/EKM029/index.html) | **89 SEK incl. VAT**, displayed in stock at the review; supplier information may change |
| **LIS3DH IC**, STMicroelectronics | **1.71–3.6 V** chip supply; selectable **±2/±4/±8/±16 g** ranges; I²C/SPI; 32-sample FIFO; configurable wake-up/free-fall/orientation interrupts; selectable measurement rates; indicative **2 µA normal 1 Hz**, **6 µA low-power 50 Hz**, **11 µA normal 50 Hz**, **0.5 µA power-down** at stated chip test conditions | [ST LIS3DH product](https://www.st.com/en/mems-and-sensors/lis3dh.html), [ST datasheet](https://www.st.com/resource/en/datasheet/lis3dh.pdf) | Figures are **IC-only**, not measured full-board current or purchase prices |

**Documentation discrepancy:** EKM029's overview describes `A0` and `A1` jumpers and claims up to **four** devices on one I²C bus, while its detailed address section documents **only** `0x19` and `0x18`, implying up to **two** unique addresses. The LIS3DH chip also provides a single selectable I²C address bit. **For firmware and purchasing, assume 0x19/0x18 only**, and confirm with a physical I²C scan; do not plan on four addresses without supplier clarification.

## Expected advantages, limitations, and uncertainties

### Expected benefits / untested hypotheses

- Small external 3-axis module can sit inside a protective enclosure with no exposed mechanical switch; may register pickup transitions, impacts, drops, stillness and changes in orientation.
- Configurable FIFO and interrupt event detection offer a possible lower-duty-cycle, battery-efficient acquisition strategy, if wake support and software are validated.
- Simple 3.3 V I²C connection to the [Pico WH candidate](EV005-raspberry-pi-pico-wh.md). Qwiic eases a bench setup, but requires a compatible cable / adapter at the Pico end.
- Can record synchronized motion traces alongside a separate mouth-contact cue such as [EV010](EV010-adafruit-1374-at42qt1010.md) to compare standalone vs combined detection.

### Limitations / failure modes

- **Motion is not mouth retrieval.** Running, jumping, shaking, neck movement, dropping, collisions and handler manipulation can resemble pickup. A slow or smooth pickup can be missed.
- No gyroscope, unlike [EV007](EV007-arduino-modulino-movement.md); accelerometer gravity-vector change can infer orientation approximately, but does not measure rotation rate.
- IC-only microampere numbers do not cover board traces, pull-ups during bus activity, sensors in active modes, Pico WH radio/CPU or LEDs. EKM029 **whole-module current and mass are not established**.
- Need rigid, stable mounting and known axis orientation; movement of a loose breakout is not necessarily movement of the Roll.
- Output sensitivity, sample rate, clipping, filtering, power consumption and algorithm latency trade off against one another. No evaluated pickup classifier or recorded labeled datasets exist.
- Published **23 × 18 mm PCB** is not a demonstration of installed fit inside the [full enclosure/body/mass constraints](../requirements.md#dimensional-and-mass-targets). Qwiic plugs, wire bend radius, battery and other parts must be included.

## Integration implications

- **Pico WH and 3 × AAA proposal:** Three alkaline AAA cells are **nominally 4.5 V in series**; three NiMH AAA cells are **nominally 3.6 V**. The [Pico WH's VSYS input](EV005-raspberry-pi-pico-wh.md) is rated approximately **1.8–5.5 V**. Feed the battery to **VSYS/GND**, with USB disconnected during a basic battery-only bench test; feed this breakout with **Pico 3V3(OUT)/GND**, **never the direct three-cell pack**. Both logic and pull-ups must be at 3.3 V, not battery voltage. Do not use three rechargeable **3.7 V 10440** cells in series for this arrangement.
- **Data/interrupt wiring:** V+ (3.3 V), GND, SDA, SCL to a configured Pico I²C bus. Optional `INT1` or `INT2` to another 3.3 V GPIO for event logging/wake testing. Confirm microcontroller pin assignments during prototype revision design. EKM029's **4.7 kΩ** pull-ups already bias SDA/SCL; review total parallel pull-ups when adding modules.
- **Supply protection:** Electrokit cautions **not to power both via V+ pins and a Qwiic connector simultaneously**. Choose a single supply route and common ground.
- **Logic/interface:** Verify actual I²C address by scanning before code integration; 0x19 is the documented board default. For optional analog channels, Electrokit lists a restricted useful ADC range of about **0.8–1.6 V**, which is **not** a substitute for the Pico's usual ADC range.
- **Power budget:** The 3 × AAA hypothesis is electrically plausible, **not** proof of either [mandatory/preferred runtime](../requirements.md#operating-time-requirements). Measure battery input current with the controller plus both sensors, Wi-Fi choice and representative LED usage, then perform actual endurance trials.
- **Mechanical/safety:** Exposed board, Qwiic connector and wiring are bench-only. The eventual enclosed assembly requires secure internal mounting, water/saliva isolation, impact/bite integrity, correct attachment and review of [dog-exposure prerequisites](../safety.md).

## Proposed evaluation experiments (none performed)

1. Inspect the delivered PCB and connector/headers, record measured breakout mass and three-dimensional installed envelope. Verify a stable 3.3 V rail and scan for `0x19` (`0x18` only if configured).
2. Sample `x/y/z` at documented rate(s) and measurement ranges. Rotate a bench fixture and apply known controlled movements; record axes, raw series, timestamps, settings and current.
3. Simulate collar-like running/handling, deliberate slow pickup, fast pickup, carried motion, release/drop, re-pickup, impacts, shaking, and false-trigger conditions. Label event windows; compare misses, false positives and latency.
4. Repeat with rigid and loose mounting to quantify sensitivity to fixture effects; then re-test inside a **sealed dummy enclosure off-dog**.
5. Evaluate an interrupt-driven low-power configuration against continuous polling; measure **complete-board / Pico / LED** current (active and idle) under 3 × AAA power.
6. Optionally synchronize with capacitive contact data from [EV010](EV010-adafruit-1374-at42qt1010.md) and assess if combining channels improves discrimination; decide from documented tests rather than assumption. Acceptance thresholds remain to be set in [requirements](../requirements.md).

## Findings and evidence

| Finding | Classification | Evidence |
| --- | --- | --- |
| EKM029 is a 23 × 18 mm, 3.3 V nominal, 0x19-default LIS3DH breakout with Qwiic/I²C and interrupts | Published board specification | Electrokit product and EKM029 documentation |
| LIS3DH supports 1.71–3.6 V supply and ultra-low-power chip modes; **no gyroscope** | Manufacturer specification | ST product page/datasheet |
| EKM029 documentation conflicts over number of unique I²C addresses | Documentation inconsistency | Same supplier EKM029 page |
| Regulated 3.3 V from a battery-fed Pico WH is a plausible supply | Engineering compatibility assessment | Pico WH evaluation + supplier limits |
| Ability to detect an intentional gentle-bite retrieval, module current, response time, enclosure fit, mass and 1 h/12 h endurance | **Unknown / untested** | No bench tests or integrated build |

## Conclusion and next action

- **Assessment:** **Promising secondary sensor for controlled off-dog movement characterization; not validated as standalone retrieval detector.**
- **Reasoning:** The I²C connection and power requirements fit a Pico WH test setup, and the low-current LIS3DH chip has relevant interrupt/FIFO capabilities. The fundamental risk is motion ambiguity, not supply voltage.
- **Next action / decision link:** Bench-log motion sequences using the proposed [P001-v02 revision](../../prototypes/P001-pico-wh/v02/build.md), compare with [EV010](EV010-adafruit-1374-at42qt1010.md) only when data justify combining them, record results in [tests](../../tests/README.md), and register an actual selection (if any) in [decisions](../decisions.md). **No prototype selection or project requirement changes were made here.**

## References

- [Electrokit Sweden, EKM029 LIS3DH product (article 4103 6175)](https://www.electrokit.com/3-axlig-accelerometer-qwiic), reviewed 2026-11-22.
- [Electrokit EKM029 board documentation — wiring, pull-ups, pin functions and address jumper](https://docs.electrokit.com/en/modules/EKM029/index.html), reviewed 2026-11-22.
- [STMicroelectronics LIS3DH product information](https://www.st.com/en/mems-and-sensors/lis3dh.html), reviewed 2026-11-22.
- [STMicroelectronics LIS3DH datasheet](https://www.st.com/resource/en/datasheet/lis3dh.pdf), reviewed 2026-11-22.
- [Raspberry Pi Pico WH power and GPIO comparison — EV005](EV005-raspberry-pi-pico-wh.md).
