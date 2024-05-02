from motor_control import MotorControl
from firebase_controller import FirebaseController
import time
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format the date as a string (in the format YYYY-MM-DD)
current_date_string = current_datetime.strftime("%Y-%m-%d")

print(current_date_string)

f = open("demofile2.txt", "a")
f.write("{}\n".format(current_date_string))
f.close()
###

if __name__ == "__main__":
    firebase = FirebaseController()
    motor_control = MotorControl()
    try:
        while True:
            x, y = firebase.get_direction()
            firebase.response()
            motor_control.motor(x, y)
            motor_control.shutdown()
    except:
        motor_control.cleanup()
        print("Cleaned GPIO")
