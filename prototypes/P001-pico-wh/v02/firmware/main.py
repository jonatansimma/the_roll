# P001-v02 planned OFF-DOG bench firmware; no hardware test yet.
from machine import Pin, I2C
from time import ticks_ms, ticks_diff, sleep_ms
from struct import unpack
import os

LOG_MODE = "serial"  # serial / file / off
LOG_PATH = "roll_v02.csv"
MAX_ROWS = 3000
DEBOUNCE_MS = 30
HOLD_MS = 500

led = Pin(15, Pin.OUT, value=0)
touch = Pin(14, Pin.IN, Pin.PULL_DOWN)
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100000)
header = "elapsed_ms,touch_raw,touch_stable,led,x_mg,y_mg,z_mg,overrun\n"
log = None
rows = 0

def setup_accel():
    found = [a for a in i2c.scan() if a in (0x19, 0x18)]
    if len(found) != 1:
        raise RuntimeError("Expected exactly one LIS3DH at 0x19 or 0x18")
    addr = found[0]
    if i2c.readfrom_mem(addr, 0x0F, 1)[0] != 0x33:
        raise RuntimeError("Unexpected LIS3DH WHO_AM_I")
    i2c.writeto_mem(addr, 0x20, b"\x00")  # power down during setup
    i2c.writeto_mem(addr, 0x21, b"\x00")  # no high-pass filter
    i2c.writeto_mem(addr, 0x23, b"\x98")  # BDU, +/-4g, HR
    i2c.writeto_mem(addr, 0x20, b"\x47")  # 50 Hz, XYZ, LP disabled
    sleep_ms(100)
    return addr

try:
    if LOG_MODE not in ("serial", "file", "off"):
        raise ValueError("Invalid LOG_MODE")
    addr = setup_accel()
    if LOG_MODE == "file":
        if LOG_PATH in os.listdir():
            raise RuntimeError("Copy/remove previous CSV before capture")
        fs = os.statvfs(".")
        if (fs[1] or fs[0]) * fs[4] < 256 * 1024:
            raise RuntimeError("Insufficient free space for CSV")
        log = open(LOG_PATH, "w")
        log.write(header)
    elif LOG_MODE == "serial":
        print(header, end="")
    # Allow touch baseline to settle; leave pad untouched on startup.
    sleep_ms(1000)
    start = ticks_ms()
    raw = touch.value()
    stable = 0
    changed = start
    released = None

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
        lit = int(bool(stable or released is not None))
        led.value(lit)

        status = i2c.readfrom_mem(addr, 0x27, 1)[0]
        if status & 0x08:  # XYZ new sample available
            data = i2c.readfrom_mem(addr, 0x28 | 0x80, 6)
            xyz = tuple((v >> 4) * 2 for v in unpack("<hhh", data))
            if LOG_MODE != "off" and (log is not None or LOG_MODE == "serial"):
                row = "%d,%d,%d,%d,%d,%d,%d,%d\n" % (
                    ticks_diff(ticks_ms(), start), raw, stable, lit,
                    xyz[0], xyz[1], xyz[2], int(bool(status & 0x80)))
                if log is not None:
                    log.write(row)
                    rows += 1
                    if rows % 100 == 0:
                        log.flush()
                    if rows >= MAX_ROWS:
                        log.close()
                        log = None  # continue sensing, no further file writes
                else:
                    print(row, end="")
        sleep_ms(5)
finally:
    led.value(0)
    if log is not None:
        log.close()
