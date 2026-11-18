# EV004 — Arduino Nano RP2040 Connect (official reference board)

- **Status:** Researching — manufacturer's board identity corroborated by photos of the listed retail packaging; actual board, package sealing, and functionality unverified; no bench tests
- **Problem / requirement IDs:** [REQ001, REQ002, REQ003, REQ004, REQ005, REQ008](../requirements.md#functional-and-practical-requirements)
- **Author and date:** ChatGPT desk research and review of user-supplied listing photos, 2026-11-08
- **Related records:** [EV001 D1 Mini](EV001-luxorparts-wemos-d1-mini.md), [evaluation guidelines](README.md), [prototype rules](../../prototypes/README.md), [test records](../../tests/README.md), [decisions](../decisions.md); no related prototype or test run exists

> **Identification scope (updated 2026-11-08):** The advertisement initially called this **“Arduino Nano RP2040”**. User-provided screenshots of the second-hand listing show the **front and back of a retail box** printed **“ARDUINO NANO RP2040 CONNECT WITH HEADERS”**; the back prints Arduino's store URL for that with-headers variant. Arduino identifies the official with-headers model as **ABX00053** (without headers: ABX00052). This resolves the **advertised retail-package model**, not the identity, authenticity, completeness, or functionality of any board inside. The seller reportedly calls it **unopened**, but no unbroken seal or actual board is independently confirmed by these photographs. The evaluation applies to the specified manufacturer's model only; visually inspect the PCB if the package is eventually opened.

## Objective and operating principle

Assess the Arduino Nano RP2040 Connect as a main microcontroller for the Roll's **off-dog sensor-to-LED prototype**. It can sample external retrieval-sensor signals, run programmable detection/timing logic, and control a separate LED driver. The board also contains a 6-axis accelerometer/gyroscope (IMU), which may support a candidate **motion-sensing** experiment. Motion is not equivalent to intentional mouth retrieval; no sensing method is selected or validated.

## Candidate components and sources

| Candidate / part | Key specification | Source / datasheet | Estimated cost / availability |
| --- | --- | --- | --- |
| **Arduino Nano RP2040 Connect with Headers** (ABX00053 as shown on box; ABX00052 is separate no-headers option) | Raspberry Pi **RP2040** dual-core Cortex-M0+ at **133 MHz**; **3.3 V I/O**, **8 mA per I/O pin**; **4–20 V VIN**; **16 MB external flash**, **264 KB SRAM**; 20 digital I/O and 8 analog inputs according to Arduino's board specification; 6-axis **LSM6DSOX** IMU, NINA-W102 Wi-Fi/Bluetooth, microphone and RGB LED; micro-USB; **45 × 18 mm**, **6 g** | [Arduino hardware documentation](https://docs.arduino.cc/hardware/nano-rp2040-connect/), [Arduino official store](https://store.arduino.cc/products/arduino-nano-rp2040-connect), [with-headers variant](https://store.arduino.cc/products/arduino-nano-rp2040-connect-with-headers) | **Second-hand price and condition unknown**. Official store lists **€23.90** as a new-unit reference at research time; verify current stock/prices. |

Arduino's hardware documentation currently marks the board **End of Life**; its store listing may still show stock. This is a supply-continuity consideration, not proof that the individual second-hand unit has a fault.

## Expected advantages, limitations, and uncertainties

- **Potential advantages:** programmable Arduino-class board, small 45 × 18 mm form factor, considerably more processing headroom and memory than an ATmega328P Nano, and a built-in IMU that could reduce wiring for *initial motion-sensing comparisons*. Built-in RGB LED is useful for software bring-up, though it does **not** establish required handler visibility.
- **Potential excess complexity:** Wi-Fi/Bluetooth, microphone and security circuitry are not known requirements for the Roll. Added components may increase idle-power complexity relative to a simpler controller; actual board-level consumption and power-gating behavior remain **unknown**.
- **3.3 V logic only:** do not connect 5 V sensor outputs directly to GPIO. The specified **8 mA/pin** is not a suitable assumption for powering a bright external LED arrangement; plan a current-limited LED driver with appropriate supply.
- **IMU detection uncertainty:** an accelerometer/gyroscope could detect motion associated with retrieval, but may also react to running, shaking, impacts or handler contact. Sensitivity, false activations, and effects of mounting position require experimental evaluation, not inference from chip presence.
- **Second-hand-specific unknowns:** the pictured **retail package** says “Nano RP2040 Connect with Headers” (corresponding to Arduino SKU **ABX00053**). The board itself is **not shown**; whether it is present, genuine, undamaged and operational is unknown. The seller describes the package as unopened, but the photos do **not independently establish a factory seal**. USB, sensor, radio, boot and programming functionality remain untested.
- **Lifecycle:** End-of-Life status complicates standardizing on it for future builds, although one functioning second-hand board may still be practical for a DIY experiment.

## Integration implications

- **Power:** Arduino lists **4–20 V VIN** and **3.3 V circuit operation**. The photographed box instead prints **4.5–21 V** for VIN; this **published-label discrepancy** should be resolved using the manufacturer's current board specifications and actual board revision before selecting a power source (do not assume the wider packaging range is safe). Use the correct designated board input and regulated/protected power path; never apply an unregulated Li-Po cell to GPIO or a supply rail without validating the manufacturer's power instructions. The [EV002 D1 Mini battery shield](EV002-luxorparts-battery-shield.md) is **not presumed mechanically or electrically compatible** with this Nano board. Test power interfaces separately.
- **Sensors:** Check actual 3.3 V compatibility and wiring for any external capacitive, pressure, magnetic or other candidate module. An external analog sensor must respect this board's analog input limits. The on-board LSM6DSOX offers a potential no-extra-module motion experiment; a different sensor remains possible.
- **LEDs:** Use an externally rated output stage, series current limiting and supply budgeting for the final visible indication. The small built-in LED is only an initial test indicator.
- **Form factor:** Board is narrow, but fit cannot be claimed until the existing cylinder's available length/diameter are measured. Header pins, USB clearance, wiring, secure retention, moisture sealing and shock exposure will increase the required space.
- **Prototypes:** If selected as the **main controller**, it would define a separate **P###** prototype per [prototype identification policy](../../prototypes/README.md). This paper evaluation does not assign a prototype ID or approve a design.
- **Safety:** All initial work must be off-dog; any enclosed dog-exposure proposal is subject to the [documented safety gate](../safety.md).

## Proposed evaluation experiments

These are **proposed tests only**. Define reproducible [test procedures](../../tests/README.md), configurations, and pass/fail targets before recording results in test runs.

1. **Confirm contents and inspect the actual used board if acquired:** keep a record of any packaging/seal and product identification; then photograph both PCB faces, check board markings, headers, USB connector and distinct onboard components; inspect corrosion, damaged pads, headers and connector. **If the board does not match the pictured model, stop applying this evaluation.**
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
| Listing photos depict a retail box labeled **Arduino Nano RP2040 Connect WITH HEADERS**; manufacturer identifies with-headers board as **ABX00053**. Box contents and condition remain unverified. | **Observed retail-packaging evidence + manufacturer model mapping; not a PCB inspection** | User-provided front/back listing screenshots, 2026-11-08 (not archived in repository); [Arduino SKU ABX00053](https://store.arduino.cc/products/arduino-nano-rp2040-connect-with-headers) |
| Retail box prints **VIN 4.5–21 V**, while Arduino store lists **VIN 4–20 V** | **Unresolved specification discrepancy; use verified manufacturer limits pending revision-specific check** | User-provided back-of-box screenshot, 2026-11-08; [Arduino product specification](https://store.arduino.cc/products/arduino-nano-rp2040-connect-with-headers) |
| Whether onboard IMU can distinguish retrieval from ordinary motion | **Unknown / hypothesis** | No experiment or test run |
| Current consumption, battery runtime, required LED brightness, cylinder fit, hardware condition | **Unknown** | No physical inspection or test run |

## Requirement-fit review — 2026-11-08 (desk assessment)

Compared against [current requirements](../requirements.md), including [physical limits and total mass](../requirements.md#dimensional-and-mass-targets) and [mandatory/preferred operating times](../requirements.md#operating-time-requirements).

- **Physical integration (REQ005):** The published **45 × 18 mm** PCB is plausibly narrow/short enough for an axial layout, and the stated **6 g** board mass appears compatible with investigating the assembly mass target. **Neither proves** that the with-headers board, battery, enclosure walls, LED and attachment all fit together.
- **Detection/indication (REQ001–REQ003):** The integrated LSM6DSOX IMU provides a motion-sensor input without a separate motion board, and GPIO can command a properly rated LED driver. Whether motion differentiates deliberate retrieval from other dog/handler movements is **unproven**; LED brightness and false-activation performance are unmeasured.
- **Operating time (REQ004):** Active, sensing-idle and low-power whole-board consumption have not been measured; no demonstrated compliant battery configuration. Additional radio features do not in themselves satisfy a requirement.
- **Safety (REQ006, REQ009):** Appropriate power supply, secure mounts, moisture protection, thermal/impact checks, animal-exposure clearance and actual condition of the second-hand board remain unresolved.
- **Classification:** **Plausible controller candidate, especially for initial IMU experiments; not validated as a compliant assembled Roll.**

## Conclusion and next action

- **Assessment:** **Promising for exploratory bench work, but requires more evidence before selection or integration.**
- **Reasoning:** Built-in IMU makes the official board attractive as a *motion-detection test platform*, independent of whether motion ultimately proves useful. Box images identify the **advertised with-headers model**, but the actual board, original seal, condition, supply characteristics and functioning remain unknown. Added radios, unknown board consumption and End-of-Life status remain limitations.
- **Next action / decision link:** If acquired, verify box contents and board identity, inspect pins/headers, and reconcile the VIN-range discrepancy before powering via VIN; then test USB programming, IMU behavior and actual current. Log results in [tests](../../tests/README.md) and only then propose any hardware selection in [decisions](../decisions.md).

## References

- [Arduino Nano RP2040 Connect — official hardware documentation](https://docs.arduino.cc/hardware/nano-rp2040-connect/) (accessed 2026-11-08).
- [Arduino Nano RP2040 Connect — Arduino Store (ABX00052)](https://store.arduino.cc/products/arduino-nano-rp2040-connect) (accessed 2026-11-08).
- [Arduino Nano RP2040 Connect with Headers — Arduino Store (ABX00053)](https://store.arduino.cc/products/arduino-nano-rp2040-connect-with-headers) (accessed 2026-11-08).
- [Arduino guide to Nano-family hardware](https://docs.arduino.cc/learn/hardware/nano-pcb-guide/) (accessed 2026-11-08).
- Two user-provided screenshots of the **front and rear of the second-hand product box** in the project conversation, 2026-11-08. Described here as unarchived visual evidence; no photograph of the PCB or verified seal was provided.
