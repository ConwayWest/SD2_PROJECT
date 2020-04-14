from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2
import time
import globals
from logMessage import *
from toggleButtons import *
from vision import *

class SimpleApp(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        input_display = Text(self)
        self.vid_source_front = 0
        self.vid_source_rear = 0
        self.initialize(input_display)

    def initialize(self, display):
        globals.initialize()
        self.video_front = MyVideoCaptureFront(self.vid_source_front)
        # self.video_back = MyVideoCaptureBack(self.vid_source_rear)
        self.grid()

        gas_gauge = Label(self, anchor="center", bg="black", fg="red", text="GAS GAUGE\n DELAYED", bd=5)
        gas_gauge.grid(column=0, row=0, sticky='EWNS')

        self.front_video_display = Canvas(self)
        self.front_video_display.grid(column=1, row=0, sticky='EWNS')

        laser_level = Label(self, anchor="center", bg="black", fg="red", text="LASER LEVEL\n DELAYED", bd=5)
        laser_level.grid(column=2, row=0, sticky='EWNS')

        battery_gauge = Label(self, anchor="center", bg="black", fg="red", text="BATTERY GAUGE\n DELAYED", bd=5)
        battery_gauge.grid(column=0, row=1, sticky='EWNS')

        self.back_video_display = Canvas(self)
        self.back_video_display.grid(column=1, row=1, sticky='EWNS')
        self.back_video_button = Button(self, anchor="center", text="SWITCH VIDEO", command=lambda: switch_vid_view(display))
        self.back_video_button.grid(column=1, row=1, sticky='S')


        input_graph = Label(self, anchor="center", bg="black", fg="red", text="GRAPHED INPUT\n DELAYED", bd=5)
        input_graph.grid(column=2, row=1, sticky='EWNS')

        start_button = Button(self, anchor="center", bg="red", text="TOGGLE POWER", bd=5, command=lambda: togglePower(display, start_button))
        start_button.grid(column=0, row=2, sticky='EWNS')

        display.config(bg="black", fg="grey", state=DISABLED, bd=5, height=int(self.front_video_display.winfo_height() / 2))
        display.grid(column=1, row=2, sticky='EWNS')

        logMessage(display, "Welcome to the Dirt Smoother Interface!")

        light_button = Button(self, anchor="center", bg="red", text="TOGGLE LIGHTS", bd=5, command=lambda: toggleLights(display, light_button))
        light_button.grid(column=2, row=2, sticky='EWNS')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.delay = 15
        self.update()

    def update(self):
        ret, frame = self.video_front.get_frame(0)
        ret2, frame2 = self.video_front.get_frame(globals.vid_view)
        
        if ret:
            img = cv2.resize(frame, (int(self.front_video_display.winfo_width()), int(self.front_video_display.winfo_height())))
            self.photo_front = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img))
            self.front_video_display.create_image(0, 0, image = self.photo_front, anchor = NW)

        if ret2:
            img2 = cv2.resize(frame2, (int(self.back_video_display.winfo_width()), int(self.back_video_display.winfo_height())))
            self.photo_back = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img2))
            self.back_video_display.create_image(0, 0, image = self.photo_back, anchor = NW)
        
        self.after(self.delay, self.update)
        
        

if __name__ == "__main__":
    root = SimpleApp(None)
    root.title("Dirt Smoother Interface")
    screen_width = int(root.winfo_screenwidth() / 1.5)
    screen_height = int(root.winfo_screenheight() / 1.5)
    root.geometry(str(screen_width) + "x" + str(screen_height))
    root.mainloop()
