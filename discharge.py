import RPi.GPIO as GPIO
import time


def rotate_servo(pin):
    # Set up the GPIO pin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)

    # Set up the PWM controller
    pwm = GPIO.PWM(pin, 50)
    pwm.start(0)

    # Rotate the servo 90 degrees
    pwm.ChangeDutyCycle(7.5)
    time.sleep(1)

    # Rotate the servo back to its original position
    pwm.ChangeDutyCycle(2.5)
    time.sleep(1)

    # Clean up the GPIO pin and PWM controller
    pwm.stop()
    GPIO.cleanup()


# Example usage: rotate the servo on GPIO pin 11
