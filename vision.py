from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2
import time
import globals
from logMessage import *
from toggleButtons import *

def switch_vid_view(display_log):
    if (globals.vid_view == 1):
        globals.vid_view = 2
    else:
        globals.vid_view = 1

    logMessage(display_log, "Rear video switched")
    

class MyVideoCaptureFront:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self, frame_view):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # sobel = cv2.Sobel(greyFrame, cv2.CV_64F, 1, 1, 5)
            edges = cv2.Canny(greyFrame, 50, 50)
            
            if ret and frame_view == 0:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            elif ret and frame_view == 1:
                return (ret, cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
            elif ret and frame_view == 2:
                contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                cv2.drawContours(frame, contours, -1, (0,0,255), 2)
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

class MyVideoCaptureBack:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # sobel = cv2.Sobel(greyFrame, cv2.CV_64F, 1, 1, 5)
            edges = cv2.Canny(greyFrame, 50, 50)

            if ret and globals.vid_view == 0:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
            elif ret and globals.vid_view == 1:
                return (ret, cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
            elif ret and globals.vid_view == 2:
                contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                cv2.drawContours(frame, contours, -1, (0,0,255), 2)
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
