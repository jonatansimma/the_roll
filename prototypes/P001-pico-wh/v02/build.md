# P001-v02 — Dual-sensor retrieval bench prototype

- **Status:** Planned; owner reports purchase of both sensor modules on 2026-11-26. Delivery, assembly, operation and safety not verified.
- **Purpose:** Collect synchronized contact and acceleration observations, demonstrate an experimental contact-to-LED signal, and assess feasibility of later sensor fusion.
- **Controller:** Raspberry Pi Pico WH (unchanged).
- **Predecessor:** [v01](../v01/build.md); preserved.
- **Evaluations:** [EV009 EKM029 LIS3DH](../../../docs/evaluations/EV009-electrokit-ekm029-lis3dh.md), [EV010 Adafruit 1374 AT42QT1010](../../../docs/evaluations/EV010-adafruit-1374-at42qt1010.md).
- **Authority:** This revision is a proposed design on agent_main, not an approved decision on main. See [requirements](../../../docs/requirements.md), [safety gate](../../../docs/safety.md).

## Change from v01

Replace the simulated button with the purchased active-high capacitive breakout; add the purchased 3-axis accelerometer. Retain a single current-limited test LED. Contact controls the LED provisionally; motion is logged independently, **not a mandatory gate**. No enclosure, salvaged LED circuit or final battery selection is implied. No tests have been run on v01 or v02.

## BOM and wiring

See [bom.csv](bom.csv). Power off before wiring. Solder appropriate headers or use a Qwiic-to-2.54-mm adapter; do not assume a Pico debug connector is Qwiic. Verify actual pin labels and solder bridges on the delivered parts.

| Pico WH signal | Physical pin | Connection |
| --- | --- | --- |
| 3V3(OUT) | 36 | Adafruit VDD and EKM029 V+ (or Qwiic 3.3 V via one supply path) |
| GND | 38 or other GND | Both sensor grounds, test LED cathode, battery negative |
| GP4 / I2C0 SDA | 6 | EKM029 SDA |
| GP5 / I2C0 SCL | 7 | EKM029 SCL |
| GP14 | 19 | Adafruit OUT (active high); no v01 button connected |
| GP15 | 20 | 330-ohm resistor to single identified red LED anode; cathode to GND |
| VSYS | 39 | External battery positive via rated protection and switch, USB disconnected |

Use the EKM029 on its factory I2C setting; CS and bus lines have onboard pull-ups. Leave INT1/INT2, ADC and other unused pins unconnected. Leave solder jumpers unchanged. Use only one module supply path (Qwiic or header). Confirm default address 0x19 and WHO_AM_I 0x33; 0x18 is supported if the address jumper differs. No 5 V signals on GPIO or sensor bus. No extra I2C pull-ups initially. Begin at 100 kHz.

### Power

USB only for initial commissioning and serial capture. The existing 3-AA holder is external bench power only. A 3-AAA series alkaline pack (nominal 4.5 V) or 3-AAA NiMH pack (nominal 3.6 V) is an **unselected candidate** for later experiments. Inspect holder, verify polarity and actual open-circuit/loaded voltage, use appropriate fuse/switch and connect only to VSYS/GND with USB unplugged. Never connect batteries to 3V3(OUT) or VBUS. Do not use three 10440 lithium-ion cells. Do not simultaneously connect USB and this unisolated pack; consult Pico power-ORing guidance for a later dual-source circuit. Both sensors receive regulated 3.3 V from the Pico. Keep the unknown salvaged LEDs disconnected until their topology, voltage and current are identified; use a single known LED and resistor as in v01. A larger LED assembly needs a separately assessed current-limiting/driver circuit.

## Mechanical concept (not enclosed)

For bench work rigidly mount EKM029 to a nonconductive mock cylinder/fixture and record its axis orientation. Secure the AT42QT1010 near the proposed grip area, initially using its onboard pad with a removable insulating sheet; do not expose conductive parts to an animal. Map sensitivity at different positions and thicknesses; a later remote electrode or enclosure changes capacitance and requires retesting. Keep electrode wiring short and away from ground planes, battery and moving wires; don't add permanent foil or alter jumpers until tests justify it.

