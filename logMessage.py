from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2
import time
from datetime import datetime

def logMessage(display, message):
        now = datetime.now().strftime("%H:%M:%S")
        display.config(state=NORMAL)
        display.insert(INSERT, message + " - " + now + "\n")
        display.see(INSERT)
        display.config(state=DISABLED)