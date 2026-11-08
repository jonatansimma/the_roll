# EV001 — Luxorparts Wemos D1 Mini (ESP8266EX controller)

- **Status:** Researching — desk assessment only; no bench tests or selection
- **Problem / requirement IDs:** [REQ001, REQ002, REQ003, REQ004, REQ005, REQ008](../requirements.md#functional-and-practical-requirements)
- **Author and date:** ChatGPT desk research, 2026-11-07
- **Related records:** [EV002 battery shield](EV002-luxorparts-battery-shield.md), [EV003 Li-Po cell](EV003-luxorparts-lipo-1200mah.md); [prototype rules](../../prototypes/README.md); [test records](../../tests/README.md); no build or test run exists

## Objective and operating principle

Evaluate whether Kjell & Company article **87294**, a D1 Mini development board based on the ESP8266EX, is a practical *main controller* for an off-dog retrieval-sensing and LED prototype. Firmware would read candidate switches/sensors, decide whether an intentional retrieval occurred, and drive an LED circuit. The board **does not itself detect mouth retrieval**; that requires separate sensors and evidence.

## Candidate components and sources

| Candidate / part | Key specification | Source / datasheet | Estimated cost / availability |
| --- | --- | --- | --- |
| Luxorparts Wemos D1 Mini, article 87294 | ESP8266EX; 3.3 V logic; 11 digital I/O (pin restrictions apply); 1 analog input, **3.2 V maximum at A0**; micro-USB; board 34.2 × 25.6 mm, 3 g; 80/160 MHz | [Product](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/utvecklingskort/luxorparts-wemos-d1-mini-utvecklingskort-p87294), [Luxorparts datasheet](https://www.kjell.com/globalassets/mediaassets/855793_87294_datasheet_en.pdf) | Indicative retailer listing ~140 SEK (observed in indexed listings, 2026-11-07); confirm live price/stock |

The retailer advertises **4 MB** flash, whereas the Luxorparts datasheet prints **“4 Mb”**; the discrepancy in units is unresolved for this particular board. For experimental Arduino-class firmware, use the actual board/toolchain report to confirm capacity. The developer documentation includes Arduino IDE and MicroPython support. These are board specifications, **not** measured values from the project.

## Expected advantages, limitations, and uncertainties

- **Expected advantages:** compact and light controller board; straightforward USB programming; ample basic digital interfaces for one or several candidate sensors and an LED driver; software-configurable thresholds and timing. Wi-Fi could support debugging, but is **not a stated Roll requirement**.
- **Constraints:** GPIO and peripherals operate at **3.3 V** (not 5 V tolerant). A0 must not receive more than the specified **3.2 V**. Some pins affect boot modes; avoid blindly attaching sensors or LED loads to bootstrap pins (GPIO0/GPIO2/GPIO15). D0/GPIO16 differs from general interrupt/PWM pins.
- **Power hypothesis:** Wi-Fi and development-board support circuitry may be costly for a small battery. Espressif's ESP8266EX sleep-current figures concern the **chip**, not this complete board or the proposed power shield; neither complete-system standby current nor prompt wake-on-retrieval is established. Deep sleep may require specific wake wiring and can interfere with immediate sensing.
- **Life-cycle note:** Espressif lists ESP8266EX as **not recommended for new designs**. That is a consideration for future redesign, not a technical disqualification for one available DIY prototype.
- **Unknowns:** actual board current in selected firmware modes; boot behavior with intended sensor pins; sufficient transient current when LEDs activate; enclosure clearances and thermal behavior.

## Integration implications

- The controller requires a regulated supply appropriate to the board (e.g., the board's **5V input** with its onboard regulator); **never connect an unregulated 3.7 V nominal Li-Po directly to 3V3 or ESP8266 supply pins**. [EV002](EV002-luxorparts-battery-shield.md) assesses a candidate 5 V supply.
- Use common ground and 3.3 V-compatible sensor interfaces; verify actual I²C, digital, or analog signal levels. Drive higher-current visible LEDs through suitably rated resistors and an external transistor/driver rather than assuming a GPIO can power the LED arrangement.
- Reserve accessible micro-USB during bench development; the port and board are not moisture-resistant or safe for animal contact without an appropriately assessed enclosure.
- If this board becomes a prototype's main controller, give that build a distinct **P###** ID. Replacing it with another main controller requires a **new** P### per [the prototype policy](../../prototypes/README.md); evaluating it does not create a prototype.

## Proposed evaluation experiments

All experiments are **proposals**, not executed work. Create and link reusable [test procedures](../../tests/README.md) and actual runs once performed.

1. **Boot and interface check:** power from a known, current-limited regulated source; flash a minimal program, exercise candidate 3.3 V digital and analog inputs and a safely current-limited LED/driver; verify pin behavior at boot.
2. **Detection-loop feasibility:** introduce a representative sensor or simulated switch, then compare successful events and incidental-contact events. Record event latency and any missed/false triggers; pass/fail thresholds must first be set in [requirements](../requirements.md).
3. **Power/LED current:** measure board input current when idle, sampling, driving LEDs, and optionally using Wi-Fi; record startup peaks and 5 V rail dips. Compare with the [shield evaluation](EV002-luxorparts-battery-shield.md) before estimating runtime.
4. **Size/handling check:** measure actual board-and-header footprint and fit against the as-yet-unmeasured Roll interior. All tests are off-dog; follow the [safety gate](../safety.md).

## Findings and evidence

| Finding | Classification | Evidence |
| --- | --- | --- |
| Board has 3.3 V logic, A0 rated to 3.2 V, and is 34.2 × 25.6 mm / 3 g | Published specification (not measured) | [Luxorparts datasheet](https://www.kjell.com/globalassets/mediaassets/855793_87294_datasheet_en.pdf) |
| Accessible Arduino-compatible development path and general sensor/LED firmware capability | Published specification / engineering inference | [Retailer](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/utvecklingskort/luxorparts-wemos-d1-mini-utvecklingskort-p87294), [Espressif](https://documentation.espressif.com/0a-esp8266ex_datasheet_en.html) |
| Full-board low-power operation and acceptable runtime | **Unknown** | No build, current measurement or test run |
| Retrieval detection, LED visibility and false-trigger performance | **Unknown** | No sensor/LED configuration or test run |
| “4 MB” vs “4 Mb” flash notation | **Unresolved documentation discrepancy** | Retailer description vs Luxorparts datasheet |

## Requirement-fit review — 2026-11-08 (desk assessment)

Reviewed against the [current requirements on `main`](../requirements.md), especially [body, attachment, and mass](../requirements.md#dimensional-and-mass-targets) and [battery operating time](../requirements.md#operating-time-requirements). This is a candidate assessment, **not compliance or hardware validation**.

- **Physical integration (REQ005):** The published 34.2 × 25.6 mm board footprint is smaller than the allowable cylinder's length and outer diameter; it is **plausible** for axial mounting. Clearance for the complete controller, connectors, battery, enclosure walls, LEDs, sensor and attachment is **unverified**. The board's published 3 g mass alone does not prove whole-assembly mass compliance.
- **Function (REQ001–REQ003):** GPIO and programmable logic can interface to a proposed retrieval sensor and a correctly rated LED driver. Deliberate-retrieval detection, false-trigger behavior and handler-visible indication are **unverified**.
- **Operating time (REQ004):** Neither the mandatory minimum nor preferred runtime is established: full-board active/idle/LED current and usable battery energy have not been measured. ESP8266 chip sleep figures cannot establish system-level runtime.
- **Safety/exposure (REQ006–REQ009):** Electrical, thermal, moisture, impact and animal-exposure checks are outstanding; see [safety gate](../safety.md).
- **Classification:** **Plausible controller candidate; does not yet demonstrate compliance.** Requires a complete packaging/power budget and off-dog tests.

## Conclusion and next action

- **Assessment:** **Promising for a first bench controller; requires more evidence** for battery-powered integrated use.
- **Reasoning:** Compact and easy to program, but its available I/O, power cost, and geometry have not been demonstrated with a chosen sensor/LED stack. No main controller is selected on `main`.
- **Next action / decision link:** Bench-test a minimal sensor-to-LED loop and log power/current. Record any subsequent hardware choice in [decisions](../decisions.md), backed by a [test run](../../tests/README.md).

## References

- [Kjell & Company, article 87294](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/utvecklingskort/luxorparts-wemos-d1-mini-utvecklingskort-p87294) (accessed 2026-11-07).
- [Luxorparts, D1 Mini datasheet, article 87294](https://www.kjell.com/globalassets/mediaassets/855793_87294_datasheet_en.pdf) (dated 2022-08-17; accessed 2026-11-07).
- [Espressif, ESP8266EX datasheet](https://documentation.espressif.com/0a-esp8266ex_datasheet_en.html) (accessed 2026-11-07; chip specifications are not measured board specifications).
