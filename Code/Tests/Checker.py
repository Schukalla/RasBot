#!/usr/bin/env python3

import psutil
import subprocess
import time

def start_script(script_path):
    print("start {}".format(script_path))
    subprocess.Popen(['python', script_path])

if __name__ == "__main__":
    script_path = "/home/pi/test3/Raspbot.py"  
    process_name = ['python', '/home/pi/test3/Raspbot.py']  
    
    
    flag_process_found = False
    i = 0
    while True:
        
        for process in psutil.process_iter():
           if process.cmdline() == process_name:
              print("found")
              flag_process_found = True
              break
           else:
              flag_process_found = False
        if flag_process_found == False:
          start_script(script_path) 
        i += 1
        time.sleep(10)  # Adjust interval if necessary
