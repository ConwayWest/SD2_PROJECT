from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2
import time

machine_power = False
light_power = False

class SimpleApp(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def togglePower(self, display):
        global machine_power

        if machine_power == False:
            # Registers user input to begin start power process
            display.config(state=NORMAL)
            display.insert(INSERT, "Machine starting up now...\n")
            display.see(INSERT)
            display.config(state=DISABLED)

            # Once machine actually turns on
            display.config(state=NORMAL)
            display.insert(INSERT, "Machine now turned on!\n")
            display.see(INSERT)
            display.config(state=DISABLED)

            # Set machine power state to true
            machine_power = True
        elif machine_power == True:
            # Registers user input to begin shutdown power process
            display.config(state=NORMAL)
            display.insert(INSERT, "Machine shutting down now...\n")
            display.see(INSERT)
            display.config(state=DISABLED)

            # Once machine actually turns off
            display.config(state=NORMAL)
            display.insert(INSERT, "Machine now turned off!\n")
            display.see(INSERT)
            display.config(state=DISABLED)

            # Set machine power state to false
            machine_power = False

    def toggleLights(self, display):
        global light_power

        if light_power == False:
            # Registers user input to begin turn on lights
            display.config(state=NORMAL)
            display.insert(INSERT, "Lights On\n")
            display.see(INSERT)
            display.config(state=DISABLED)

            # Set light power state to true
            light_power = True
        elif light_power == True:
            # Registers user input to begin shutdown lights
            display.config(state=NORMAL)
            display.insert(INSERT, "Lights Off\n")
            display.see(INSERT)
            display.config(state=DISABLED)

            # Set light power state to true
            light_power = False
        

    def initialize(self):
        self.grid()

        gas_gauge = Label(self, anchor="center", bg="black", fg="red", text="GAS GAUGE\n DELAYED", bd=5)
        gas_gauge.grid(column=0, row=0, sticky='EWNS')

        front_video = Canvas(self, bd=5)
        front_video.grid(column=1, row=0, sticky='EWNS')

        laser_level = Label(self, anchor="center", bg="black", fg="red", text="LASER LEVEL\n DELAYED", bd=5)
        laser_level.grid(column=2, row=0, sticky='EWNS')

        battery_gauge = Label(self, anchor="center", bg="black", fg="red", text="BATTERY GAUGE\n DELAYED", bd=5)
        battery_gauge.grid(column=0, row=1, sticky='EWNS')

        back_video = Canvas(self, bd=5)
        back_video.grid(column=1, row=1, sticky='EWNS')

        input_graph = Label(self, anchor="center", bg="black", fg="red", text="GRAPHED INPUT\n DELAYED", bd=5)
        input_graph.grid(column=2, row=1, sticky='EWNS')

        start_button = Button(self, anchor="center", bg="green", text="TOGGLE POWER", bd=5, command=lambda: self.togglePower(input_display))
        start_button.grid(column=0, row=2, sticky='EWNS')

        input_display = Text(self, bg="black", fg="grey", state=DISABLED, bd=5, height=int(back_video.winfo_height() / 2))
        input_display.grid(column=1, row=2, sticky='EWNS')

        input_display.config(state=NORMAL)
        input_display.insert(INSERT, "Welcome to the Dirt Smoother Interface!\n")
        input_display.see(INSERT)
        input_display.config(state=DISABLED)

        light_button = Button(self, anchor="center", bg="red", text="TOGGLE LIGHTS", bd=5, command=lambda: self.toggleLights(input_display))
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
