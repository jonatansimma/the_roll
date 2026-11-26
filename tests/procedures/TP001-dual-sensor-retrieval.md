# TP001 — Comparative contact and motion bench procedure

- **Method revision:** 1
- **Objective:** Compare candidate retrieval signals and power use against REQ001–REQ004 and REQ006; this is exploratory, not validation.
- **Equipment:** Pico WH dual-sensor fixture, known test LED, USB host with serial capture, multimeter, verified battery holder/cells, insulating mock cylinder, removable dielectric sheets, conductive contact fixture, stopwatch or video, and damp cloth.

**Status:** Proposed procedure, no runs performed. All trials off-dog; no animal clearance. Hardware and firmware: [P001-v02](../../prototypes/P001-pico-wh/v02/build.md). Requirements and acceptance thresholds: [requirements](../../docs/requirements.md). [Test recording rules](../README.md).

## Setup and recorded configuration

Record full firmware Git commit, sensor board IDs, I2C address, supply type/voltage, contact debounce/hold, accelerometer settings, fixture mass, electrode/dielectric dimensions, mounting orientation, logging mode, ambient conditions and trial labels. Use an insulating mock cylinder and single known test LED. Use USB for serial logging; battery-only file mode for short independent traces. Never expose live electronics to water or the dog. Use a stopwatch/video of the fixture to independently mark events; align with log start and record alignment uncertainty. Preserve CSV and trial labels with each run. CSV is host-polled, not hardware-synchronized; report timing gaps and overrun flags.

## Procedure (proposed exploratory counts; not acceptance criteria)

1. Power-up untouched; verify identity and at-rest gravity magnitude around 1000 mg, then turn through six orientations. Check raw/stable touch, LED state, signed axes, data gaps. Record baseline for 10 s.
2. For each dry condition, run at least 10 repetitions, with separate labeled rest/transition windows: gentle conductive contact through plastic, slow pickup, fast pickup, sustained hold with movement, release, re-pickup within ~500 ms, re-pickup after ~500 ms, ordinary swinging/handling without contact, shake/impact, contact without pickup. Include slow contacts with little motion. Use consistent safe bench fixtures, not actual dog bite force; simulated contact does not validate behavior.
3. Repeat relevant contact and non-contact trials with a damp exterior on a sealed dummy fixture, including stationary wet surface and incidental wet contact. Keep exposed electronics dry, stop on ingress, and record wetting method. Map grip position and dielectric thickness separately.
4. Hold conductive contact continuously for at least 120 s (serial mode), and longer if needed to observe output timeout. Record any spontaneous LOW while contact persists, release and re-trigger. If no timeout is observed within that window, report only that observation; do not infer unlimited hold.
5. For each event, record expected action and compare raw contact, stable contact and actual LED. Evaluate acceleration separately using labeled pickup/drop/ordinary-motion windows. Compare candidate offline fusion rules (contact plus a motion cue in a specified time window) against contact-only and motion-only rules. Choose exploratory motion thresholds from a subset, then compare on separate held-out repetitions. Report misses, false activations, latency, short gaps and any reduction in sensitivity; no pass/fail threshold until requirements specify one.
6. Measure battery input current with sensing active, LED off/on and representative duty cycles. Use logging off for endurance; use brief file captures separately, noting logging overhead. Test mandatory duration and preferred target with a documented operating profile; check rail and LED function at defined intervals. Do not connect USB while battery is attached. Do not extrapolate endurance from nominal cell capacity alone.
7. Record runs with the exact flashed commit, settings, actual conditions, raw CSV/video references, counts, observations, failures and next steps. If hardware or electrode configuration changes, document revision as appropriate. No testing on the dog until the documented [safety gate](../../docs/safety.md) is satisfied.
