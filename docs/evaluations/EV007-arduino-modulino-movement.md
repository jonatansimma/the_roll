# EV007 — Arduino Modulino Movement (LSM6DSOXTR six-axis IMU)

- **Status:** Researching — datasheet and product-page review only; no bench measurement or selection
- **Problem / requirement IDs:** [REQ001–REQ003, REQ004–REQ006, REQ008–REQ009](../requirements.md#functional-and-practical-requirements); [dimensional and mass targets](../requirements.md#dimensional-and-mass-targets); [operating-time requirements](../requirements.md#operating-time-requirements)
- **Author and date:** ChatGPT research, 2026-11-20
- **Related records:** [EV001 Wemos D1 Mini](EV001-luxorparts-wemos-d1-mini.md), [EV004 Nano RP2040 Connect](EV004-arduino-nano-rp2040-connect.md), [EV005 Pico WH](EV005-raspberry-pi-pico-wh.md), [EV006 ESP32-C3 Super Mini](EV006-tenstar-robot-esp32-c3-super-mini.md), [test guidance](../../tests/README.md), [decision register](../decisions.md); no associated build or test run

## Objective and operating principle

Evaluate **Kjell & Company article 88456 / Arduino part ABX00101**, the **Modulino Movement**, as a candidate sensor for recognizing the Roll's intentional retrieval. It uses STMicroelectronics' **LSM6DSOXTR**, combining three-axis acceleration measurements with three-axis angular-rate measurements (six-axis inertial measurement unit, IMU). Its host controller could process time-series sensor data to detect a proposed retrieval-related pattern and command a separately driven LED output.

**Critical limitation:** This module measures movement, not mouth pressure, grip, saliva, or the dog's decision to retrieve. Running, turning, shaking, impacts and incidental handling can also create large signals. A detection algorithm and representative controlled trials must establish whether there is an adequately distinctive retrieval signature. No sensing approach is selected on `main`.

## Candidate components and sources

| Candidate / part | Key specification | Source / datasheet | Estimated cost / availability |
| --- | --- | --- | --- |
| **Arduino Modulino Movement ABX00101**, Kjell article **88456** | **LSM6DSOXTR**, 3-axis accelerometer + 3-axis gyro; **I²C over two Qwiic connectors**; **3.3 V nominal supply**; standard **7-bit I²C address 0x6A**, selectable **0x6B** by solder jumper; **41 × 25.36 mm** PCB, **1.6 ±0.2 mm** PCB thickness; **3.9 g** listed mass; four **Ø3.2 mm** mounting holes; solderable I²C pads and additional 1×10 pin field for sensor functions | [Kjell product](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/moduler/arduino-modulino-movement-6-axlig-rorelsesensor-p88456); [Arduino product](https://store.arduino.cc/products/modulino-movement); [Arduino official datasheet](https://docs.arduino.cc/resources/datasheets/ABX00101-datasheet.pdf); [schematics](https://docs.arduino.cc/resources/schematics/ABX00101-schematics.pdf) | Kjell product-category listing displayed **149 SEK promotional / 159 SEK regular** around 2026-11-20; price/stock may change. Retailer states one **50 mm Qwiic cable** included. |
| **LSM6DSOXTR sensor on the module** | Manufacturer/Arduino-published **sensor** examples: accelerometer high-performance **170 µA**; accelerometer low-power at 50 Hz **26 µA**, ultra-low-power at 50 Hz **9.5 µA**; gyro + accelerometer high-performance approximately **0.55 mA** as listed by Arduino. These are **sensor-mode figures**, not validated current consumption of the complete Modulino board. | [Arduino getting-started technical reference](https://docs.arduino.cc/tutorials/modulino-movement/how-movement/); [Arduino official datasheet](https://docs.arduino.cc/resources/datasheets/ABX00101-datasheet.pdf) | Already integrated on ABX00101; not independently priced. |

**Documentation ambiguity to verify:** Arduino's published address table lists **0x6A** as the default and **0x6B** as the alternative, but also prints **0x7E** in a separate “hardware I2C address” column without adequately explaining its role. The official schematic marks **0x6A default / 0x6B selectable**. For firmware planning, use the documented **0x6A** default and verify actual bus responses with a scanner; do **not** treat **0x7E** as a confirmed address or silently substitute it.

## Expected advantages, limitations, and uncertainties

### Expected advantages (not performance results)

- A **ready-to-wire, documented 6-axis sensor** with published schematics, mechanical drawing, pinout, software examples and official Modulino library, making it convenient for DIY **off-dog** comparisons of movement patterns.
- Both accelerometer and gyroscope data allow testing orientation changes, rotation, impact and temporal sequences rather than relying on a single acceleration magnitude.
- Qwiic connectors enable fast I²C experiments without soldering; separate solderable pads and **INT1/INT2** sensor interrupt signals are documented for more controlled wiring and low-power experiments.
- Manufacturer-published low-current **sensor modes** give possible power-optimization directions, **not** a claim that the assembled module or controller will use that little power.

### Limitations, risks, unknowns

- **Cannot independently recognize retrieval:** movement-only evidence may produce false positives during routine dog activity or a handler's handling, and false negatives for unusual retrievals. No training dataset, thresholds, performance metrics or field results exist.
- **Board size and connectors:** 41 × 25.36 mm board plus sockets/cables occupies substantially more volume than a bare LSM6DSOXTR chip or very small breakout. Actual installed depth, routing and enclosure fit are unknown.
- **Power LED overhead:** The official **ABX00101 schematic** shows a green LED and a **1 kΩ** series resistor permanently across the 3.3 V rail. Its current is not represented by the low-power **chip-only** figures, and might materially impact the Roll's 12-hour target. Exact complete-board current is unmeasured. Do not alter the LED or PCB until a separate documented hardware revision or safety review warrants it.
- **Interrupt routing:** Qwiic exposes **GND, 3V3, SDA, SCL**, not the sensor's **INT1/INT2** signals. An interrupt-driven wake-up experiment likely requires soldered wiring to the additional 1×10 pads and a controller input that can wake in the chosen sleep mode.
- **3.3 V supply only for normal board integration:** Qwiic connects 3.3 V directly to the sensor circuitry; do not connect a 5 V I²C bus or assume the module has a 5 V regulator/level shifter. Verify pull-ups and shared ground with the chosen microcontroller.
- **No weather/impact/animal qualification:** exposed connectors, solder pads and components need secure, sealed integration. Manufacturer conformity labels do not prove resistance to dog bite or saliva.
- **Software portability:** the Arduino Modulino library supports documented Arduino setups; verify its actual compatibility with the chosen Wemos D1 Mini, Pico WH or ESP32-C3 core. Direct LSM6DSOX-compatible I²C access is another **engineering option to test**, not an already validated combination.

## Integration implications

- **Sensor-to-controller interface (REQ001–REQ003):** Four I²C wires/pins (**3.3 V, GND, SDA, SCL**) plus a compatible microcontroller and appropriately driven LEDs are the simplest bench setup. The module is **not a microcontroller** and does not control the Roll LEDs on its own. For event-based wake trials, plan a separate **INT1** or **INT2** wire and test interrupt configuration, response time and reset behavior.
- **Existing controllers:** [Wemos D1 Mini](EV001-luxorparts-wemos-d1-mini.md), [Pico WH](EV005-raspberry-pi-pico-wh.md) and [ESP32-C3 Super Mini](EV006-tenstar-robot-esp32-c3-super-mini.md) are plausible 3.3 V I²C hosts if pinout, software, pull-ups and power are verified. [Arduino Nano RP2040 Connect](EV004-arduino-nano-rp2040-connect.md) **already has an LSM6DSOX-family IMU**, making this separate module largely **redundant for basic motion sensing** with that board (although a second independently mounted sensor could be useful for a different, expressly justified experiment). Arduino UNO R4 WiFi with Qwiic offers documented plug-and-play compatibility but is not selected as a Roll controller.
- **Physical compatibility (REQ005):** The module's published **25.36 mm board width** is less than the Roll's **35 mm nominal external cylinder diameter**, and **41 mm board length** is less than **120 mm**; axial mounting therefore appears geometrically *plausible*. This comparison does **not prove fit** inside the smaller interior diameter or leave room for USB/Qwiic cables, battery, sensor orientation, enclosure, LED optics, secure mounting and the **10 mm textile attachment-loop projection**. Measure the full assembly stack and use CAD/physical mockups.
- **Mass (REQ005):** **3.9 g module** occupies part of the **≤50 g total-target budget**. The controller, power system, LEDs, cable, enclosure and attachment must still be included; no full mass budget has been demonstrated.
- **Power/runtime (REQ004):** **1 hour minimum** is mandatory, **12 hours preferred**. Power-source, sampling, interrupt wake/sleep feasibility, idle sensor and status-LED currents, CPU activity and LED indication duty cycle must be **measured as a whole system**. Neither runtime is demonstrated.
- **Behavior/environment/safety (REQ006–REQ009):** Motion may be altered by PCB position, orientation and mounting stiffness; a loose module can register its own rattling rather than Roll motion. Secure mounting, insulation, moisture protection, retention and the [documented off-dog safety gate](../safety.md) are prerequisites to any animal exposure.

## Proposed evaluation experiments

**All the following are proposals.** Follow the [repository's test procedure and test run rules](../../tests/README.md); no device has been built, fitted or tested for this evaluation.

1. **Identity/fit/bench inspection:** Confirm ABX00101 and actual board revision, 3.3 V rail, cable routing, connector height, board mass and mounting-hole spacing. Create a nonpowered axial packing mockup including the desired controller, battery, LEDs and textile attachment.
2. **Simple bring-up (off-dog):** Use a known regulated **3.3 V** source and supported I²C host; scan for **0x6A** (or documented **0x6B** if jumper modified); record any conflicting or extra responses without assuming the unexplained **0x7E** address is correct. Read acceleration and angular-rate data, check direction/calibration and wiring stability.
3. **Comparable movement trials:** Log timestamped six-axis traces at controlled sample rates and consistent mounting orientation for simulated deliberate pickup/retrieval sequences versus ordinary movement, impacts, inversion, handling, shaking and wet-enclosure effects. Define quantitative sensitivity, latency and false-alarm criteria **before** claiming success.
4. **Wake-on-motion strategy:** Test with/without gyro, lower-rate accelerometer operation and, if practical, INT1/INT2 wiring; determine whether the chosen controller can wake on an appropriate event without missing a real retrieval. Measure detection timing under the proposed power modes.
5. **Current and battery tests:** Measure **complete-module current at 3.3 V** across sensing modes and any power-LED contribution; then measure **controller + module + LED driver** under representative duty cycle. Document battery energy assumptions, actual usable energy, thermal state and achieved operation time versus the canonical hard and preferred targets.
6. **Integrated retest and safety gate:** Recheck performance after mounting and sealing, including mechanical shock, connector retention, moisture, accessibility of sharp parts, battery containment and false activations. Do **not** expose a dog to unfinished electronics; follow [safety.md](../safety.md) and record any clearance.

## Findings and evidence

| Finding | Classification | Evidence |
| --- | --- | --- |
| Official **ABX00101**, LSM6DSOXTR, 3.3 V Qwiic, **41 × 25.36 mm**, **3.9 g** | **Published specification; not measured by project** | [Arduino product](https://store.arduino.cc/products/modulino-movement); [Arduino official datasheet](https://docs.arduino.cc/resources/datasheets/ABX00101-datasheet.pdf); [Kjell product](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/moduler/arduino-modulino-movement-6-axlig-rorelsesensor-p88456) |
| Default 7-bit I²C **0x6A**, selectable **0x6B**; datasheet additionally prints **0x7E** in separate address column | **Published with unresolved documentation ambiguity** | [Arduino official datasheet, I²C table](https://docs.arduino.cc/resources/datasheets/ABX00101-datasheet.pdf); [official schematic](https://docs.arduino.cc/resources/schematics/ABX00101-schematics.pdf) |
| Power-status LED and 1 kΩ resistor connected to 3.3 V | **Published schematic observation; board consumption unknown** | [Arduino official schematics](https://docs.arduino.cc/resources/schematics/ABX00101-schematics.pdf) |
| Low-power accelerometer modes may reduce **sensor-only** current | **Published chip/sensor-mode rating; not a board-level result** | [Arduino tutorial](https://docs.arduino.cc/tutorials/modulino-movement/how-movement/) |
| Dimensions are plausible for axial mounting inside Roll; total enclosure/connector fit and mass unknown | **Engineering inference / unknown** | [Mechanical specification](https://docs.arduino.cc/resources/datasheets/ABX00101-datasheet.pdf), [canonical requirements](../requirements.md#dimensional-and-mass-targets) |
| Retrieval detection accuracy, false positives, minimum 1 h runtime, preferred 12 h runtime, environmental tolerance and dog-use safety | **Unknown / untested** | No prototype and no test runs |

## Conclusion and next action

- **Assessment:** **Promising as an off-dog six-axis sensing evaluation module; requires further evidence before selection.**
- **Reasoning:** Identified brand/model, documented I²C interface, readily available cables and firmware examples make it practical for repeatable motion-sensing experiments. Its board is physically plausible but relatively large for a compact enclosure; the fixed power LED complicates low-power estimates; and **motion does not prove retrieval**. It offers less added value with [EV004](EV004-arduino-nano-rp2040-connect.md), which already carries an LSM6DSOX-family IMU.
- **Next action / decision link:** Prefer a fast **USB-powered/off-dog motion-versus-normal-movement test**, recording six-axis traces with one non-IMU host; independently measure module power, then assess a smaller external IMU breakout if the integrated package is too large or inefficient. Treat a method decision as **proposed** until supported by actual [test evidence](../../tests/README.md) and recorded in [decisions](../decisions.md).

## References

- [Kjell & Company article 88456, Modulino Movement](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/moduler/arduino-modulino-movement-6-axlig-rorelsesensor-p88456), consulted 2026-11-20.
- [Arduino Official Store, Modulino Movement SKU ABX00101](https://store.arduino.cc/products/modulino-movement), consulted 2026-11-20.
- [Arduino ABX00101 datasheet, official mechanical and pinout documentation](https://docs.arduino.cc/resources/datasheets/ABX00101-datasheet.pdf), consulted 2026-11-20.
- [Arduino ABX00101 official schematic](https://docs.arduino.cc/resources/schematics/ABX00101-schematics.pdf), consulted 2026-11-20.
- [Arduino getting started with Modulino Movement](https://docs.arduino.cc/tutorials/modulino-movement/how-movement/), consulted 2026-11-20.
