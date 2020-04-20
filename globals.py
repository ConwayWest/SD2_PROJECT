def initialize():
    # Used to track whether machine is on or not
    global machine_power
    # Used to track whether machine lights are on or not
    global light_power
    # Used to switch rear camera filters
    global vid_view
    # Used to track whether program is on or not
    global program_power
    # Used for controller input strings
    global thread_string

    machine_power = False
    light_power = False
    vid_view = 1
    program_power = True
    thread_string = ""