import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUTTON_1 = 5   # Button 1 -> hostile
BUTTON_2 = 6   # Button 2 -> explode only if hostile was on
BUTTON_3 = 13  # Button 3 -> explode only if hostile was on
BUTTON_4 = 19  # Button 4 -> explode from idle or hostile

HOSTILE_LED = 27
EXPLODE_LED = 22

GPIO.setup(BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(HOSTILE_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(EXPLODE_LED, GPIO.OUT, initial=GPIO.LOW)

state = "idle"

def set_state(new_state):
    global state
    state = new_state
    GPIO.output(HOSTILE_LED, GPIO.HIGH if state == "hostile" else GPIO.LOW)
    GPIO.output(EXPLODE_LED, GPIO.HIGH if state == "explode" else GPIO.LOW)

last1 = last2 = last3 = last4 = False

try:
    while True:
        b1 = GPIO.input(BUTTON_1)
        b2 = GPIO.input(BUTTON_2)
        b3 = GPIO.input(BUTTON_3)
        b4 = GPIO.input(BUTTON_4)

        if b1 and not last1:
            set_state("hostile")

        if b2 and not last2 and state == "hostile":
            set_state("explode")

        if b3 and not last3 and state == "hostile":
            set_state("explode")

        if b4 and not last4 and state in ("idle", "hostile"):
            set_state("explode")

        last1, last2, last3, last4 = b1, b2, b3, b4
        time.sleep(0.05)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
