# LinkedIn Automated Backup Script

## Overview

This script automates the process of logging into LinkedIn, requesting your data archive, and sending notifications when the archive is ready. It also saves your login session to avoid repeated logins. The process is automated to run at regular intervals (default: every 14 days). The script sends notifications via email or SMS in case of errors, such as expired cookies or failed downloads.

## Features

- **Automated Login**: Logs into LinkedIn and saves session cookies.
- **Data Backup**: Requests LinkedIn data archive and downloads it once available.
- **Notification System**: Sends email or SMS notifications on errors.
- **Scheduled Execution**: Runs at regular intervals (default every 14 days).
- **Cloud Deployment**: Can be deployed on cloud servers like AWS, Google Cloud.

## Prerequisites

Make sure you have the following installed:

1. **Python 3.8+**
2. **Google Chrome**
3. **Chromedriver** compatible with your version of Google Chrome
4. A valid **LinkedIn account** with credentials
5. An **SMTP** or **Twilio** account for sending email/SMS notifications

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/<your-username>/linkedin-backup-script.git
cd linkedin-backup-script
```

### Step 2: Install Dependencies
Install all required Python dependencies:


```bash
pip install -r requirements.txt
```

### Step 3: Configure LinkedIn Login Credentials
In the linkedin_backup.py file, set your LinkedIn credentials:

```
LINKEDIN_USERNAME = "your_email@example.com"
LINKEDIN_PASSWORD = "your_password"
Replace your_email@example.com and your_password with your LinkedIn login details.
 ```

### Step 4: Configure Notification Settings
You can choose to receive notifications via email or SMS.

Email Notifications (via SMTP):
Set up email notifications in linkedin_backup.py:

```
NOTIFICATION_EMAIL = "your_email@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your_smtp_user"
SMTP_PASS = "your_smtp_password"

```
NOTIFICATION_EMAIL: Your email address.
SMTP_SERVER: SMTP server address (e.g., smtp.gmail.com).
SMTP_PORT: The SMTP server port (usually 587 for Gmail).
SMTP_USER: Your email address.
SMTP_PASS: Your email password or an app-specific password.
SMS Notifications (via Twilio):
For SMS notifications, configure Twilio settings:


```
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
YOUR_PHONE_NUMBER = "your_personal_phone_number"
```

TWILIO_ACCOUNT_SID: Your Twilio Account SID.
TWILIO_AUTH_TOKEN: Your Twilio Auth Token.
TWILIO_PHONE_NUMBER: Your Twilio phone number.
YOUR_PHONE_NUMBER: Your phone number to receive SMS alerts.

### Step 5: Set the Backup Interval
Set the backup interval in days. The default is 14 days, but you can change it by modifying the BACKUP_INTERVAL_DAYS variable:
```
BACKUP_INTERVAL_DAYS = 14  # Modify this value for your preferred interval
```
### Step 6: Set Up Chromedriver
Make sure Chromedriver is installed and compatible with your version of Google Chrome. You can download it from Chromedriver.

If Chromedriver is not globally accessible, specify the path in the script:

```
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
```
Running the Script



### Step 7: Run the Script Manually
You can run the script manually by executing:
```
python linkedin_backup.py
```
What happens when you run the script?
The script checks for existing cookies. If none are found, it will log you into LinkedIn.
Once logged in, the cookies will be saved for future use.
The script will request your LinkedIn data archive.
After 24 hours (or your set interval), the script will attempt to download the archive.
You will receive notifications once the archive is ready or if any errors occur.


### Step 8: Schedule the Script for Regular Execution
The script uses the schedule library to run automatically at set intervals (every 14 days by default). To modify the interval, update the following line in the script:

```
schedule.every(14).days  # Modify the interval in days as needed
Deployment
```
### Step 9: Deploying on Cloud Servers (AWS, Google Cloud, etc.)
You can deploy the script on a cloud server. Follow these steps:

Set Up VPS: Create a VPS instance with your chosen cloud provider.
Install Dependencies: Follow the installation steps from Step 2.
Run the Script Continuously: Use tools like screen or tmux to run the script in the background.
Set Auto-Start: Use cron or systemd to set the script to run at startup.


