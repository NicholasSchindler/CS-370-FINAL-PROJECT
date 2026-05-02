from datetime import datetime
import threading
import os

sensor_height = 0
SWE_constant = 1
status = ""

def get_sensor_height():
    temp = input("Enter the sensor height: ")
    try:
        value = float(temp)
        if value > 0:
            sensor_height = value
            print(f"Sensor height successfully set to: {sensor_height}")
            return True
        else:
            print("Invalid input. Sensor height must be a positive number.")
            return False
    except ValueError:
        print("Invalid input. Sensor height must be a positive number.")
        return False

def calc_depth(distance):
    return sensor_height - distance

def calc_SWE(depth):
    return depth * SWE_constant

def get_status(SWE):
    if SWE < 0.5:
        return "LOW"
    elif SWE < 1.5:
        return "NORMAL"
    else:
        return "HIGH"

def get_current_status(depth, SWE, log_file):
    temp_status = get_status(SWE)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] Depth: {str(depth)} in, SWE: {str(SWE)} in, Status: {temp_status}\n")
    if temp_status != status:
        with open(log_file, 'a') as f:
            f.write(f"[{timestamp}] ---------- NEW STATUS ----------\n")
        print("Status changed from " + status + " to " + temp_status)
        status = temp_status
    return status  

def main():
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),f'snow_log_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt')
    if get_sensor_height() == False:
        return -1
    with open(log_file, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] ---------- START OF SNOW LOG ----------\n")

    stop_event = threading.Event()

    def wait_for_enter():
        input()
        stop_event.set()

    listener_thread = threading.Thread(target=wait_for_enter, daemon=True)
    listener_thread.start()

    print("Monitoring snow levels, press Enter to stop...")
    while not stop_event.is_set():
        # distance = insert method to fetch distance to from sensor to snow
        # depth = calc_depth(distance)
        # SWE = calc_SWE(depth)
        # get_current_status(depth, SWE, log_file)
        stop_event.wait(timeout=60)

    with open(log_file, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] ---------- END OF SNOW LOG ----------\n")
    print("\nStopped by user. Log file name is: " + log_file)

if __name__ == "__main__":
    main()