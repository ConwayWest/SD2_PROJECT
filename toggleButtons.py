from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2
import time
import globals
from logMessage import *

def togglePower(display, button):
    if globals.machine_power == False:
        # Registers user input to begin start power process
        logMessage(display, "Machine starting up now...")

        # Network code to go here

        # Once machine actually turns on
        logMessage(display, "Machine now turned on!")
        button.config(bg="green")

        # Set machine power state to true
        globals.machine_power = True
    elif globals.machine_power == True:
        # Registers user input to begin shutdown power process
        logMessage(display, "Machine shutting down now...")

        # Network code to go here

        # Once machine actually turns off
        logMessage(display, "Machine now turned off!")
        button.config(bg="red")

        # Set machine power state to false
        globals.machine_power = False

def toggleLights(display, button):

    if globals.light_power == False:
        # Network code to go here

        # Registers user input to begin turn on lights
        logMessage(display, "Lights On")
        button.config(bg="green")

        # Set light power state to true
        globals.light_power = True
    elif globals.light_power == True:
        # Network code to go here

        # Registers user input to begin shutdown lights
        logMessage(display, "Lights Off")
        button.config(bg="red")

        # Set light power state to true
        globals.light_power = False
        