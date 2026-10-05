import RPi.GPIO as GPIO
import time

PIN1 = 11   # LED
PIN2 = 12   # Buzzer
freq = 523

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)

voice = GPIO.PWM(PIN2, freq)

try:
    # S：3 短
    for i in range(3):
        GPIO.output(PIN1, GPIO.HIGH)
        voice.start(50)
        time.sleep(0.3)

        GPIO.output(PIN1, GPIO.LOW)
        voice.stop()
        time.sleep(0.3)

    time.sleep(0.6)

    # O：3 長
    for i in range(3):
        GPIO.output(PIN1, GPIO.HIGH)
        voice.start(50)
        time.sleep(0.9)

        GPIO.output(PIN1, GPIO.LOW)
        voice.stop()
        time.sleep(0.3)

    time.sleep(0.6)

    # S：3 短
    for i in range(3):
        GPIO.output(PIN1, GPIO.HIGH)
        voice.start(50)
        time.sleep(0.3)

        GPIO.output(PIN1, GPIO.LOW)
        voice.stop()
        time.sleep(0.3)

except KeyboardInterrupt:
    pass

finally:
    voice.stop()
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN2, GPIO.LOW)
    GPIO.cleanup()