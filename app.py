import os
import requests
import time
import schedule
from flask import Flask
import logging

app = Flask(__name__)

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
            response = requests.get(url, timeout=10)
            logging.info(f"Request to {url} completed with status code: {response.status_code}")
        except Exception as e:
            logging.error(f"An error occurred for {url}: {e}")

# Schedule the function to run every 2 minutes
schedule.every(2).minutes.do(hit_websites)

# Background scheduler
def run_scheduler():
    while True:
        logging.info("Scheduler is running...")
        schedule.run_pending()
        time.sleep(10)

# Flask route
@app.route("/")
def home():
    return "Website monitor is running!"

if __name__ == "__main__":
    from threading import Thread
    # Run the scheduler in a separate thread
    scheduler_thread = Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()

    # Run Flask app
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
