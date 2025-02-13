import requests
import time
import schedule
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# List of websites to hit
urls = [
    "https://greenyield.onrender.com",
    "https://greenguardian.onrender.com",
    "https://likeme-backend-fxrs.onrender.com/api/portfolio/count",
    "https://snapurls.onrender.com",
    "https://snappedurl.onrender.com/temp"
]

# Function to hit multiple websites
def hit_websites():
    for url in urls:
        try:
            # Send the HTTP GET request with a timeout
            response = requests.get(url, timeout=10)
            logging.info(f"Request to {url} completed with status code: {response.status_code}")
        except requests.exceptions.Timeout:
            logging.error(f"Request to {url} timed out.")
        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred for {url}: {e}")

# Schedule the function to run every 2 minutes
schedule.every(2).minutes.do(hit_websites)

logging.info("Script started. Hitting the websites every 2 minutes...")

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
