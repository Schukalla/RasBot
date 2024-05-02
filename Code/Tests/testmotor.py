import RPi.GPIO as GPIO
import time

# Physical pin numbers for motor control
motor1_pwm_pin = 12  # PWM pin for motor 1 (example: pin 12)
motor1_in1_pin = 16  # Input 1 of the H-bridge for motor 1 (example: pin 16)
motor1_in2_pin = 18  # Input 2 of the H-bridge for motor 1 (example: pin 18)

motor2_pwm_pin = 22  # PWM pin for motor 2 (example: pin 22)
motor2_in1_pin = 24  # Input 1 of the H-bridge for motor 2 (example: pin 24)
motor2_in2_pin = 26  # Input 2 of the H-bridge for motor 2 (example: pin 26)

# Set pin numbering to physical pins
GPIO.setmode(GPIO.BOARD)

# Configure motor control pins as outputs
GPIO.setup(motor1_pwm_pin, GPIO.OUT)
GPIO.setup(motor1_in1_pin, GPIO.OUT)
GPIO.setup(motor1_in2_pin, GPIO.OUT)

GPIO.setup(motor2_pwm_pin, GPIO.OUT)
GPIO.setup(motor2_in1_pin, GPIO.OUT)
GPIO.setup(motor2_in2_pin, GPIO.OUT)

# Configure PWM modes with a frequency of 100 Hz
motor1_pwm = GPIO.PWM(motor1_pwm_pin, 100)
motor2_pwm = GPIO.PWM(motor2_pwm_pin, 100)

# Start PWMs with a duty cycle of 0 (motors are off)
motor1_pwm.start(0)
motor2_pwm.start(0)

def motor1_forward(duty_cycle):
    GPIO.output(motor1_in1_pin, GPIO.HIGH)
    GPIO.output(motor1_in2_pin, GPIO.LOW)
    motor1_pwm.ChangeDutyCycle(duty_cycle)

def motor1_backward(duty_cycle):
    GPIO.output(motor1_in1_pin, GPIO.LOW)
    GPIO.output(motor1_in2_pin, GPIO.HIGH)
    motor1_pwm.ChangeDutyCycle(duty_cycle)

def motor2_forward(duty_cycle):
    GPIO.output(motor2_in1_pin, GPIO.HIGH)
    GPIO.output(motor2_in2_pin, GPIO.LOW)
    motor2_pwm.ChangeDutyCycle(duty_cycle)

def motor2_backward(duty_cycle):
    GPIO.output(motor2_in1_pin, GPIO.LOW)
    GPIO.output(motor2_in2_pin, GPIO.HIGH)
    motor2_pwm.ChangeDutyCycle(duty_cycle)

def motor1_speed_test(duty_cycle=0):
    duty_cycle = 0
    while True:
        print(duty_cycle)
        GPIO.output(motor1_in1_pin, GPIO.LOW)
        GPIO.output(motor1_in2_pin, GPIO.HIGH)
        GPIO.output(motor2_in1_pin, GPIO.HIGH)
        GPIO.output(motor2_in2_pin, GPIO.LOW) 
        motor1_pwm.ChangeDutyCycle(duty_cycle)
        motor2_pwm.ChangeDutyCycle(duty_cycle)
        vari = input("Input")
        duty_cycle = duty_cycle + 5
        if vari == "e":
            break

motor1_speed_test()

print("Example: Both motors forward")
motor1_forward(50)
motor2_forward(50)
input("Enter")

print("Example: Stop both motors")
motor1_pwm.ChangeDutyCycle(0)
motor2_pwm.ChangeDutyCycle(0)
input("Enter")

print("Example: Both motors backward")
motor1_backward(50)
motor2_backward(50)
input("Enter")

print("Stop the PWMs and reset the GPIO pin configuration")
motor1_pwm.stop()
motor2_pwm.stop()
GPIO.cleanup()
