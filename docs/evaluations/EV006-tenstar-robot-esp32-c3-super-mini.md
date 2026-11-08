# EV006 — TENSTAR ROBOT-marked ESP32-C3 Super Mini

- **Status:** Researching — pictured board family identified; documentation-based assessment only, no hardware testing
- **Problem / requirement IDs:** [REQ001–REQ005, REQ008–REQ009](../requirements.md#functional-and-practical-requirements), notably the [physical and mass constraints](../requirements.md#dimensional-and-mass-targets) and [runtime requirements](../requirements.md#operating-time-requirements)
- **Author and date:** ChatGPT desk research with user-provided second-hand listing screenshots, 2026-11-08
- **Related records:** [EV001 D1 Mini](EV001-luxorparts-wemos-d1-mini.md), [EV004 Arduino Nano RP2040 Connect](EV004-arduino-nano-rp2040-connect.md), [EV005 Raspberry Pi Pico WH](EV005-raspberry-pi-pico-wh.md); [test records](../../tests/README.md), [decisions](../decisions.md); no prototype or test run for this board

> **Identification and scope:** The second-hand photographs show two small black PCBs with 16 castellated/header pads (eight per edge), USB-C, two buttons labeled **BOOT** and **RST**, a red ceramic antenna marked **C3**, and a visible Espressif-branded IC. In the second photo, the back-side marking visible through a bag reads **“TENSTAR / ROBOT / ESP32-C3 / Super Mini”**. This identifies the **advertised board family and pictured layout** with high confidence. “TENSTAR ROBOT” is a board marking; whether the company manufactured, designed or merely sold the hardware is not verified. The two photographed loose boards and the bagged board appear to be the same family but individual units have not been inspected. PCB revision, exact regulator IC, fitted flash capacity, authenticity, electrical condition and operating history are **not established**. **This evaluation is for the pictured standard-layout, non-OLED, non-Plus variant only**; do not transfer its pinout or power assumptions to other boards sold as “Super Mini”.

## Objective and operating principle

Assess this compact **ESP32-C3-based controller** for the Roll's off-dog retrieval-sensor and LED prototype. Firmware would interpret an **external** pressure, switch, capacitive or motion-sensing device and control an LED driver. This board **does not itself include an accelerometer/gyroscope or detect mouth retrieval**. ESP32-C3 is a single-core RISC-V microcontroller with wireless features; Wi-Fi and Bluetooth are **not necessary** for the present basic sensor-to-LED function.

## Candidate components and sources

| Candidate / part | Key specification | Source / datasheet | Estimated cost / availability |
| --- | --- | --- | --- |
| **TENSTAR ROBOT-marked ESP32-C3 Super Mini, standard 16-pad USB-C layout, pictured with uninstalled pin headers** | **Observed:** USB-C, BOOT/RST, ceramic antenna, two 8-pad rows and an ESP32-C3 designation on the reverse. **Typical published board layout:** about **22.5 × 18 mm PCB** (about **24 × 18 mm** including USB-C protrusion), 13 GPIO signals on the 16 edge pads plus 5V/GND/3V3; **fitted mass, populated height and power regulator unknown**. | User-provided listing screenshots (2026-11-08, **not archived in repository**); [Tenstar-labeled variant description and photos](https://nuttx.apache.org/docs/latest/platforms/risc-v/esp32c3/boards/esp32c3-supermini/index.html); [independent board measurements](https://sigmdel.ca/michel/ha/esp8266/super_mini_esp32c3_en.html) | Listing screenshot shows **100 SEK buy-now** and shipping from **22 SEK**. Two loose boards are pictured; exact transaction quantity, condition and total cost require seller confirmation. |
| **ESP32-C3 system-on-chip** (fitted to the pictured board family) | **Published chip-level:** 32-bit RISC-V, up to **160 MHz**, **400 kB SRAM**, Wi-Fi 2.4 GHz, Bluetooth **LE 5**, native USB Serial/JTAG, configurable digital peripherals and ADC. **5 µA deep-sleep** is a **chip figure only**, not a measurement or promise for the complete PCB. Typical Super Mini flash is often **4 MB**, but the pictured unit's flash size is **not verified**. | [Espressif ESP32-C3 Series datasheet](https://documentation.espressif.com/esp32-c3_datasheet_en.html); [NuttX Tenstar board notes](https://nuttx.apache.org/docs/latest/platforms/risc-v/esp32c3/boards/esp32c3-supermini/index.html) | Chip features are not evidence of second-hand board functionality. |

## Expected advantages, limitations, and uncertainties

- **Advantages (engineering hypotheses):** very small layout and exposed GPIOs could simplify space-constrained prototyping; USB-C with native serial/JTAG allows convenient firmware bring-up; Arduino-ESP32 and Espressif tooling support an accessible development workflow; a simple contact sensor and LED driver need only a few pins.
- **Power potential, not yet established:** ESP32-C3 offers configurable sleep modes, and wireless functions can be left unused. The complete Super Mini's actual idle and deep-sleep input current depends on regulator quiescent current, power LED, firmware, sensor, LED driver and wake circuit. **Do not use the ESP32-C3 chip's 5 µA deep-sleep figure for a system-runtime prediction.**
- **Limited board-specific traceability:** variants sold under the same commercial name may use different regulators, LEDs, antenna layouts and flash parts. No independently verified schematic or bill of materials establishes **this pictured unit's** regulator model, quiescent current, reverse-polarity protection or power-path isolation.
- **Pin conflicts:** ESP32-C3 uses **GPIO2, GPIO8 and GPIO9 as strapping pins**; typical Super Mini connects its user LED to **GPIO8** (active-low) and BOOT to **GPIO9**. Loads that pull them into the wrong state during reset may prevent boot. Native USB is on **GPIO18/19**, not exposed as independent GPIOs on the standard edge rows. Prefer uncontroversial GPIOs for the first external switch and LED-driver experiments.
- **Analog caution:** ADC1 GPIO0–GPIO4 are the straightforward analog candidates when supported by the board's pinout; Espressif documents restrictions/errata affecting ADC2 on GPIO5. Never exceed **3.3 V** on I/O.
- **No on-board IMU or lithium charger:** motion sensing requires an additional device. Charging, protection, battery undervoltage handling and reliable supply switching require independent circuitry.
- **Wireless caution:** the ceramic antenna's range and performance are not guaranteed on a board of this format, and an enclosing cylinder could affect RF operation. Wireless is optional for the current Roll goal.

## Integration implications

- **Mechanical (REQ005):** The *typical* **22.5 × 18 mm** PCB is a promising candidate for an axial arrangement inside the [specified circular body envelope](../requirements.md#dimensional-and-mass-targets); **this is not a demonstrated 3D fit**. Measure actual board dimensions, header thickness and USB protrusion, then allow for enclosure wall thickness, sensor, battery, LED optics, wiring, secure retention and the existing attachment loop. Headers pictured are **loose**, not soldered; for the enclosed version a secure low-profile connection may be preferable. No board mass or complete assembly mass has been measured against the [target](../requirements.md#dimensional-and-mass-targets).
- **Power (REQ004):** Standard boards take **5 V at USB/5V input** and regulate to **3.3 V**; the photograph does not prove the specific regulator's dropout/current rating, safe input range or protection. **Do not connect a raw 3.7 V nominal Li-Po directly to the 3V3 rail** (4.2 V when charged can damage the chip), or assume the 5V header works correctly throughout the battery's discharge range. Use an appropriately regulated, protected supply with a verified charging arrangement. If a separate supply is connected to the 5V header, **do not simultaneously connect USB** until back-feed and power-path isolation are confirmed.
- **Runtime:** The [mandatory minimum and preferred operating-time requirements](../requirements.md#operating-time-requirements) cannot be evaluated without a battery choice, actual board/sensor/LED current and an event duty cycle. Deep sleep could impair wake-on-retrieval, depending on the external sensor and chosen wake-capable pin.
- **Detection/LED (REQ001–REQ003):** Use suitable 3.3 V logic for sensors, keep boot pins free from problematic loads, and drive handler-visible LEDs using appropriate current-limiting and an external transistor/driver if needed. The onboard status LED is a programming indicator, **not proof of handler-visible signaling**.
- **Environmental and dog safety (REQ006–REQ009):** Exposed USB, antenna, components and terminals need an enclosed, mechanically retained, electrically protected configuration. No dog exposure until [safety assessment and required inspection](../safety.md) are completed.

### Reference pinout — verify physically before wiring

For the **standard** layout with USB-C at the top and the antenna at the bottom, published board pinouts show two eight-pad rows:
- **5V-side row (USB end toward antenna):** 5V, GND, 3V3, GPIO4, GPIO3, GPIO2, GPIO1, GPIO0.
- **Other row (USB end toward antenna):** GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10, GPIO20, GPIO21.

This pin arrangement is consistent with the visible edge labeling but has **not been confirmed by continuity testing on these actual boards**. GPIO8/9 require boot/LED/button consideration; use alternative pins for I²C rather than assuming the commonly published GPIO8/GPIO9 defaults are safe for external pull resistors.

## Proposed evaluation experiments

**None of these experiments has been conducted.** Record procedures and results using [the project testing system](../../tests/README.md), with the exact board and firmware commit.

1. **Board identity/inspection:** verify the actual received PCB(s) match the photos on both faces; examine IC/regulator markings, solder quality, header pads, any damage; measure PCB/USB/header envelope and mass. Record whether the listing contained one or two units.
2. **USB bring-up:** power off-dog from a known-good current-limited USB source, confirm serial enumeration and bootloader access; upload a minimal program, exercise user LED and one separate GPIO through a safe test load. Confirm installed flash size and pin definitions from the board itself.
3. **Sensor-to-LED proof:** connect a simple 3.3 V-compatible switch/sensor on a non-strapping input and an appropriately limited LED driver; record response timing, resets and false triggers under simulated handling, not on the dog.
4. **Full-board power characterization:** measure USB input current in boot, idle sensing, radio-disabled active mode, possible sleep states, wake-on-switch and LED events. Observe startup peaks and regulator/LED effects; determine whether sensing during sleep is feasible.
5. **Battery protection and duration:** use only a separately verified regulator, protected battery and charger; check input voltage/ripple, USB back-feed protection and sustained voltage under load. Measure usable duration against the [required operating profile](../requirements.md#operating-time-requirements), not a chip-only datasheet estimate.
6. **Packing and electrical safety:** prepare a layout and mass budget for all installed components, then verify enclosure, strain relief, water resistance, bite/impact retention and heat off-dog before consideration of the [animal-exposure gate](../safety.md).

## Findings and evidence

| Finding | Classification | Evidence |
| --- | --- | --- |
| Two photographed black boards show USB-C, BOOT/RST, C3-marked ceramic antenna and 16 edge pads; reverse of one pictured unit reads **TENSTAR ROBOT / ESP32-C3 / Super Mini** | **Observed in user-provided listing images; not inspected or tested** | User screenshots, 2026-11-08 (images not archived in repository) |
| Standard Super Mini dimensions approximately **22.5 × 18 mm** and pin assignment of 13 GPIO signals | **Published third-party measurements and documentation; unit not measured** | [Independent review](https://sigmdel.ca/michel/ha/esp8266/super_mini_esp32c3_en.html); [Apache NuttX board description](https://nuttx.apache.org/docs/latest/platforms/risc-v/esp32c3/boards/esp32c3-supermini/index.html) |
| ESP32-C3 supports 160 MHz RISC-V, 400 kB SRAM, 3.3 V logic, Wi-Fi and BLE | **Manufacturer chip specification, not board measurement** | [Espressif datasheet](https://documentation.espressif.com/esp32-c3_datasheet_en.html) |
| Chip deep sleep about 5 µA; complete board sleep/runtime | **Published chip figure; board figure UNKNOWN** | [Espressif datasheet](https://documentation.espressif.com/esp32-c3_datasheet_en.html); no test runs |
| Populated mass, 3D integration, onboard regulator/charger/protection details, installed flash, functional condition and actual operational duration | **Unknown** | No hands-on inspection, configuration or test run |
| Eligibility for the Roll's normal dimensional constraints | **Promising geometry hypothesis, not a demonstrated complete assembly fit** | Published PCB dimensions compared qualitatively with [current requirements](../requirements.md#dimensional-and-mass-targets) |

## Conclusion and next action

- **Assessment:** **Promising controller candidate; requires more evidence**. Eligible for **off-dog bench investigation**, **not proven to meet complete prototype requirements**.
- **Reasoning:** The photos meaningfully resolve the earlier generic-name ambiguity to a TENSTAR ROBOT-marked *standard-format* board. Its compact PCB is an attractive possible fit; the external sensor, protected battery, real current, integrated assembly mass and mechanical/animal safety remain unknown. Its lack of an IMU is a disadvantage compared with [EV004](EV004-arduino-nano-rp2040-connect.md) if motion sensing is tested.
- **Next action / decision link:** Inspect a received board, verify its regulator and electrical interfaces, and perform basic USB + sensor-to-LED + power tests. Record actual test evidence and any selection in the appropriate [test](../../tests/README.md) and [decision](../decisions.md) records; do not declare a prototype or selected controller from a paper evaluation.

## References

- [Espressif — ESP32-C3 Series datasheet](https://documentation.espressif.com/esp32-c3_datasheet_en.html) (consulted 2026-11-08; chip data).
- [Apache NuttX — Tenstar Robot ESP32-C3 SuperMini board support and pinout](https://nuttx.apache.org/docs/latest/platforms/risc-v/esp32c3/boards/esp32c3-supermini/index.html) (consulted 2026-11-08; not proof of exact PCB revision).
- [Michel Sigmondel — First Look at the Super Mini ESP32-C3](https://sigmdel.ca/michel/ha/esp8266/super_mini_esp32c3_en.html) (updated 2026-04; consulted 2026-11-08; independent account of Tenstar-marked examples, power limitations and variation).
- User-provided second-hand listing screenshots, 2026-11-08 (unarchived evidence; photograph is not a bench measurement).
