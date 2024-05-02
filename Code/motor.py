import RPi.GPIO as GPIO
import time
import os

class MotorController:
    def __init__(self):
        # Physical pin numbers for motor control
        motor1_pwm_pin = 12  # PWM pin for Motor 1 (Example: Pin 12)
        self.motor1_in1_pin = 16  # Input 1 of the H-Bridge for Motor 1 (Example: Pin 16)
        self.motor1_in2_pin = 18  # Input 2 of the H-Bridge for Motor 1 (Example: Pin 18)

        motor2_pwm_pin = 22  # PWM pin for Motor 2 (Example: Pin 22)
        self.motor2_in1_pin = 24  # Input 1 of the H-Bridge for Motor 2 (Example: Pin 24)
        self.motor2_in2_pin = 26  # Input 2 of the H-Bridge for Motor 2 (Example: Pin 26)

        # Set pin numbering to physical pins
        GPIO.setmode(GPIO.BOARD)

        # Configure motor control pins as outputs
        GPIO.setup(motor1_pwm_pin, GPIO.OUT)
        GPIO.setup(self.motor1_in1_pin, GPIO.OUT)
        GPIO.setup(self.motor1_in2_pin, GPIO.OUT)

        GPIO.setup(motor2_pwm_pin, GPIO.OUT)
        GPIO.setup(self.motor2_in1_pin, GPIO.OUT)
        GPIO.setup(self.motor2_in2_pin, GPIO.OUT)

        # Configure PWM modes with a frequency of 100 Hz
        self.motor1_pwm = GPIO.PWM(motor1_pwm_pin, 100)
        self.motor2_pwm = GPIO.PWM(motor2_pwm_pin, 100)

        # Start PWMs with a duty cycle of 0 (motors are off)
        self.motor1_pwm.start(0)
        self.motor2_pwm.start(0)

        self.duty_cycle = 100
        self.timesec = 0.3

        # Shutdown button
        self.button_pin = 40
        self.button_pressed_counter = 0
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def shutdown(self):
        try:
            # Check if the button is pressed
            if GPIO.input(self.button_pin) == GPIO.HIGH:
                print("Button pressed! Shutting down...")
                self.button_pressed_counter += 1
                print(self.button_pressed_counter)
                if self.button_pressed_counter >= 10:
                    print("clean") #todo
                    # Initiate shutdown
                    GPIO.cleanup()
                    os.system("sudo shutdown now")
                    # Clean up GPIO on exit
        except KeyboardInterrupt:
            pass

    def _motor1_forward(self, duty_cycle):
        GPIO.output(self.motor1_in1_pin, GPIO.HIGH)
        GPIO.output(self.motor1_in2_pin, GPIO.LOW)
        self.motor1_pwm.ChangeDutyCycle(duty_cycle)

    def _motor1_backward(self, duty_cycle):
        GPIO.output(self.motor1_in1_pin, GPIO.LOW)
        GPIO.output(self.motor1_in2_pin, GPIO.HIGH)
        self.motor1_pwm.ChangeDutyCycle(duty_cycle)

    def _motor2_forward(self, duty_cycle):
        GPIO.output(self.motor2_in1_pin, GPIO.HIGH)
        GPIO.output(self.motor2_in2_pin, GPIO.LOW)
        self.motor2_pwm.ChangeDutyCycle(duty_cycle)

    def _motor2_backward(self, duty_cycle):
        GPIO.output(self.motor2_in1_pin, GPIO.LOW)
        GPIO.output(self.motor2_in2_pin, GPIO.HIGH)
        self.motor2_pwm.ChangeDutyCycle(duty_cycle)

    def motor(self, v1, v2, y):
        print(v1, v2, y)
        if y >= 0:
            if v1 >= 0:
                self._motor1_forward(v1)
            if v1 < 0:
                v1 *= -1
                self._motor1_backward(v1)
            if v2 >= 0:
                self._motor2_forward(v2)
            if v2 < 0:
                v2 *= -1
                self._motor2_backward(v2)
        else:
            if v1 >= 0:
                self._motor1_forward(v1)
            if v1 < 0:
                v1 = v1 * -1
                self._motor1_backward(v1)
            if v2 >= 0:
                self._motor2_forward(v2)
            if v2 < 0:
                v2 = v2 * -1
                self._motor2_backward(v2)

        time.sleep(self.timesec)

    def cleanGPIO(self):
        self.motor1_pwm.stop()
        self.motor2_pwm.stop()
        GPIO.cleanup()
