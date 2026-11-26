# TP002 — USB dual-sensor commissioning and comparison

- **Method revision:** 1.
- **Status:** Proposed; no runs performed.
- **Objective:** Explore contact and motion signals (REQ001, REQ002, REQ006) and bench indication logic (partial REQ003); not battery-runtime or handler-visibility validation.
- **Equipment:** [P001-v03](../../prototypes/P001-pico-wh/v03/build.md), USB data cable and computer/serial capture, multimeter, rigid insulating fixture, removable dielectric sheets, conductive contact fixture, stopwatch/video.
- **Related method:** [TP001](TP001-dual-sensor-retrieval.md) is retained for the battery-capable v02 design. This method is USB-only.

## Setup and precautions

Record full firmware commit, actual MicroPython version, sensor board labels, I2C address, 3.3 V rail measurement, contact timing, acceleration configuration, orientation, fixture, dielectric thickness, USB host/cable arrangement, and ambient conditions. Support USB cable with slack so it does not pull the fixture. Keep capacitive pad untouched during startup. No external power supply, battery or LED circuit; the Pico onboard LED is the indicator. All work off-dog; keep electronics dry and do not perform free drops while tethered. USB grounding and cable motion can influence results.

## Steps

1. Before attaching sensors, run the onboard LED REPL test in the build instructions. Observe ON and OFF. Disconnect USB and wire both modules per the build document.
2. Power up from USB and confirm 3.3 V rail, correct address and LIS3DH identity, CSV output, and LED initially off with no contact. Record 10 s baseline; turn fixture slowly through six orientations and verify gravity magnitude approximately 1000 mg and axis signs.
3. Record ten labeled repetitions per exploratory dry condition: light contact through insulation, slow pickup-like movement, fast pickup-like movement, sustained contact while moving, release, re-contact within and beyond the configured hold, motion without contact, and stationary contact. Simulate drop/re-pickup with controlled fixture support, not an actual tethered free drop. Note actual LED transitions and cable disturbances separately.
4. Record a continuous controlled contact for at least 120 s; if a sensor timeout occurs, note duration and output recovery after release. Do not infer indefinite hold if no timeout is observed. Map position and dielectric thickness with repeated trials.
5. Capture raw CSV and independent event labels on the host. Report missed expected contacts, incidental activations, apparent latency, data gaps, overruns, and LED observations. Compare contact-only and motion-only cues and, offline if useful, candidate combinations using separate exploratory and held-out trial sets. Report false-trigger reductions and missed slow pickups.
6. Stop with Ctrl-C/Thonny Stop, observe LED off, save host data and record run under [tests](../README.md). If initialization or communication fails, record the failure and resolve before proceeding.

## Acceptance and limitations

Use [requirements](../../docs/requirements.md) for criteria; no new thresholds are established by these exploratory repetitions. No battery endurance, enclosure fit, wet exposure, handler visibility or animal safety is demonstrated. Moisture tests, actual drops and untethered operation require a later suitable fixture/revision. The [safety gate](../../docs/safety.md) remains mandatory before any dog exposure.
