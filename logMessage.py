from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2
import time
import globals
from datetime import datetime

# Used to write strings to the debug log of the GUI
# Saves many lines of code
def logMessage(display, message):
        now = datetime.now().strftime("%H:%M:%S")
        display.config(state=NORMAL)
        display.insert(INSERT, message + " - " + now + "\n")
        display.see(INSERT)
        display.config(state=DISABLED)

# Handles controller input event listener and prints to debug log for GUI
# Weird implementation, might be worth refactoring
def printThreadMessage(display_thread):
        if (len(globals.thread_string) > 0):
                logMessage(display_thread, globals.thread_string)
                globals.thread_string = ""