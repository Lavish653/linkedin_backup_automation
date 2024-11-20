from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
import smtplib
from email.mime.text import MIMEText
import schedule
from twilio.rest import Client

# --- Configuration ---
LINKEDIN_USERNAME = "your_email@example.com"  # Replace with your LinkedIn email
LINKEDIN_PASSWORD = "your_password"          # Replace with your LinkedIn password
CHROMEDRIVER_PATH = "/path/to/chromedriver"  # Update this with the ChromeDriver path
BACKUP_INTERVAL_DAYS = 14  # Schedule backups every 14 days

# Notification settings (email)
NOTIFICATION_EMAIL = "your_email@example.com"  # Replace with your email for notifications
SMTP_SERVER = "smtp.example.com"              # e.g., smtp.gmail.com
SMTP_PORT = 587
SMTP_USER = "your_email_username"
SMTP_PASS = "your_email_password"

# Twilio settings (optional)
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
YOUR_PHONE_NUMBER = "your_personal_phone_number"

# --- Helper Functions ---
def send_email_notification(subject, body):
    """Send an email notification."""
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SMTP_USER
        msg["To"] = NOTIFICATION_EMAIL
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, NOTIFICATION_EMAIL, msg.as_string())
        print(f"Email notification sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def send_sms_notification(body):
    """Send an SMS notification (optional)."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            to=YOUR_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            body=body
        )
        print("SMS notification sent.")
    except Exception as e:
        print(f"Failed to send SMS: {e}")


def linkedin_login(driver):
    """Logs into LinkedIn and saves cookies."""
    driver.get("https://www.linkedin.com/login")
    try:
        driver.find_element(By.ID, "username").send_keys(LINKEDIN_USERNAME)
        driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Wait for manual OTP or CAPTCHA
        input("Complete OTP or CAPTCHA and press Enter...")

        # Save cookies
        pickle.dump(driver.get_cookies(), open("linkedin_cookies.pkl", "wb"))
        print("Login successful, cookies saved.")
    except Exception as e:
        send_email_notification("LinkedIn Login Failed", f"Error: {e}")
        send_sms_notification(f"LinkedIn Login Failed: {e}")


def load_cookies(driver):
    """Loads cookies for LinkedIn."""
    try:
        cookies = pickle.load(open("linkedin_cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("Cookies loaded successfully.")
    except FileNotFoundError:
        print("No cookies found. Login required.")


def request_data_download(driver):
    """Requests LinkedIn data archive."""
    try:
        driver.get("https://www.linkedin.com/mypreferences/d/download-my-data")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='complete-archive']"))
        ).click()
        driver.find_element(By.XPATH, "//button[contains(text(),'Request archive')]").click()
        print("Data download requested.")
    except Exception as e:
        send_email_notification("Data Download Request Failed", f"Error: {e}")
        send_sms_notification(f"Data Download Request Failed: {e}")


def download_data(driver):
    """Downloads LinkedIn data archive."""
    try:
        driver.get("https://www.linkedin.com/mypreferences/d/download-my-data")
        download_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Download archive')]"))
        )
        download_link.click()
        print("Data archive downloaded successfully.")
    except Exception as e:
        send_email_notification("Data Download Failed", f"Error: {e}")
        send_sms_notification(f"Data Download Failed: {e}")


def initiate_backup():
    """Main backup process."""
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    try:
        driver.get("https://www.linkedin.com")
        try:
            load_cookies(driver)
            driver.refresh()
        except:
            linkedin_login(driver)

        request_data_download(driver)

        # Wait 24 hours for LinkedIn to process the archive
        print("Waiting 24 hours for archive preparation...")
        time.sleep(86400)

        download_data(driver)
    finally:
        driver.quit()


# --- Scheduling ---
schedule.every(BACKUP_INTERVAL_DAYS).days.do(initiate_backup)

if __name__ == "__main__":
    print("Starting LinkedIn backup automation...")
    while True:
        schedule.run_pending()
        time.sleep(60)
