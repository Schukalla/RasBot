from motor import MotorController

class MotorControl:
    def __init__(self):
        self.motor_controller = MotorController()

    def motor(self, x, y):
        def check_value(val):
            if val < -100:
                return -100
            elif val > 100:
                return 100
            else:
                return val

        if y >= 0:
            v1 = y - x
            v2 = y + x
        else:
            v1 = y + x
            v2 = y - x
        v1 = check_value(v1)
        v2 = check_value(v2)
        self.motor_controller.motor(v1, v2, y)

    def cleanup(self):
        #GPIO.cleanup()
        self.motor_controller.cleanGPIO()

    def shutdown(self):
       self.motor_controller.shutdown()
