MakeFile
    make all: Compiles SnowPackMonitor.py.
    make run: Excecutes SnowPackMonitor.
    make clean: Deletes all compiled python files + all text files. Only works on windows.

SnowPackMonitor.py
    Infinite loop that monitors sensor, logs data, and prints alerts to terminal. Does not accept command line arguments.
    Methods:
        get_sensor_height(): Allows user to input the sensor height above the ground.
        calc_depth(distance): Takes in the measured distance of the sensor, returns the snow depth.
        calc_SWE(depth): Takes in the snow depth, and outputs SWE.
        get_status(SWE): Helper method to determine whether the SWE is at a healthy level.
        get_current_status(SWE, log_file): Takes in the SWE, and logs the result along with status to the log file. Prints to terminal if there is an alert.
        main(): Creates date and time stamped .txt file for logging. Stops running when user presses enter.