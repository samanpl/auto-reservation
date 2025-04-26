import requests
from auto_reservation_ik import config
from auto_reservationik.utils.logger import log

def book_service(auth_token):
    log("Booking the service...")

    headers = {
        "Authorization": f"Bearer {auth_token}",
    }

    payload = {
        "service_id": "12345",  # You can make this dynamic later
        "time_slot": "09:00",   # Example time slot
    }

    response = requests.post(f"{config.SERVICE_URL}/book", headers=headers, json=payload)

    if response.status_code == 201:
        log("Service booked successfully!")
    else:
        log(f"Booking failed: {response.status_code} {response.text}")
        raise Exception("Booking failed")
