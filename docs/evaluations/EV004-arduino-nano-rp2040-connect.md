# EV004 — Arduino Nano RP2040 Connect (official reference board)

- **Status:** Researching — manufacturer-documentation evaluation only; second-hand item not visually verified, no bench tests
- **Problem / requirement IDs:** [REQ001, REQ002, REQ003, REQ004, REQ005, REQ008](../requirements.md#functional-and-practical-requirements)
- **Author and date:** ChatGPT desk research, 2026-11-08
- **Related records:** [EV001 D1 Mini](EV001-luxorparts-wemos-d1-mini.md), [evaluation guidelines](README.md), [prototype rules](../../prototypes/README.md), [test records](../../tests/README.md), [decisions](../decisions.md); no related prototype or test run exists

> **Identification scope:** The second-hand advertisement says only **“Arduino Nano RP2040”**. Searches identify the official Arduino **Nano RP2040 Connect** (Arduino board without headers: **ABX00052**; with headers: **ABX00053**). The header variants share the same controller design. This evaluation describes **that manufacturer-identified board**, not an inspected or authenticated second-hand item. Confirm the seller's actual board has the Nano RP2040 Connect identification and the specified on-board features before applying these specifications; an alternate RP2040 board would require separate identification and evaluation.

## Objective and operating principle

Assess the Arduino Nano RP2040 Connect as a main microcontroller for the Roll's **off-dog sensor-to-LED prototype**. It can sample external retrieval-sensor signals, run programmable detection/timing logic, and control a separate LED driver. The board also contains a 6-axis accelerometer/gyroscope (IMU), which may support a candidate **motion-sensing** experiment. Motion is not equivalent to intentional mouth retrieval; no sensing method is selected or validated.

## Candidate components and sources

| Candidate / part | Key specification | Source / datasheet | Estimated cost / availability |
| --- | --- | --- | --- |
| **Arduino Nano RP2040 Connect** (ABX00052 no headers; ABX00053 with headers) | Raspberry Pi **RP2040** dual-core Cortex-M0+ at **133 MHz**; **3.3 V I/O**, **8 mA per I/O pin**; **4–20 V VIN**; **16 MB external flash**, **264 KB SRAM**; 20 digital I/O and 8 analog inputs according to Arduino's board specification; 6-axis **LSM6DSOX** IMU, NINA-W102 Wi-Fi/Bluetooth, microphone and RGB LED; micro-USB; **45 × 18 mm**, **6 g** | [Arduino hardware documentation](https://docs.arduino.cc/hardware/nano-rp2040-connect/), [Arduino official store](https://store.arduino.cc/products/arduino-nano-rp2040-connect), [with-headers variant](https://store.arduino.cc/products/arduino-nano-rp2040-connect-with-headers) | **Second-hand price and condition unknown**. Official store lists **€23.90** as a new-unit reference at research time; verify current stock/prices. |

Arduino's hardware documentation currently marks the board **End of Life**; its store listing may still show stock. This is a supply-continuity consideration, not proof that the individual second-hand unit has a fault.

## Expected advantages, limitations, and uncertainties

- **Potential advantages:** programmable Arduino-class board, small 45 × 18 mm form factor, considerably more processing headroom and memory than an ATmega328P Nano, and a built-in IMU that could reduce wiring for *initial motion-sensing comparisons*. Built-in RGB LED is useful for software bring-up, though it does **not** establish required handler visibility.
- **Potential excess complexity:** Wi-Fi/Bluetooth, microphone and security circuitry are not known requirements for the Roll. Added components may increase idle-power complexity relative to a simpler controller; actual board-level consumption and power-gating behavior remain **unknown**.
- **3.3 V logic only:** do not connect 5 V sensor outputs directly to GPIO. The specified **8 mA/pin** is not a suitable assumption for powering a bright external LED arrangement; plan a current-limited LED driver with appropriate supply.
- **IMU detection uncertainty:** an accelerometer/gyroscope could detect motion associated with retrieval, but may also react to running, shaking, impacts or handler contact. Sensitivity, false activations, and effects of mounting position require experimental evaluation, not inference from chip presence.
- **Second-hand-specific unknowns:** whether the advertised board is genuinely the official Connect model, which header variant it is, its physical condition, USB functionality, sensor/radio functionality, and whether it boots and programs correctly. No seller photos, part number or test history were provided.
- **Lifecycle:** End-of-Life status complicates standardizing on it for future builds, although one functioning second-hand board may still be practical for a DIY experiment.

## Integration implications

- **Power:** Arduino lists **4–20 V VIN** and **3.3 V circuit operation**. Use the correct designated board input and regulated/protected power path; never apply an unregulated Li-Po cell to GPIO or a supply rail without validating the manufacturer's power instructions. The [EV002 D1 Mini battery shield](EV002-luxorparts-battery-shield.md) is **not presumed mechanically or electrically compatible** with this Nano board. Test power interfaces separately.
- **Sensors:** Check actual 3.3 V compatibility and wiring for any external capacitive, pressure, magnetic or other candidate module. An external analog sensor must respect this board's analog input limits. The on-board LSM6DSOX offers a potential no-extra-module motion experiment; a different sensor remains possible.
- **LEDs:** Use an externally rated output stage, series current limiting and supply budgeting for the final visible indication. The small built-in LED is only an initial test indicator.
- **Form factor:** Board is narrow, but fit cannot be claimed until the existing cylinder's available length/diameter are measured. Header pins, USB clearance, wiring, secure retention, moisture sealing and shock exposure will increase the required space.
- **Prototypes:** If selected as the **main controller**, it would define a separate **P###** prototype per [prototype identification policy](../../prototypes/README.md). This paper evaluation does not assign a prototype ID or approve a design.
- **Safety:** All initial work must be off-dog; any enclosed dog-exposure proposal is subject to the [documented safety gate](../safety.md).

## Proposed evaluation experiments

These are **proposed tests only**. Define reproducible [test procedures](../../tests/README.md), configurations, and pass/fail targets before recording results in test runs.

1. **Identify and inspect the actual used board:** photograph both faces; check markings (including `Nano RP2040 Connect` and/or ABX00052/ABX00053), USB connector and distinctive NINA-W102 module/LSM6DSOX implementation; inspect corrosion, damaged pads, headers and connector. **If the identification does not match, stop applying this evaluation.**
2. **Basic functionality:** power safely by USB on the bench; upload a known minimal Arduino sketch, confirm USB enumeration, serial output and a current-limited LED signal. Log any bootloader/firmware or used-board issues.
3. **Internal IMU experiment:** verify the LSM6DSOX can be read using a compatible library. Log acceleration/rotation traces during simulated retrieval-like movements and normal handling. Compare false activation rates only against defined conditions and thresholds.
4. **External sensing and LED drive:** connect a single compatible sensor and correctly rated LED driver; measure responsiveness and input-level integrity.
5. **Battery/runtime:** measure complete-board current in actual sensor sampling, radio-disabled idle, any intended sleep mode and active LED signaling, including peaks; then evaluate a *verified compatible* battery/regulator. Do not infer runtime from microcontroller-chip data alone.
6. **Mechanical verification:** measure effective populated-board size and compare it with the Roll's actual interior. Stop before dog use until inspection and documented safety clearance.

## Findings and evidence

| Finding | Classification | Evidence |
| --- | --- | --- |
| Official Nano RP2040 Connect has RP2040 processor, 3.3 V logic, VIN 4–20 V, integrated LSM6DSOX IMU and 45 × 18 mm footprint | **Published manufacturer specifications, not measured** | [Arduino board specifications](https://store.arduino.cc/products/arduino-nano-rp2040-connect) |
| Official Nano RP2040 Connect documentation is labeled End of Life | **Published manufacturer status** | [Arduino documentation](https://docs.arduino.cc/hardware/nano-rp2040-connect/) |
| “Arduino Nano RP2040” appears consistent with the official “Nano RP2040 Connect” reference board, but the used item's exact identity is not independently confirmed | **Name-based identification; actual listing unverified** | [Arduino official model](https://docs.arduino.cc/hardware/nano-rp2040-connect/); seller did not provide part number, photo or URL |
| Whether onboard IMU can distinguish retrieval from ordinary motion | **Unknown / hypothesis** | No experiment or test run |
| Current consumption, battery runtime, required LED brightness, cylinder fit, hardware condition | **Unknown** | No physical inspection or test run |

## Conclusion and next action

- **Assessment:** **Promising for exploratory bench work, but requires more evidence before selection or integration.**
- **Reasoning:** Built-in IMU makes the official board attractive as a *motion-detection test platform*, independent of whether motion ultimately proves useful. Its added radios, unknown board consumption, second-hand condition and documented End-of-Life status are limitations. The used board's identity still needs physical confirmation.
- **Next action / decision link:** Obtain a photograph or board marking from the second-hand listing; if confirmed as the official Connect model, test USB programming, IMU behavior and actual current. Log results in [tests](../../tests/README.md) and only then propose any hardware selection in [decisions](../decisions.md).

## References

- [Arduino Nano RP2040 Connect — official hardware documentation](https://docs.arduino.cc/hardware/nano-rp2040-connect/) (accessed 2026-11-08).
- [Arduino Nano RP2040 Connect — Arduino Store (ABX00052)](https://store.arduino.cc/products/arduino-nano-rp2040-connect) (accessed 2026-11-08).
- [Arduino Nano RP2040 Connect with Headers — Arduino Store (ABX00053)](https://store.arduino.cc/products/arduino-nano-rp2040-connect-with-headers) (accessed 2026-11-08).
- [Arduino guide to Nano-family hardware](https://docs.arduino.cc/learn/hardware/nano-pcb-guide/) (accessed 2026-11-08).
