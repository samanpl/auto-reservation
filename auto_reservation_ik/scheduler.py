import time
from auto_reservation_ik.utils.logger import log

def wait_until(target_time_str):
    """
    Waits until the target time (HH:MM format).
    """
    target_hour, target_minute = map(int, target_time_str.split(":"))

    log(f"Waiting until {target_time_str} to book...")

    while True:
        now = time.localtime()
        if now.tm_hour == target_hour and now.tm_min == target_minute:
            log("Target time reached.")
            break
        time.sleep(10)  # Check every 10 seconds
