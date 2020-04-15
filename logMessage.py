from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2
import time
import globals
from datetime import datetime

def logMessage(display, message):
        now = datetime.now().strftime("%H:%M:%S")
        display.config(state=NORMAL)
        display.insert(INSERT, message + " - " + now + "\n")
        display.see(INSERT)
        display.config(state=DISABLED)

def printThreadMessage(display_thread):
        if (len(globals.thread_string) > 0):
                logMessage(display_thread, globals.thread_string)
                globals.thread_string = ""