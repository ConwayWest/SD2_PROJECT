from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2, time
import globals
from logMessage import *
from toggleButtons import *
from vision import *
from input_listener import *
from threading import Thread
from multiprocessing import Process

# Main script is in charge of creating GUI as well as
# hooking up UI to various project components
# For next group: Feel free to email me at kyleconway@rocketmail.com
# Also feel free to message me on LinkedIn for advice, my name is Kyle Conway

class SimpleApp(Tk):
    # Initializes Python object
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.input_display = Text(self)
        self.vid_source_front = 0
        self.vid_source_rear = 0
        self.initialize(self.input_display)

    # Initializes tkinter GUI
    def initialize(self, display):
        globals.initialize()

        # Due to COVID-19 our project was understandably down-scoped
        # only had access to a single video source (webcam) hence why there is
        # only one video capture, will need to change this to access both cameras
        self.video_front = MyVideoCaptureFront(self.vid_source_front)
        # self.video_back = MyVideoCaptureBack(self.vid_source_rear)
        
        self.grid()

        # Needs to be implemented/built
        gas_gauge = Label(self, anchor="center", bg="black", fg="red", text="GAS GAUGE\n DELAYED", bd=5)
        gas_gauge.grid(column=0, row=0, sticky='EWNS')

        # Mostly setup, just needs to have correct video source
        self.front_video_display = Canvas(self)
        self.front_video_display.grid(column=1, row=0, sticky='EWNS')

        # Needs to be implemented/built - consult ME side as
        # they are the experts in this area
        laser_level = Label(self, anchor="center", bg="black", fg="red", text="LASER LEVEL\n DELAYED", bd=5)
        laser_level.grid(column=2, row=0, sticky='EWNS')

        # Needs to be implemented/built
        battery_gauge = Label(self, anchor="center", bg="black", fg="red", text="BATTERY GAUGE\n DELAYED", bd=5)
        battery_gauge.grid(column=0, row=1, sticky='EWNS')

        # Mostly setup, needs to have correct video source (rear)
        # as well as dialed in for best visual of dirt
        # Rear = IR Camera = better viewing regardless of light
        self.back_video_display = Canvas(self)
        self.back_video_display.grid(column=1, row=1, sticky='EWNS')

        # Just switches rear video filtering from canny edge to contouring and back
        self.back_video_button = Button(self, anchor="center", text="SWITCH VIDEO", command=lambda: switch_vid_view(display))
        self.back_video_button.grid(column=1, row=1, sticky='S')

        # Needs to be built/implemented - ME ask
        # Visual representation of movement input, think a graph arrow
        # whose magnitude is scaled by how far user is inputting forward/back/left/right
        input_graph = Label(self, anchor="center", bg="black", fg="red", text="GRAPHED INPUT\n DELAYED", bd=5)
        input_graph.grid(column=2, row=1, sticky='EWNS')

        # Setup fine, just needs networking (as does most of the project)
        start_button = Button(self, anchor="center", bg="red", text="TOGGLE POWER", bd=5, command=lambda: togglePower(display, start_button))
        start_button.grid(column=0, row=2, sticky='EWNS')

        # This is your debug log essentially in the bottom center
        # , currently communicates user inputs
        display.config(bg="black", fg="grey", state=DISABLED, bd=5, height=int(self.front_video_display.winfo_height() / 2))
        display.grid(column=1, row=2, sticky='EWNS')

        # Function used to write to debug log, saves quite a few lines of codes like this
        logMessage(display, "Welcome to the Dirt Smoother Interface!")

        # Setup fine, just needs networking (as does most of the project)
        light_button = Button(self, anchor="center", bg="red", text="TOGGLE LIGHTS", bd=5, command=lambda: toggleLights(display, light_button))
        light_button.grid(column=2, row=2, sticky='EWNS')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # delay in ms, used for updating video feeds
        self.delay = 15
        self.update()
        
        # listener thread is for event listener for controller input
        self.listener_thread = Thread(target = listener, args =(display, ))
        self.listener_thread.start()

    def update(self):
        ret, frame = self.video_front.get_frame(0)
        ret2, frame2 = self.video_front.get_frame(globals.vid_view)
        
        # Front camera
        if ret:
            img = cv2.resize(frame, (int(self.front_video_display.winfo_width()), int(self.front_video_display.winfo_height())))
            self.photo_front = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img))
            self.front_video_display.create_image(0, 0, image = self.photo_front, anchor = NW)

        # Rear camera
        if ret2:
            img2 = cv2.resize(frame2, (int(self.back_video_display.winfo_width()), int(self.back_video_display.winfo_height())))
            self.photo_back = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img2))
            self.back_video_display.create_image(0, 0, image = self.photo_back, anchor = NW)
        
        # Loop
        self.after(self.delay, self.update)

    # Shutdown sequence when user closes window
    # Releases video and closes thread - though has an edge case
    # controller input event listener will close on its next event
    # so if controller is plugged in and user closes you might notice
    # the console window still open. Jiggle the controller joystick and it'll shutdown
    # dumb problem just don't have time to fix
    def _close_thread(self):
        globals.program_power = False
        self.video_front.vid.release()
        root.destroy()
        exit()
        
        
# Instantiates GUI object
if __name__ == "__main__":
    root = SimpleApp(None)
    root.title("Dirt Smoother Interface")
    screen_width = int(root.winfo_screenwidth() / 1.5)
    screen_height = int(root.winfo_screenheight() / 1.5)
    root.geometry(str(screen_width) + "x" + str(screen_height))
    root.protocol("WM_DELETE_WINDOW", root._close_thread)
    root.mainloop()
    