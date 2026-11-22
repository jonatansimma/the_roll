# P001-v01 — Pico WH contact-to-LED bench circuit

- **Status:** Planned, **NOT BUILT OR TESTED**.
- **Purpose:** Verify USB programming, reusable LED switching, battery operation, and contact-triggered indication **off-dog**.
- **Controller:** First-generation Raspberry Pi Pico WH; 3.3 V GPIO, 51 x 21 mm board; 2x20 pre-fitted headers.
- **Inputs:** Initially pushbutton between GP14 and GND, using internal pull-up. Optionally substitute a verified 3.3 V digital capacitive touch breakout on GP14 (active-high firmware configuration required).
- **Output:** GP15 drives a single identified, current-limited LED via resistor to ground. Recycled multi-LED arrays require a **separately assessed resistor-per-string / appropriate driver**, not direct GPIO connection.
- **Power:** During programming **USB only**. For isolated battery bench test, 3 alkaline AA cells (nominal ~4.5 V fresh, check actual voltage and polarity) on **VSYS pin 39**, negative on **GND**; USB disconnected. Use a switch and preferably a suitably rated low-value fuse/polyswitch. Never wire batteries to GPIO, 3V3(OUT), or VBUS. Never connect USB concurrently with this basic unisolated battery wiring; consult manufacturer's power-ORing guidance for dual-source design.
- **Enclosure / dog use:** No enclosure; external AA pack and exposed parts; **ABSOLUTELY NO DOG EXPOSURE**. Future integrated battery, weight and geometry feasibility are open.

## BOM

See [bom.csv](bom.csv). Reused LED board and 3-AA holder are **unidentified**, so do not power a salvaged LED module before inspecting circuit topology and determining current limit and rated voltage.

## Electrical wiring for initial single discrete LED

```text
Pico GP15 (physical pin 20) -- 330 ohm -- LED anode (+)
LED cathode (-) ------------------------- Pico GND

Pico GP14 (physical pin 19) -- normally open pushbutton -- Pico GND
   (firmware internal pull-up; pressed = GPIO LOW)

For external battery-only bench operation:
3 x AA holder + -- switch / optional fuse -- Pico VSYS (physical pin 39)
3 x AA holder - -------------------------- Pico GND (e.g. pin 38)
USB disconnected.
```

Single-LED resistor example: with 3.3 V GPIO, nominal 2 V red LED forward drop, 330 ohm yields about **3.9 mA**, neglecting GPIO output droop. This is **not** a generic resistor value for the unknown recycled LED assembly. Check actual LED polarity, forward voltage, resistor location and total current first. A transistor/MOSFET switching stage with source-appropriate current limiting is needed for higher-current LED groups.

## Optional capacitive breakout substitution

Only after verifying its board's rated supply and signal: breakout VCC -> Pico 3V3(OUT) **pin 36**; GND -> GND; digital OUT -> GP14 (physical pin 19). Set `ACTIVE_LOW = False` in code if sensor output asserts high. If the breakout uses pull-ups to higher than 3.3 V, **do not connect**. Mount an insulated electrode for bench tests. Do not connect a bare electrode or exposed wiring to a dog.

## Firmware

- [MicroPython source](firmware/main.py). Flash suitable Pico W/WH MicroPython UF2 using BOOTSEL USB bootloader; copy as `main.py` to MicroPython filesystem via Thonny or an equivalent transfer method.
- Default input: button active-low; 30 ms stability debounce; provisional 500 ms LED hold after last contact.
- **Hold timing is an experimental setting, not an approved behavior requirement.** Input transitions (including a drop and re-pickup) should be logged and compared. No code was executed on the board.
- Wi-Fi is not used.

## Bench commissioning (proposed)

1. Inspect board/LED salvaged parts for damage and document actual wiring, component identities, voltage and mass.
2. With battery disconnected, program Pico via USB. Connect one low-current resistor-limited discrete LED, then pushbutton; verify LED and log pickup/release/re-pickup transitions.
3. Disconnect USB; connect measured AA pack to VSYS/GND through switch, verify polarity with multimeter **before powering**. Repeat and measure idle and lit current.
4. Substitute compatible digital touch breakout; compare insulated gentle-touch/release/wet/impact handling without dog involvement; log counts and durations.
5. Determine appropriate external LED driver only after identifying recycled LED assembly. Later evaluate accelerometer separately under EV008, documenting new hardware revision.
6. Produce [recorded test runs](../../../tests/README.md) citing actual flashed firmware Git commit and conditions. Test battery endurance for 1 h and 12 h only with measured current and documented representative operating profile. Do not claim pass from calculation alone.

## Unresolved

Recycled LEDs' topology/polarity/rating; AA holder connector and contact integrity; actual Pico board health; capacitance sensor module availability; final LED timing/brightness; effect of water/saliva; false positive rates; internal battery form factor; ability to fit envelope and weight; animal safety inspection. See [requirements](../../../docs/requirements.md), [safety](../../../docs/safety.md).
