# P001-v03 — USB-only dual-sensor bench build

- **Status:** Planned; intended first physical P001 build per owner direction. No assembly, firmware execution, test result or safety clearance is recorded.
- **Purpose:** Verify both purchased sensing modules, display experimental contact indication using the Pico WH onboard LED, and capture contact/motion data over USB.
- **Controller:** Raspberry Pi Pico WH, first-generation RP2040 wireless board.
- **Predecessor:** [v02](../v02/build.md), preserved as an unbuilt alternative; v03 supersedes it for the first physical build.
- **Evaluations:** [EV009 LIS3DH](../../../docs/evaluations/EV009-electrokit-ekm029-lis3dh.md), [EV010 AT42QT1010](../../../docs/evaluations/EV010-adafruit-1374-at42qt1010.md).
- **Authority:** Proposed implementation on agent_main; [main requirements](../../../docs/requirements.md) are unchanged.

## Changes from v02

Owner-directed simplification: USB power only and Pico WH onboard LED only. No external battery pack, external LED, LED resistor/driver, or flash data logging. Keep both sensor modules, existing GPIO allocations, and provisional contact-driven LED behavior. Acceleration is logged independently rather than gating indication. Use the computer for serial CSV capture. Defer battery testing, handler-visible LED design, fit and enclosure work to a later revision; this is not the final battery-powered prototype.

## BOM

See [bom.csv](bom.csv). Use a micro-USB **data** cable to a computer, breadboard and jumpers. The EKM029 may need its included header soldered or a Qwiic adapter; the Adafruit board also needs a suitable connection to its pads. Inspect delivered parts before powering them.

## Electrical assembly

Disconnect USB before making or changing connections. Both modules must use the Pico regulated 3V3(OUT) rail, not VBUS. Verify actual module pin labels. No battery connected to VSYS, no external indicator on GP15, and no connection to GP25. Share grounds.

| Pico WH signal | Physical pin | Module connection |
| --- | --- | --- |
| 3V3(OUT) | 36 | Adafruit VDD/VCC and EKM029 V+ / 3.3 V |
| GND | 38 (or any GND) | Adafruit GND and EKM029 GND |
| GP14 | 19 | Adafruit OUT (active high) |
| GP4 / I2C0 SDA | 6 | EKM029 SDA |
| GP5 / I2C0 SCL | 7 | EKM029 SCL |

This is seven point-to-point sensor connections (two supply, two ground and three signal connections); use breadboard rails if convenient. Leave EKM029 INT1/INT2 and unused pins unconnected; keep factory I2C configuration and pull-ups. Use one EKM029 power route (header or Qwiic). I2C bus starts at 100 kHz; scan for 0x19 or 0x18 and verify WHO_AM_I = 0x33. No extra pull-ups initially.

On Pico WH the onboard green LED connects to the CYW43439 wireless chip, not RP2040 GP25. MicroPython for Pico W provides the named pin `Pin("LED", Pin.OUT)`. Use Pico W/WH firmware, not ordinary Pico or Pico 2 firmware. No Wi-Fi connection or network code is required; onboard LED access still uses the wireless-chip interface.

## Mechanical setup

Bench only: secure the accelerometer rigidly on an insulating fixture and note its axes. Begin with the capacitive onboard pad and a removable insulating sheet. Keep sensor leads fixed relative to the fixture; support the USB cable with slack/strain relief. Cable movement and USB host grounding can change acceleration and capacitive response; retest in a later independent-power configuration. Do not expose electronics to moisture or the dog. No enclosure construction in this revision.

## Firmware

[main.py](firmware/main.py) uses MicroPython built-in machine, time and struct modules. Install the official first-generation [Pico W MicroPython UF2](https://micropython.org/download/RPI_PICO_W/) using BOOTSEL; open Thonny with the appropriate MicroPython interpreter. With sensor pad untouched at power-up, verify the onboard LED first from the REPL with `from machine import Pin; led = Pin("LED", Pin.OUT); led.on(); led.off()` (execute each command separately to observe it). Upload main.py and start it while capturing USB serial output to a file on the computer. The LED must not be driven by a physical header pin. Use Thonny Stop/Ctrl-C to stop; firmware attempts to extinguish the LED on exit.

Experimental settings retained from v02: 50 Hz LIS3DH ODR, +/-4 g high-resolution mode with BDU, nominal 2 mg/count; touch poll target 5 ms, debounce 30 ms, release hold 500 ms. Contact drives the onboard LED; no motion threshold. Data rows contain elapsed_ms,touch_raw,touch_stable,led,x_mg,y_mg,z_mg,overrun. Serial capture is host-polled; actual intervals vary and data loss is possible. A sustained-touch timeout may look like release; test rather than assume. No onboard filesystem capture or battery operating mode. No physical LED wiring. On initialization or I2C error the script stops and attempts LED off. This is experimental, not a fault-tolerant field device.

## Commissioning and verification

1. Before sensors are wired, test the onboard LED via USB and correct Pico W firmware. Disconnect USB.
2. Wire AT42QT1010, then EKM029, with power off. Check for shorts, polarity and rail continuity; power from USB and verify nominal 3.3 V. Keep the touch pad clear at startup.
3. Run firmware and capture CSV. Observe contact/release, re-contact and onboard LED; verify signed acceleration and at-rest magnitude approximately 1000 mg. Follow [TP002](../../../tests/procedures/TP002-usb-dual-sensor.md).
4. Record exact flashed firmware commit and actual configuration in a [test run](../../../tests/README.md). Evaluate contact-only and motion signals before implementing fusion.

## Unresolved and deferred

The onboard LED is a bench indicator, not evidence of handler-visible brightness (REQ003). USB power does not demonstrate battery runtime (REQ004). No fit, mass, moisture, detection-rate or safety requirements are validated. Battery selection, salvaged LED identification, enclosure and final indication behavior remain open. Follow the [dog-exposure gate](../../../docs/safety.md); never test this tethered exposed build on a dog.

## References

- [Raspberry Pi Pico-series documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- [MicroPython for Raspberry Pi Pico W](https://micropython.org/download/RPI_PICO_W/)
- [Raspberry Pi Pico-series Python SDK](https://pip-assets.raspberrypi.com/categories/610-raspberry-pi-pico/documents/RP-008355-DS-1-raspberry-pi-pico-python-sdk.pdf)
- [EKM029 module documentation](https://docs.electrokit.com/en/modules/EKM029/index.html)
- [LIS3DH datasheet](https://www.st.com/resource/en/datasheet/lis3dh.pdf)
- [Adafruit 1374](https://www.adafruit.com/product/1374)
