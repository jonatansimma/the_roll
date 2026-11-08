# EV003 — Luxorparts 3.7 V 1200 mAh Li-Po battery

- **Status:** Researching — desk assessment only; no capacity, fit, or safety validation
- **Problem / requirement IDs:** [REQ004, REQ005, REQ006, REQ008, REQ009](../requirements.md#functional-and-practical-requirements)
- **Author and date:** ChatGPT desk research, 2026-11-07
- **Related records:** [EV001 D1 Mini](EV001-luxorparts-wemos-d1-mini.md), [EV002 battery shield](EV002-luxorparts-battery-shield.md), [safety review](../safety.md), [test records](../../tests/README.md); no build or test run exists

## Objective and operating principle

Evaluate Kjell & Company article **87924**, a **single-cell flat-pouch lithium-polymer battery**, as the energy store for off-dog controller/sensor/LED tests and potentially an integrated Roll. A rechargeable Li-Po battery supplies a varying cell voltage; it does **not** directly provide regulated 3.3 V or 5 V rails or a safe charging system.

## Candidate components and sources

| Candidate / part | Key specification | Source / datasheet | Estimated cost / availability |
| --- | --- | --- | --- |
| Luxorparts Li-Po battery, article 87924 | **3.7 V nominal**, **1200 mAh** (1.2 Ah), **4.2 V charge voltage**; max charge **1 C = 1.2 A**, max discharge **1 C = 1.2 A**; listed undervoltage shutoff **2.4 V**; **JST-PH 2.0 mm** connector; **63 × 36 × 4.7 mm**, **23.3 g** | [Kjell & Company specification](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/arduino-tillbehor/luxorparts-li-po-batteri-37-v-med-kontakt-1200-mah-p87924) | Indicative listing ~80 SEK in indexed November 2026 listings; confirm live price/stock |

The seller gives charging temperature **10–45 °C** and discharging temperature **−20–60 °C**. These are *published limits*, not safe-temperature results measured in the Roll. No independent cell datasheet or cycle-life curve was located for this exact article; inspect the actual pack label and protection circuit before relying on further characteristics.

## Expected advantages, limitations, and uncertainties

- **Expected advantages:** rechargeable, compact in thickness, with a nominal energy content adequate to justify initial run-time experiments. The JST lead avoids direct soldering to a cell.
- **Geometry concern:** this is a **wide, flat 36 mm** pouch, not a cylindrical cell. Its shape may be inconvenient for a narrow Roll and it must not be bent, crushed, punctured or compressed to fit. Internal Roll dimensions are currently **TBD** in [requirements](../requirements.md); do not assume fit.
- **Protection concern:** the product page states a **2.4 V undervoltage shutoff**, but the exact physical protection implementation and full overcharge/short-circuit protection are **not verified**. Do not design around deep discharge to 2.4 V without confirming the cell and system requirements. Avoid exposed terminals and uncontrolled high currents.
- **Compatibility concern:** the listed **JST-PH 2.0 mm** plug may not match the **shield described in [EV002](EV002-luxorparts-battery-shield.md)** because that shield's product listing and datasheet conflict. Physical mating and pin polarity must be checked before any live connection.
- **Animal safety:** a soft Li-Po pouch is particularly vulnerable to bite/impact puncture, swelling, heat and moisture. This battery is **not appropriate for dog exposure** without verified protective enclosure, electrical checks and the documented [safety gate](../safety.md).

## Integration implications

- **Energy estimate (not measured):** nominal capacity × nominal voltage = **1.2 Ah × 3.7 V = 4.44 Wh ≈ 16.0 kJ**. This is *nominal*, not usable output energy; temperature, discharge rate, converter losses and voltage cutoff reduce delivered energy.
- **Illustrative runtime only:** for a hypothetical **5 V × 0.10 A = 0.50 W** continuous *system* load and assumed **80%** overall conversion efficiency, **4.44 Wh × 0.80 / 0.50 W ≈ 7.1 h**. Neither the 0.10 A load nor 80% efficiency has been measured; this is **not a battery-life prediction** or project acceptance target. Actual sleep and LED duty cycle must be measured.
- Use a charger configured for this single-cell chemistry and **4.2 V** maximum cell charge voltage, with appropriate protection. The [shield evaluation](EV002-luxorparts-battery-shield.md) covers candidate charger settings and its unresolved risks; never connect the battery to an unverified shield connector.
- The specified **1.2 A maximum discharge** is a battery limit, not a recommended normal operating current. Compare peak controller + sensors + LED demand, boost input current, fuse behavior and cell/wire temperature against measured data.
- Reserve physical containment, strain relief, padding that does not compress the pouch, inspection access and a way to isolate/remove power. All handling and electronics tests remain off-dog until cleared.

## Proposed evaluation experiments

These are **proposals**, not completed tests; use [documented procedures and runs](../../tests/README.md).

1. **Unpowered identification:** record the pack dimensions and mass, inspect swelling/damage and label/protection markings, and check JST plug pitch, keyed direction and polarity. Document actual Roll dimensions separately in [requirements](../requirements.md) before any fit assessment.
2. **Interface check:** resolve the [EV002 shield connector discrepancy](EV002-luxorparts-battery-shield.md) and verify charge-voltage/current limits and cell protection *before connecting this pack*. Use a suitable single-cell charger with a verified CC/CV profile and controlled setup.
3. **Current/temperature:** in a protected, supervised bench configuration away from flammables, record cell voltage, input/output current and surface temperature during typical simulated sensor/LED activity. Stop on unexpected heat, swelling, damage or voltage instability.
4. **Usable-energy/runtimes:** log actual voltage, current and time under a representative measured duty cycle; terminate well before an unverified protection cutoff. Define needed runtime and testing criteria in [requirements](../requirements.md).
5. **Enclosure review:** check protective mechanical separation and secure retention without puncturing, bending or pressing on the pouch. Do not place any battery-powered prototype on the dog before [recorded safety clearance](../safety.md).

## Findings and evidence

| Finding | Classification | Evidence |
| --- | --- | --- |
| Nominal 3.7 V, 1200 mAh, 4.2 V charge, 1.2 A limits, dimensions 63 × 36 × 4.7 mm and mass 23.3 g | Published specification (not measured) | [Product specification](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/arduino-tillbehor/luxorparts-li-po-batteri-37-v-med-kontakt-1200-mah-p87924) |
| Nominal stored energy **4.44 Wh** | **Calculated estimate** | 3.7 V × 1.2 Ah (published nominal values) |
| Approx. **7.1 h** for *hypothetical* 0.50 W load and 80% efficiency | **Illustrative estimate, not measured or predicted runtime** | 4.44 Wh × 0.8 / 0.50 W |
| Physical fit, real usable capacity, internal protection features, safe charging with proposed shield | **Unknown** | No direct inspection, verified wiring or test run |
| Potential connector mismatch with article 87296 | **Unresolved compatibility concern** | [EV002 conflict analysis](EV002-luxorparts-battery-shield.md) |

## Conclusion and next action

- **Assessment:** **Requires more evidence**; reasonable **bench energy-storage candidate** but unconfirmed geometry and protection make integrated suitability unknown.
- **Reasoning:** Its nominal energy and supply ratings permit a practical investigation, but the proposed connector combination and mechanical/puncture risks need resolution before use.
- **Next action / decision link:** Inspect/measure the pack and shield, establish a verified charging/protection arrangement, and perform logged off-dog discharge/current tests. Record a decision only with supporting [evidence](../../tests/README.md) in [decisions](../decisions.md).

## References

- [Kjell & Company, Luxorparts Li-Po 3.7 V 1200 mAh, article 87924](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/arduino-tillbehor/luxorparts-li-po-batteri-37-v-med-kontakt-1200-mah-p87924) (accessed 2026-11-07; source for rated pack data).
- [Kjell & Company, battery shield article 87296](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/moduler/luxorparts-batterimodul-till-utvecklingskort-p87296) and [Luxorparts shield datasheet](https://www.kjell.com/globalassets/mediaassets/855795_87296_datasheet_en.pdf) (accessed 2026-11-07; incompatible connector descriptions).
