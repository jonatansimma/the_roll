# EV005 — Raspberry Pi Pico WH (RP2040 wireless microcontroller)

- **Status:** Researching — product identified from second-hand listing photo; specification research only, no hands-on or bench validation
- **Problem / requirement IDs:** [REQ001–REQ005, REQ008–REQ009](../requirements.md#functional-and-practical-requirements); in particular, [dimensions and mass](../requirements.md#dimensional-and-mass-targets) and [operating-time requirements](../requirements.md#operating-time-requirements)
- **Author and date:** ChatGPT review of user-provided listing photograph and manufacturer documentation, 2026-11-08
- **Related records:** [EV004 Arduino Nano RP2040 Connect](EV004-arduino-nano-rp2040-connect.md), [EV001 D1 Mini](EV001-luxorparts-wemos-d1-mini.md), [EV003 battery candidate](EV003-luxorparts-lipo-1200mah.md), [test records](../../tests/README.md), [decision register](../decisions.md); no prototype or test run exists for this board.

> **Identity and evidence scope:** A user-provided screenshot of a second-hand listing (2026-11-08; photograph not archived in the repository) shows the **actual component side of a green Raspberry Pi Pico-family PCB**. Visible identification includes **“Raspberry Pi Pico WH © 2022”** silkscreen, the RP2040 chip, the metal-shielded wireless section, a central keyed three-contact debug connector, and a micro-USB port. This combination closely matches Raspberry Pi's official **Pico WH**, the header-equipped version of Pico W, rather than Pico W, Pico H or Pico 2 W. The image supports **high-confidence model identification**, but is not proof of authenticity, operation, absence of damage on the reverse side, or possession by the seller. The listing price, electrical test history and actual mass are unknown.

## Objective and operating principle

Determine whether the **Raspberry Pi Pico WH** can be the main controller of a battery-powered Project ROLL **off-dog** sensor-to-LED experiment. This RP2040 microcontroller reads **external** sensor signals, makes software-configurable retrieval decisions, and controls a correctly rated external LED circuit.

**Important detection distinction:** The Pico WH has **no onboard accelerometer or gyroscope**. Unlike the [Arduino Nano RP2040 Connect evaluation](EV004-arduino-nano-rp2040-connect.md), a motion-based method on Pico WH needs a separate inertial sensor or other independent detection mechanism. No method has been selected; detecting motion alone does not establish intentional mouth retrieval.

## Candidate components and sources

| Candidate / part | Key specification | Source / datasheet | Estimated cost / availability |
| --- | --- | --- | --- |
| Raspberry Pi **Pico WH**, first-generation Pico W variant **with pre-soldered 2 × 20-pin headers** and keyed three-pin SWD debug connector | **RP2040**: dual-core Arm Cortex-M0+, up to **133 MHz**, **264 kB SRAM**, **2 MB external flash**; **26 user GPIO, 3 ADC-capable**; **3.3 V I/O (not 5 V tolerant)**; **2 × I²C, 2 × SPI, 2 × UART, PWM**; **2.4 GHz 802.11n Wi-Fi / Bluetooth 5.2**; **51 × 21 mm PCB**, micro-USB; regulator accepts **approximately 1.8–5.5 V on VSYS** per Pico W datasheet (power-path constraints apply) | [Raspberry Pi Pico-family documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html), [official Pico W datasheet applicable to the wireless RP2040 board electronics](https://pip-assets.raspberrypi.com/categories/686-raspberry-pi-pico-w/documents/RP-008312-DS/pico-w-datasheet.pdf); user-supplied listing photograph | **Second-hand price and actual condition unknown.** Photo shows no identifiable functional test. Supplier availability/pricing should be checked at purchase time. |

**Variant distinction:** Raspberry Pi documents Pico W and **Pico WH as electrically functionally equivalent**. The WH includes factory-fitted GPIO headers and a **keyed three-pin SWD debug connector**; the W lacks headers and exposes three debug pads. Do **not** confuse the 3-pin SWD connector with a power or battery connector: it carries **SWDIO, GND, SWCLK** and **no power pin**.

## Expected advantages, limitations, and uncertainties

### Potential advantages

- **Practical microcontroller for bench testing:** flash by USB/BOOTSEL; MicroPython or C/C++ development, with third-party Arduino IDE ecosystem support to be verified against the exact core and wireless features used.
- **I/O flexibility:** plenty of 3.3 V pins for basic switches, capacitive-sensor modules, I²C motion sensors, and a separate LED driver.
- **Battery-input flexibility:** the onboard 3.3 V buck-boost supply can accept a properly connected battery supply via **VSYS**; it is **not necessary to add a generic 5 V booster solely to power the Pico WH**. This can simplify comparison with [EV002, the D1 Mini-specific power module](EV002-luxorparts-battery-shield.md), which should **not** be presumed mechanically compatible with the Pico.
- **Headers make initial breadboard work easy**; ready-made SWD debug socket supports diagnostics.

### Constraints and unknowns

- **No onboard retrieval sensor:** an inertial sensing approach will need external hardware, increasing wiring, assembly complexity, mass and current relative to a board with an IMU.
- **Wireless functionality is optional, not a stated requirement.** Radio power and firmware support can complicate low-power operation. **Whole-board current** in real sensing and LED duty cycles, with radios enabled/disabled, is **unknown**. Datasheet microcontroller sleep figures are not valid whole-board current measurements.
- **Pre-soldered headers are a mechanical disadvantage for the final enclosure:** they increase occupied depth, create exposed sharp/conductive features and complicate sealed protective mounting. They are useful on a bench but must be safely contained or a board without headers may be preferable for integration.
- **3.3 V GPIO:** verify level compatibility of external devices. Do not connect a 5 V logic output or an unregulated battery directly to a GPIO/ADC pin. Size LED supply/driver and resistors to their own ratings; do not assume the GPIO directly powers a handler-visible LED array.
- **No onboard battery charger or complete lithium-cell protection:** an external appropriate charging, protection and power-selection arrangement is needed when using rechargeable Li-Po cells. The Pico's buck-boost regulator does not substitute for a charger or battery safety circuit.
- **Used-board condition:** no underside photograph, continuity/USB/firmware check, header inspection or observed output is available. One angle alone cannot establish physical condition or functional safety.

## Integration implications

- **Geometry:** The **51 × 21 mm** board is shorter/narrower than the project's [nominal 120 mm × 35 mm cylindrical body envelope](../requirements.md#dimensional-and-mass-targets), but this simple 2D comparison **does not demonstrate fit**. Measure the actual *header-inclusive* 3D envelope (USB socket, RF can, SWD socket, wiring and strain relief) and the space left for enclosure walls, battery, LEDs and sensors. The assembled system must be assessed against the [50 g total-mass target](../requirements.md#dimensional-and-mass-targets). The geometry and pack constraints of the existing [EV003 cell candidate](EV003-luxorparts-lipo-1200mah.md) require a separate fit check.
- **Run time:** [REQ004](../requirements.md#operating-time-requirements) requires **at least 1 hour** operation and aims for **12 hours** without charging or battery replacement. Neither has been measured, and no representative event duty cycle has yet been fixed. Radio-off operation and sensor wake strategy are test hypotheses, not validated battery solutions.
- **Power path:** Manufacturer's wireless-board datasheet describes approximately **1.8–5.5 V at VSYS (pin 39)** via an onboard 3.3 V regulator. Powering by USB goes via **VBUS (pin 40)** and a diode. **Do not hard-wire a battery to VSYS and then attach USB without reviewing the manufacturer's recommended dual-source power-ORing circuit**; avoid accidental back-feed. Use the correct voltage at the correct pin, verify ground, and choose suitable lithium-cell charge/protection hardware independently.
- **Sensing:** External motion, pressure or capacitive modules may be integrated over compatible digital/I²C/analog inputs. Analog signals must stay within 0–3.3 V. A pressure-only or simple switch experiment does not need the board's radio.
- **Output:** Reserve GPIO only as a logic signal; use a rated LED switching stage and current-limiting components, and measure LED peak input current and microcontroller resets.
- **Safety:** An exposed development board, pin headers and any accessible lithium cell are inappropriate for dog exposure. Apply [the required off-dog sequence and physical/electrical safety gate](../safety.md). This evaluation is not a safe-enclosure approval.

## Proposed evaluation experiments

These are **proposed procedures, not completed tests**. Create actual [test procedures and runs](../../tests/README.md); specify board identity, firmware commit and configuration for any run.

1. **Confirm second-hand board and condition:** If acquired, record PCB markings and both sides, inspect headers and solder joints, look for damage/corrosion and check the micro-USB and SWD connector mechanically. Record measured PCB + header dimensions and mass.
2. **Bring-up off-dog:** Run from known-good USB supply; enter BOOTSEL/UF2 programming mode, flash minimal MicroPython or C/C++/Arduino-compatible code, confirm serial output and a low-current test LED. Verify the selected board package and GPIO mapping.
3. **Sensor and LED-interface trial:** Connect a chosen 3.3 V-compatible switch or sensing module to GPIO/I²C; record response latency, missed simulated retrievals and false triggers from normal handling. Add an appropriately rated external LED driver; investigate rail sag/reset events.
4. **Current and battery study:** Measure actual complete-board supply current during boot, active sensing, radio idle/off where implementable, low-power wake and LED signaling. Test a verified, protected supply at VSYS with USB disconnected or properly isolated; calculate projected operating time using recorded load profile and measured usable battery energy. Check both the [hard 1-hour and preferred 12-hour goals](../requirements.md#operating-time-requirements).
5. **Enclosure and hazard check:** Test the complete component stack within the [physical and mass limits](../requirements.md#dimensional-and-mass-targets); inspect secure internal mounting, header isolation, LED visibility, battery retention, impact exposure and moisture risks. Do not proceed to any supervised animal testing without the documented [safety gate](../safety.md).

## Findings and evidence

| Finding | Classification | Evidence |
| --- | --- | --- |
| Photo shows Pico-family **“WH”** silkscreen, RP2040, shielded radio, keyed central SWD connector and micro-USB | **Visual observation of listing photo; no hands-on verification** | User-supplied second-hand listing screenshot, 2026-11-08, not archived to repository |
| WH variant includes factory-installed 40-pin header arrangement and keyed SWD; Pico W has no header | **Published manufacturer specification** | [Raspberry Pi Pico series](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) |
| RP2040 133 MHz dual-core, 264 kB SRAM, 2 MB flash; 51 × 21 mm PCB; 3.3 V I/O | **Published manufacturer specification, not measured** | [Official Pico W datasheet](https://pip-assets.raspberrypi.com/categories/686-raspberry-pi-pico-w/documents/RP-008312-DS/pico-w-datasheet.pdf) |
| Onboard IMU/gyroscope not provided; motion sensing requires an external device | **Published board-feature assessment / integration inference** | [Raspberry Pi Pico-series feature list](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html), [EV004 comparison](EV004-arduino-nano-rp2040-connect.md) |
| Internal buck-boost produces 3.3 V from a broad VSYS input range; does not supply lithium charging/protection | **Published circuit information / integration inference** | [Official Pico W datasheet, powerchain/charging sections](https://pip-assets.raspberrypi.com/categories/686-raspberry-pi-pico-w/documents/RP-008312-DS/pico-w-datasheet.pdf) |
| Board condition, whole-system power, achieved 1 h/12 h runtime, mass, water/impact resistance, false positives and 3D fit | **Unknown / untested** | No test runs, complete BOM or measured configuration |

## Conclusion and next action

- **Assessment:** **Promising as a general-purpose off-dog controller; requires more evidence before selection or integration.**
- **Reasoning:** High-confidence photographic identity and accessible interfaces, compact PCB, broad battery-input options and uncomplicated USB development make a good bench candidate. However, it lacks an IMU, has mechanically bulky pre-soldered headers, and has no verified whole-board power data or enclosed safety assessment. The photograph alone does not verify operation or the project's runtime, diameter or mass criteria.
- **Next action / decision link:** If purchased, inspect and bench-test USB programming, one suitable sensor, an LED driver and power draw; compare fairly with [EV004](EV004-arduino-nano-rp2040-connect.md) under the same proposed conditions. Log results in [tests](../../tests/README.md) and only record any selection rationale in [decisions](../decisions.md) when supported.

## References

- [Raspberry Pi Ltd — Pico microcontroller boards (Pico WH variant, features and SWD connector)](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html), accessed 2026-11-08.
- [Raspberry Pi Ltd — Pico W datasheet (RP2040 wireless board; power, mechanical specification, pinout)](https://pip-assets.raspberrypi.com/categories/686-raspberry-pi-pico-w/documents/RP-008312-DS/pico-w-datasheet.pdf), accessed 2026-11-08. Pico W and Pico WH share their controller/wireless electronics; WH adds headers and keyed SWD interface.
- User-provided screenshot of a **second-hand Pico WH listing**, 2026-11-08 (photographic observation, not a bench test; image is not archived in the repository).