For a future 120 x 35 mm outer-body target, locate the controller and batteries axially and use physical mockups. The two sensor PCBs (23 x 18 mm and 20 x 28 mm nominal) do not establish installed fit; include plugs, headers, cable clearance, shell, LED optics, attachment and retention. Three AAA cells can consume much of the mass budget; weigh actual cells/holder and boards before committing to packaging. No final enclosure or battery geometry has been established.

## Firmware and configuration

Source: [main.py](firmware/main.py); Pico W/WH MicroPython UF2, standard machine/time/struct/os modules, no external driver required. Flash via BOOTSEL, then upload main.py with Thonny. Test over USB first. Wi-Fi not initialized. Start with default settings:

- LIS3DH 50 Hz output data rate, +/-4 g range, high-resolution mode, block-data update; 12-bit left-aligned signed samples converted to mg with nominal 2 mg/count. Read XYZ when data-ready; overrun flags are recorded; not a guaranteed lossless 50 Hz logger.
- Contact input polled nominally every 5 ms; 30 ms stable-state debounce. LED follows debounced contact and remains on for 500 ms after release (experimental only). No motion gating. A re-pickup inside the hold extends indication. The AT42QT1010 may time out on a sustained grip; code cannot distinguish timeout from a true release.
- CSV output: elapsed time (ms from startup, wrapping ticks handled for short experiments), raw contact, debounced contact, LED state, XYZ (mg), overrun flag. A sample row records the host read time, not an exact synchronized hardware timestamp. Short events may fall between samples; USB/file I/O may add jitter.
- Default LOG_MODE = "serial" for USB logging. Set "file" before unplugging for a short battery run; saves a new roll_v02.csv, refuses overwrite and stops recording after 3000 rows (roughly one minute at 50 Hz). Existing file must be copied off and removed before another capture; allow 256 KiB free. File mode flushes periodically; power loss may lose data. Set "off" for battery endurance (no CSV printing/writing). Logging affects power and timing. No real-time clock, persistent event latch or validated classifier.
- Startup/communication fault switches test LED off and stops the script; reconnect/inspect and restart after resolving fault. Does not certify a safe indication under all failure modes. No dog exposure.

## Build and verification

1. Inspect board markings, headers and polarity. With USB disconnected and no battery, check wiring and absence of shorts. Attach only the known test LED and AT42QT1010, then EKM029. Check rail at 3.3 V. Ensure sensor pad is untouched during power-on calibration.
2. Start firmware with USB, battery disconnected. Verify sensor identity, CSV and indicator. Compare resting acceleration magnitude to approximately 1000 mg; rotate fixture and verify signed axes. Check touch, release and re-contact, including within and beyond the 500 ms hold.
3. Run [planned comparative procedure](../../../tests/procedures/P001-v02-dual-sensor.md). For battery tests, load settings over USB, power off, disconnect USB, connect verified pack, and restart. Do not reconnect USB until pack disconnected. Record full firmware commit, settings and actual hardware for each run.
4. Inspect actual mass/fit and recycled LED module separately; assess whole-system operating time with measured current and representative LED duty cycle. Later review whether motion adds discrimination and whether a different hardware revision is justified.

## Evidence and limitations

No build or test results. No validated classifier, runtime, grip force threshold, mass budget, enclosure fit, or animal safety approval. See [tests](../../../tests/README.md) and [safety](../../../docs/safety.md). Final LED timing, maximum-on handling, battery selection and any combined classifier remain unresolved.

## Technical references

- [Electrokit EKM029 board documentation](https://docs.electrokit.com/en/modules/EKM029/index.html)
- [ST LIS3DH datasheet](https://www.st.com/resource/en/datasheet/lis3dh.pdf), register descriptions and sensitivity table.
- [Adafruit momentary breakout wiring](https://learn.adafruit.com/adafruit-capacitive-touch-sensor-breakouts/toggle-and-momentary)
- [Pico documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
