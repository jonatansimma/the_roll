# P001-v01: OFF-DOG BENCH EXPERIMENT ONLY (MicroPython, Pico WH)
# GP14: active-low button with internal pullup by default.
# GP15: one low-current, resistor-limited LED (NOT an unknown salvaged array).
from machine import Pin
from time import ticks_ms, ticks_diff, sleep_ms

INPUT_GPIO = 14
LED_GPIO = 15
ACTIVE_LOW = True       # set False for verified active-high sensor breakout
DEBOUNCE_MS = 30
HOLD_MS = 500          # PROVISIONAL bench experiment, not a project requirement

sense = Pin(INPUT_GPIO, Pin.IN, Pin.PULL_UP if ACTIVE_LOW else Pin.PULL_DOWN)
led = Pin(LED_GPIO, Pin.OUT, value=0)

def read_contact():
    state = sense.value()
    return state == 0 if ACTIVE_LOW else state == 1

stable = read_contact()
raw = stable
changed_at = ticks_ms()
last_seen_at = changed_at if stable else None
print("P001-v01 bench input ready; initial contact:", stable)

while True:
    now = ticks_ms()
    observed = read_contact()
    if observed != raw:
        raw = observed
        changed_at = now
    if raw != stable and ticks_diff(now, changed_at) >= DEBOUNCE_MS:
        stable = raw
        print(now, "CONTACT" if stable else "RELEASE")
    if stable:
        last_seen_at = now
    active = last_seen_at is not None and ticks_diff(now, last_seen_at) < HOLD_MS
    led.value(1 if active else 0)
    sleep_ms(5)
