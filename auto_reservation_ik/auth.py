import requests
from bs4 import BeautifulSoup
from auto_reservation_ik import config
from auto_reservation_ik.utils.logger import log

def authenticate():
    log("Authenticating...")

    session = requests.Session()
    response = session.get(config.SERVICE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    payload = {
        "UName": config.USERNAME,
        "Passwordfield": config.PASSWORD,
    }
    
    
    login_response = session.post(config.SERVICE_URL, data=payload)
    
    # Simulating an API authentication (POST request)
    response = requests.post(f"{config.SERVICE_URL}/login", data=payload)

    if response.status_code == 200:
        print('we got a response code 200!')
        with open('result.html', 'w', encoding='utf-8') as file:
            file.write(response.text)

    if "خروج از سیستم" in login_response.text:
        print("Login successful!")
    else:
        print("Login failed.")

    # if response.status_code == 200:
    #     log("Authentication successful.")
    #     return response.json().get("token")
    # else:
    #     log(f"Authentication failed: {response.status_code} {response.text}")
    #     raise Exception("Authentication failed")
