import requests
import time
import schedule

# List of websites to hit
urls = [
    "https://greenyield.onrender.com",
    "https://greenguardian.onrender.com",
    "https://likeme-backend-fxrs.onrender.com/api/portfolio/count",
  "https://snapurls.onrender.com",
  "https://snappedurl.onrender.com/temp"
]  # Add more URLs as needed

# Function to hit multiple websites
def hit_websites():
    for url in urls:
        try:
            response = requests.get(url)
            print(f"Request to {url} completed with status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred for {url}: {e}")

# Schedule the function to run every 10 minutes
schedule.every(2).minutes.do(hit_websites)

print("Script started. Hitting the websites every 10 minutes...")

while True:
    schedule.run_pending()
    time.sleep(1)
