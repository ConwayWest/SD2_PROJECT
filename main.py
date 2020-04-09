from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2
import time

class SimpleApp(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        gas_gauge = Label(self, anchor="center", bg="green", text="GAS GAUGE")
        gas_gauge.grid(column=0, row=0, sticky='EWNS')

        front_video = Canvas(self)
        front_video.grid(column=1, row=0, sticky='EWNS')

        laser_level = Label(self, anchor="center", bg="red", text="LASER LEVEL")
        laser_level.grid(column=2, row=0, sticky='EWNS')

        battery_gauge = Label(self, anchor="center", bg="purple", text="BATTERY GAUGE")
        battery_gauge.grid(column=0, row=1, sticky='EWNS')

        back_video = Canvas(self)
        back_video.grid(column=1, row=1, sticky='EWNS')

        input_graph = Label(self, anchor="center", bg="yellow", text="GRAPHED INPUT")
        input_graph.grid(column=2, row=1, sticky='EWNS')

        start_button = Button(self, anchor="center", bg="green", text="Power Toggle")
        start_button.grid(column=0, row=2, sticky='EWNS')

        controller_input = Label(self, anchor="center", bg="orange", text="CONTROLLER INPUT")
        controller_input.grid(column=1, row=2, sticky='EWNS')

        light_button = Button(self, anchor="center", bg="red", text="TOGGLE LIGHTS")
        light_button.grid(column=2, row=2, sticky='EWNS')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def update(self):
        dog = 12


if __name__ == "__main__":
    root = SimpleApp(None)
    root.title("Dirt Smoother Interface")
    screen_width = int(root.winfo_screenwidth() / 2)
    screen_height = int(root.winfo_screenheight() / 2)
    root.geometry(str(screen_width) + "x" + str(screen_height))
    root.mainloop()
