# EV010 — Adafruit 1374 AT42QT1010 capacitive touch breakout

- **Status:** Researching — desk evaluation only; **not purchased, wired, measured, tested, selected, or approved for dog exposure**
- **Problem / requirement IDs:** [REQ001–REQ003, REQ004–REQ006, REQ008–REQ009](../requirements.md#functional-and-practical-requirements)
- **Author and date:** ChatGPT research, 2026-11-22
- **Related evaluations:** [EV005 Pico WH](EV005-raspberry-pi-pico-wh.md), [EV008 light-grip approaches](EV008-light-grip-retrieval-sensing.md), [EV009 LIS3DH](EV009-electrokit-ekm029-lis3dh.md)
- **Test evidence:** No tests or validated sensor choice. Follow [tests](../../tests/README.md).

## Objective and operating principle

Evaluate whether **Microchip AT42QT1010 capacitive contact/proximity sensing**, provided on the **Adafruit product 1374 breakout**, can register retrieval of the Roll despite a **reported very gentle bite and occasional drop/re-pickup** (owner observation documented as a consideration on unmerged `agent_main`, not an accepted force requirement). A capacitive electrode changes the chip's sensed capacitance when a conductive body approaches; therefore substantial force or a moving mechanical actuator is **not required in principle**. However, an output event is **not specific to a dog's mouth**, and fur, water, moisture, grounding and enclosure geometry may cause misses or false detections.

## Candidate components and sources

| Candidate | Published specification / observation | Source | Sweden price / availability checked 2026-11-22 |
| --- | --- | --- | --- |
| **Adafruit Standalone Momentary Capacitive Touch Breakout**, Adafruit **1374**, Electrokit article **4101 5256** | **20 × 28 mm**, published board mass **1.87 g**; supply **1.8–5.5 V DC**; 3-wire **VCC, GND, OUT**, **active-high** digital touch signal; onboard capacitive electrode and contact-status LED; pad for **optional external electrode**; header provided; momentary output not a latch | [Electrokit product](https://www.electrokit.com/en/kapacitiv-touchknapp-momentan), [Adafruit 1374 product](https://www.adafruit.com/product/1374) | **79 SEK incl. VAT**, displayed in stock at review; supplier information may change |
| **AT42QT1010 IC**, Microchip | Operating Vdd **1.8–5.5 V**; fast and low-power modes; **active-high OUT**; chip automatically recalibrates after **Max On-duration** (about **60 s at 3 V in LP mode**, varies with voltage, capacitor sizing and sync); output then goes low until a new touch detection | [Microchip AT42QT1010 datasheet](https://www.microchip.com/content/dam/mchp/documents/OTH/ProductDocuments/DataSheets/40001946A.pdf), [Microchip product](https://www.microchip.com/en-us/product/AT42QT1010) | Chip datasheet performance figures; not measured on Adafruit board |

**Electrical power detail:** Adafruit publishes breakout consumption **approximately 0.5 mA in default fast mode** and **approximately 50 µA after a physical jumper modification for low-power mode**. This is Adafruit's breakout description, **not** a measured current for a specific board under active LED indication, nor a claim about the Pico/LED whole system. The breakout's indicator LED can be disconnected via a separate trace modification for power-saving experiments. Neither modification is recommended as a prerequisite to an initial bench functional test.

## Expected advantages, limitations, and uncertainties

### Expected benefits / untested hypotheses

- A touch signal may be obtained through an **electrically insulating enclosure wall** with an internal pad or remote conductor; no substantial grip compression should be required, potentially attractive for very light bites.
- No I²C bus, ADC or complex motion classifier needed to read the board's one digital output on a 3.3 V Pico WH GPIO.
- An electrode can potentially be shaped to cover a useful mouth-grip region; empirical sensitivity mapping is required because geometry and wiring alter capacitance and noise.
- The single-board momentary output is convenient for measuring onset, release and repeated simulated retrievals; optional later comparison with [EV009](EV009-electrokit-ekm029-lis3dh.md) could help distinguish contact from movement.

### Key limitations, caveats and uncertainties

- **Cannot identify dog-mouth contact as such.** A hand, wet ground, collar, moisture/saliva or nearby objects may change capacitance; different grip positions and fur/insulation may reduce it. Whether wet sensor performance is acceptable is unknown.
- **Max On-duration timeout is significant:** Microchip quotes about **60 seconds only at 3 V in LP mode**. The effective continuous-detection time **depends on mode/voltage/synchronization**, and the sensor can reset its reference and **drop OUT despite ongoing contact**. Do not hard-code or rely on a universal 60-second threshold, and do not assume a sustained contact output is available indefinitely. The [AT42QT1011](https://www.microchip.com/en-us/product/AT42QT1011) is a related alternative **without that Max On timeout**, but requires a different board evaluation if selected.
- **Low-power jumper modification affects response time**; the switch between LP and fast during detection is device-dependent. Characterize event latency and short contacts; no bite duration is known.
- The board's built-in **20 × 28 mm exposed PCB** is not itself a chew-resistant sensor face. Remote copper foil / electrode behind sealed insulation changes parasitic capacitance and may behave differently from the onboard pad; must be empirically optimized.
- Fixed internal touch threshold plus calibration/drift compensation may not suit all moisture conditions. Pin/signal reliability under handling is unknown.
- Board footprint plus headers, wires, electrode, shielding, battery and enclosure must fit the [physical and mass targets](../requirements.md#dimensional-and-mass-targets). Published board mass is not an integrated mass budget.

## Integration implications

- **Pico WH with three AAA cells:** Three ordinary **alkaline AAA cells in series are nominally 4.5 V**, or **three NiMH rechargeable AAA nominally 3.6 V**. The [Pico WH VSYS](EV005-raspberry-pi-pico-wh.md) can accept approximately **1.8–5.5 V**. For common-safe logic levels, battery -> **VSYS/GND**, breakout **VCC -> Pico 3V3(OUT)**, GND -> shared GND, **OUT -> one 3.3 V GPIO input**, with USB disconnected for simple battery-only bench testing. **Do not use battery voltage on Pico GPIO**; although this breakout itself tolerates up to 5.5 V, its OUT would then be unsafe for 3.3 V-only GPIO. No direct supply from a series pack of three **3.7 V 10440 lithium-ion cells**.
- **Signal:** Output **HIGH on capacitance detection**, LOW normally, and returns LOW after release or a max-on recalibration. Firmware should log leading/trailing edges, including interrupted pickup sequences; input filtering and LED hold/reset policy remain to be specified in [requirements](../requirements.md). Touch/release is not equal to verified dog retrieval.
- **Power:** The sensor's published **0.5 mA fast** is small compared with possible Pico/LED consumption, but low-power changes and 1 h/12 h [endurance targets](../requirements.md#operating-time-requirements) require **actual whole-system measurement**. The onboard status LED may materially change current when triggered; measure both states.
- **Capacitive geometry:** Start with the built-in pad **off-dog** and a known dielectric. Then test one safely isolated remote electrode at a time and map responses across intended grip positions. Do not use a conductive electrode exposed where it can be bitten.
- **Safety:** Breadboards, unsealed foil and sensors are test equipment only; apply [safety review and dog-exposure gate](../safety.md) before considering a fully enclosed assembly on an animal.

## Proposed evaluation experiments (none performed)

1. Verify exact breakout identity, PCB revision, 3.3 V operation, GPIO HIGH/LOW logic, startup behavior, status LED and current at idle and active output. Record measured board mass and installed depth.
2. Simulate very light touches and short contact/release/re-contact periods through a fixed plastic layer. Map contact position, distance and whether contact is missed under repeated identical conditions. Record true/false detections and latency, without claiming human touches simulate animal mouths perfectly.
3. Compare dry dielectric, slightly damp surface, localized artificial wetting, handling, touches near the attachment, impacts, and leaving damp material on the outside of an **off-dog insulated fixture**. Keep water away from exposed electronics; log false activation and recovery.
4. Hold a controlled, stable conductive contact continuously for longer than the documented approximate max-on duration, in **fast and (if later modified) low-power modes**, recording time to spontaneous output drop, recalibration and re-activation after release. This is a major discriminator for choosing 1010 vs 1011.
5. Compare onboard electrode against an insulated remote electrode of documented area, routing length and position. Repeat false-trigger tests around batteries, mounting hardware and a dummy enclosure.
6. With battery-fed Pico WH and LED driver, log **total input current** at idle and simulated retrieval, and test endurance and response. Optionally compare synchronized motion data from [EV009](EV009-electrokit-ekm029-lis3dh.md).
7. Write test records under [tests](../../tests/README.md); obtain quantitative acceptance thresholds from [requirements](../requirements.md) before asserting compliance.

## Findings and evidence

| Finding | Classification | Evidence |
| --- | --- | --- |
| Adafruit 1374 / Electrokit 4101 5256 is a 20 × 28 mm momentary AT42QT1010 breakout, 1.8–5.5 V, with onboard touch pad and active-high OUT | Published product specification | Adafruit/Electrokit |
| Adafruit lists 1.87 g breakout mass and approximately 0.5 mA default fast-mode operation / 50 µA low-power modified | Published vendor values, **not measured on the delivered hardware** | Adafruit product page |
| Max On-duration is about 60 s **at 3 V in LP mode**, but not invariant under other operation | Manufacturer specification and integration interpretation | Microchip AT42QT1010 datasheet, §3.3 and §3.9 |
| Regulated Pico WH 3.3 V logic and sensor output are electrically compatible when powered from the same 3.3 V rail | Engineering compatibility assessment | Pico WH evaluation + breakout specifications |
| Ability to recognize gentle-bite pickup, prevent wet false triggers, retain output on continuous contact, meet runtime or integrated geometry/safety | **Unknown / untested** | No bench tests or assembly |

## Conclusion and next action

- **Assessment:** **Promising first off-dog contact-sensing experiment; suitability as final Roll detector unverified.**
- **Reasoning:** Capacitive sensing does not inherently need a strong bite and the 3.3 V GPIO interface is simple. **False activations from moisture/contact and the built-in max-on timeout** are major risks which could outweigh the advantage.
- **Next action / decision link:** Begin with a controlled insulated electrode experiment and continuous-hold timeout characterization, record outcomes in [tests](../../tests/README.md), and consider [AT42QT1011](https://www.microchip.com/en-us/product/AT42QT1011) or [EV009](EV009-electrokit-ekm029-lis3dh.md) only if observed failure modes justify it. Document a later selection in [decisions](../decisions.md). **No hardware choice or project requirement is established by this evaluation.**

## References

- [Electrokit Sweden, Adafruit 1374 momentary capacitive touch (article 4101 5256)](https://www.electrokit.com/en/kapacitiv-touchknapp-momentan), reviewed 2026-11-22.
- [Adafruit 1374 product page — pin logic, power, electrode, optional jumper and physical details](https://www.adafruit.com/product/1374), reviewed 2026-11-22.
- [Microchip AT42QT1010 datasheet DS40001946A — supply, current, max-on duration and output](https://www.microchip.com/content/dam/mchp/documents/OTH/ProductDocuments/DataSheets/40001946A.pdf), reviewed 2026-11-22.
- [Microchip AT42QT1011 product — no Max On timeout alternative](https://www.microchip.com/en-us/product/AT42QT1011), reviewed 2026-11-22.
- [Raspberry Pi Pico WH controller evaluation — EV005](EV005-raspberry-pi-pico-wh.md).
