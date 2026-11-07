# EV002 — Luxorparts battery shield for development boards

- **Status:** Researching — desk assessment only; **connector/charging checks required before connecting a cell**
- **Problem / requirement IDs:** [REQ004, REQ005, REQ006, REQ008, REQ009](../requirements.md#functional-and-practical-requirements)
- **Author and date:** ChatGPT desk research, 2026-11-07
- **Related records:** [EV001 D1 Mini](EV001-luxorparts-wemos-d1-mini.md), [EV003 Li-Po cell](EV003-luxorparts-lipo-1200mah.md), [safety review](../safety.md), [test records](../../tests/README.md); no build or test run exists

## Objective and operating principle

Assess whether Kjell & Company article **87296** can power a D1 Mini-class controller from a **single-cell lithium battery** and provide a practical charging interface for an **off-dog bench prototype**. The shield boosts battery voltage to a nominal 5 V output for the development board and accepts charging power via its own micro-USB port. A shield does not independently demonstrate safe charge/discharge protection.

## Candidate components and sources

| Candidate / part | Key specification | Source / datasheet | Estimated cost / availability |
| --- | --- | --- | --- |
| Luxorparts battery shield, article 87296 | Lithium cell input specified **3.3–4.2 V**; nominal **5 V boost output, max 1 A**; micro-USB charging input **5 V recommended**; charge current selectable **0.5 A / 1 A** (J1); optional J2 battery/A0 feature | [Product](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/moduler/luxorparts-batterimodul-till-utvecklingskort-p87296), [Luxorparts datasheet](https://www.kjell.com/globalassets/mediaassets/855795_87296_datasheet_en.pdf) | Indicative listing ~49 SEK promotion (~100 SEK regular) in indexed November 2026 listings; confirm live price/stock |

The product listing additionally advertises a **1 A resettable fuse**. Neither that statement nor the output-current rating establishes cell-level overcharge, overdischarge, temperature, or short-circuit protection.

**Material source conflict:** The **retailer product page calls the battery connector JST-XH 2.54 mm**, while the **manufacturer's article-87296 datasheet calls port 1 “PH2-2.0 mm”**. These are different connector families/pitches and must **not** be assumed interchangeable. The proposed [EV003 cell](EV003-luxorparts-lipo-1200mah.md) has a **JST-PH 2.0 mm** plug per its own listing. Inspect/measure the actual shield connector and **verify red/black polarity pin-by-pin** against the actual battery before mating; never force a plug or reverse polarity.

## Expected advantages, limitations, and uncertainties

- **Expected advantages:** convenient stacked D1 Mini form factor, local charging access and 5 V boost output; reduces discrete power wiring in an initial experiment.
- **Trade-offs:** boosting a nominal 3.7 V cell to 5 V and then regulating to 3.3 V on the controller creates conversion losses; efficiency and standby (quiescent) current are **unknown**, so runtime cannot be predicted from the cell rating alone.
- **Charging:** J1 is specified to select **0.5 A or 1 A** maximum charging current. Start by confirming its physical setting and using the lower setting where practical, then measure actual charging behavior with a suitable instrument. Use a regulated **5 V** USB charger even though the document also quotes a 10 V maximum input rating.
- **Potential analog-input hazard:** Datasheet says **J2 connects the battery to A0**. The [D1 Mini](EV001-luxorparts-wemos-d1-mini.md) specifies **3.2 V maximum at A0**, whereas a charged cell reaches **4.2 V**. **Leave J2 open/unfitted** until the exact on-board scaling and maximum A0 voltage have been verified against a schematic and by measurement. Do not apply unscaled cell voltage to A0.
- **Unknown protection details:** No sufficiently explicit documentation was found establishing complete cell undervoltage cutoff, overcharge protection, thermal monitoring, reverse-polarity protection, load sharing during charging, or low standby current for **this assembled shield**. Do not infer them from the presence of a charging IC or fuse.
- **Mechanical/environmental hypothesis:** exposed charging port, stacking headers, and circuitry complicate water/saliva sealing and secure retention.

## Integration implications

- The shield is plausibly compatible with the D1 Mini **5V and GND** header arrangement, but verify the actual stack orientation and voltage rail before attaching [EV001](EV001-luxorparts-wemos-d1-mini.md).
- Plan for external LED drivers: **1 A boost output is a stated limit, not a verified continuous budget** after controller/sensor current, transients and heat. A rail sag during controller startup/LED pulses could reset the microcontroller.
- The listed battery voltage operating range starting at 3.3 V is **not** equivalent to guaranteed operation through the proposed battery's full discharge range. A low-voltage strategy and actual dropout/cutoff behavior require tests.
- Charging arrangements in a closed, wet or bite-exposed cylinder require the full [safety assessment](../safety.md). This is a **bench candidate**, not an approved wearable power subsystem.

## Proposed evaluation experiments

All experiments are proposals; log conditions and numerical readings in linked [test runs](../../tests/README.md), not this evaluation.

1. **Unpowered identity check:** photograph both board faces, identify chip markings, inspect/measure battery socket pitch and keyed orientation, check connector polarity with a meter; compare with the proposed battery and both conflicting documents. **Do not connect the cell before resolving mismatch.**
2. **Regulated output test:** with an appropriate protected test cell and safe setup, check 5 V output at no load and increasing *known* resistive/electronic loads (including transient load); document current, voltage sag, heating, efficiency and cutoff. Do not exceed published ratings.
3. **Charging verification:** at ambient **10–45 °C** (cell's published charging range), verify the 0.5 A J1 setting, charging endpoint near the cell's rated **4.2 V**, and temperature; check whether charging simultaneously with a connected system is allowed by manufacturer documentation before attempting it.
4. **A0 / J2 hazard check:** without risking the controller, verify the shield's battery-sense path and scaled voltage; keep J2 disconnected until shown within the controller's maximum.
5. **Protection and idle-current investigation:** identify real overdischarge/overcurrent protection and measure no-load consumption. Do not deliberately short or deep-discharge a lithium cell as an ad-hoc test.

## Findings and evidence

| Finding | Classification | Evidence |
| --- | --- | --- |
| 5 V boost supply rated up to 1 A; J1 charging selection 0.5/1 A | Published specification (not measured) | [Luxorparts shield datasheet](https://www.kjell.com/globalassets/mediaassets/855795_87296_datasheet_en.pdf) |
| Battery socket family is **contradictory**: XH 2.54 mm versus PH 2.0 mm | **Unresolved source conflict** | [Retailer](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/moduler/luxorparts-batterimodul-till-utvecklingskort-p87296) vs [datasheet](https://www.kjell.com/globalassets/mediaassets/855795_87296_datasheet_en.pdf) |
| Optional A0 connection may exceed D1 Mini's 3.2 V maximum unless adequately scaled | **Proposed hazard / unverified circuit detail** | [Shield datasheet](https://www.kjell.com/globalassets/mediaassets/855795_87296_datasheet_en.pdf), [board datasheet](https://www.kjell.com/globalassets/mediaassets/855793_87294_datasheet_en.pdf) |
| Converter efficiency, current under load, complete cell protection and charger thermal behavior | **Unknown** | No datasheet confirmation for assembled system and no test runs |

## Conclusion and next action

- **Assessment:** **Requires more evidence; do not connect the proposed cell until connector identity/polarity are verified.**
- **Reasoning:** Convenient voltage-boost/charging concept, but supplier inconsistency and unverified protection and battery-monitor circuitry are significant integration risks.
- **Next action / decision link:** Inspect the physical shield and record connector pitch/polarity, J1/J2 states, 5 V output and actual charge/protection behavior in a reproducible [test run](../../tests/README.md). Only then consider selection in [decisions](../decisions.md).

## References

- [Kjell & Company, article 87296](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/moduler/luxorparts-batterimodul-till-utvecklingskort-p87296) (accessed 2026-11-07; lists JST-XH 2.54 mm).
- [Luxorparts, Battery shield datasheet, article 87296](https://www.kjell.com/globalassets/mediaassets/855795_87296_datasheet_en.pdf) (dated 2022-08-17; accessed 2026-11-07; lists PH2-2.0 mm).
- [Kjell & Company, proposed cell, article 87924](https://www.kjell.com/se/produkter/el-verktyg/elektronik/arduino/arduino-tillbehor/luxorparts-li-po-batteri-37-v-med-kontakt-1200-mah-p87924) (accessed 2026-11-07).
