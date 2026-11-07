# Project ROLL — DIY Prototype Roadmap

This roadmap turns the [baseline instructions](baseline_instructions.md) into practical milestones. It is a **proposed plan**, not a record of completed work. The project's scope is one functional DIY prototype, not a finished commercial product.

**Working method:** build → test → troubleshoot → improve.

## 1. Define the use case and constraints

- [ ] Measure the current Roll's length, diameter, weight, and neck attachment.
- [ ] Observe how the dog grips and retrieves it, without testing an electronic prototype on the dog.
- [ ] Identify expected exposure to saliva, rain, impacts, and vibration.
- [ ] Decide what the LED signal should do: when it starts, how it stops/resets, and when it must be visible.
- [ ] Record initial measurable targets for detection, false alarms, visibility, battery runtime, and size.

**Output:** a short requirements sheet with measurements, assumptions, unresolved questions, and proposed pass/fail criteria.

## 2. Explore retrieval detection

- [ ] Compare pressure/mechanical switches, capacitive sensing, accelerometers, and combinations where justified.
- [ ] Bench-test promising candidates separately with simulated retrieval and ordinary movement/contact.
- [ ] Investigate false triggers, missed detections, sensor sensitivity, and effects of moisture.
- [ ] Compare power use, wiring complexity, and mechanical integration.

**Output:** test results and a reasoned choice of sensor approach. Do not assume a particular sensor is proven before testing.

## 3. Build the basic electronics

- [ ] Select readily available sensor, LEDs, power source, and the simplest suitable controller, if one is needed.
- [ ] Draw a wiring diagram and record relevant voltage/current ratings.
- [ ] Assemble a workbench prototype using accessible DIY tools.
- [ ] Implement basic sensor-to-LED behavior; document any firmware and required libraries.
- [ ] Verify operation without a dog.

**Output:** reproducible wiring, a parts list, and a functioning bench demonstration.

## 4. Troubleshoot and refine

- [ ] Measure detection success, activation delay, missed detections, and false alarms in repeated trials.
- [ ] Adjust thresholds, filtering, and LED timing/reset behavior if needed.
- [ ] Measure standby and active current; estimate and then test battery runtime.
- [ ] Record failures, changes, and repeat-test results.

**Output:** a stable bench prototype and documented results against the selected criteria.

## 5. Integrate

**Baseline instruction:** “Package electronics in a simple cylinder; repeat testing.”

- [ ] Lay out the sensor, battery, wiring, and LEDs inside a practical cylindrical enclosure.
- [ ] Plan attachment, sealing, assembly access, and secure retention of every component.
- [ ] Use simple DIY fabrication or 3D printing as useful.
- [ ] Repeat detection, LED, and power tests with the electronics enclosed.

**Output:** an assembled Roll prototype and updated drawings, dimensions, and wiring.

## 6. Validate

**Baseline instruction:** “Run bench, handling, and environmental tests. Only then, after safety checks, evaluate in carefully supervised dog training. Improve from results.”

- [ ] Repeat controlled detection tests and count hits, misses, and false activations.
- [ ] Check LED brightness, visibility, timing, and reset.
- [ ] Verify active/standby consumption and measured battery runtime.
- [ ] Test attachment, impacts, vibration, enclosure integrity, and moisture exposure.
- [ ] Inspect battery containment, bite exposure, loose parts, electrical faults, and temperature before any live-dog evaluation.
- [ ] If safe to proceed, evaluate in carefully supervised training and record whether the Roll interferes with normal behavior.
- [ ] Revise the design from measured results.

**Output:** a test report with pass/fail results, limitations, and next changes.

## Test record template

For each test, record: **prototype version · setup/conditions · method · number of trials · measured result · acceptance criterion · pass/fail · observed issues · next action**.

Use metric/SI units. Keep estimates separate from measurements and mark untested ideas clearly.

## Prototype completion criterion

The DIY Roll detects deliberate mouth retrieval, activates visible LEDs, avoids unacceptable false signals, runs from a compact battery, fits a cylindrical enclosure, and can be evaluated and improved without unacceptable risks to the dog. Specific numerical thresholds remain **TBD until requirements are defined**.
