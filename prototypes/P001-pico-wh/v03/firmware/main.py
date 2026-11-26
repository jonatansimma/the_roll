# P001-v03: USB-only OFF-DOG bench firmware; not hardware-tested.
from machine import Pin, I2C
from time import ticks_ms, ticks_diff, sleep_ms
from struct import unpack

DEBOUNCE_MS = 30
HOLD_MS = 500

# Pico W/WH LED is controlled through the wireless chip, not GP25.
led = Pin("LED", Pin.OUT)
led.off()

def setup_accel(bus):
    found = [a for a in bus.scan() if a in (0x19, 0x18)]
    if len(found) != 1:
        raise RuntimeError("Expected one LIS3DH at 0x19 or 0x18")
    addr = found[0]
    if bus.readfrom_mem(addr, 0x0F, 1)[0] != 0x33:
        raise RuntimeError("Unexpected LIS3DH WHO_AM_I")
    bus.writeto_mem(addr, 0x20, b"\x00")  # power down
    bus.writeto_mem(addr, 0x21, b"\x00")  # no high-pass filter
    bus.writeto_mem(addr, 0x23, b"\x98")  # BDU, +/-4g, HR
    bus.writeto_mem(addr, 0x20, b"\x47")  # 50 Hz, XYZ enabled
    sleep_ms(100)
    return addr

def main():
    touch = Pin(14, Pin.IN, Pin.PULL_DOWN)
    bus = I2C(0, sda=Pin(4), scl=Pin(5), freq=100000)
    addr = setup_accel(bus)
    sleep_ms(1000)  # pad must be untouched during startup
    print("elapsed_ms,touch_raw,touch_stable,led,x_mg,y_mg,z_mg,overrun")
    start = ticks_ms()
    raw = touch.value()
    stable = 0
    changed = start
    released = None
    lit = 0

    while True:
        now = ticks_ms()
        observed = touch.value()
        if observed != raw:
            raw = observed
            changed = now
        if raw != stable and ticks_diff(now, changed) >= DEBOUNCE_MS:
            stable = raw
            released = None if stable else now
        if released is not None and ticks_diff(now, released) >= HOLD_MS:
            released = None
        desired = int(bool(stable or released is not None))
        if desired != lit:
            led.value(desired)
            lit = desired

        status = bus.readfrom_mem(addr, 0x27, 1)[0]
        if status & 0x08:
            data = bus.readfrom_mem(addr, 0x28 | 0x80, 6)
            xyz = tuple((v >> 4) * 2 for v in unpack("<hhh", data))
            print("%d,%d,%d,%d,%d,%d,%d,%d" % (
                ticks_diff(ticks_ms(), start), raw, stable, lit,
                xyz[0], xyz[1], xyz[2], int(bool(status & 0x80))))
        sleep_ms(5)

try:
    main()
finally:
    led.off()
