from dotenv import load_dotenv
load_dotenv()

import os

# configuration details
DRIVER_LOCATION = './chromedriver'
BASE_URL = os.getenv("BASE_URL")
HEADLESS = os.getenv("HEADLESS")

config = {
    "DRIVER_LOCATION": DRIVER_LOCATION,
    "BASE_URL": BASE_URL,
    "HEADLESS": HEADLESS
}