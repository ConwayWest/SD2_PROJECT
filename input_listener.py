import inputs
from logMessage import *
from tkinter import *
import time
import globals

# Used to listen for controller input
# Has some edge case issues (shutdown process in main)
# Worth looking into
def listener(display_log):
    pad = inputs.devices.gamepads
    controller_connected = False

    while len(pad) == 0:
        logMessage(display_log, "MISSING CONTROLLER! PLEASE CONNECT A CONTROLLER AND RESTART THE PROGRAM")
        time.sleep(5)
        pad = inputs.devices.gamepads

    while(True):
        events = inputs.get_gamepad()
        for event in events:
            globals.thread_string = str(event.code) + " " + str(event.state)
            printThreadMessage(display_log)
            if (globals.program_power == False):
                break
        if (globals.program_power == False):
            exit()