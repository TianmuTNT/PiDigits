import sys
import time

def pi_digits():
    q, r, t, i = 1, 180, 60, 2
    while True:
        u = 3 * (3 * i + 1) * (3 * i + 2)
        y = (q * (27 * i - 12) + 5 * r) // (5 * t)
        yield y
        q, r, t, i = 10 * q * i * (2 * i - 1), 10 * u * (q * (5 * i - 2) + r - y * t), t * u, i + 1

digits = pi_digits()

sys.stdout.write(f"{next(digits)}.\n")
sys.stdout.flush()

try:
    while True:
        d = next(digits)
        sys.stdout.write(str(d))
        sys.stdout.flush()
        time.sleep(0.1)  # speed

except KeyboardInterrupt:
    sys.stdout.write("\nStopped.\n")
    sys.stdout.flush()
