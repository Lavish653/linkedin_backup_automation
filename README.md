# LinkedIn Automated Backup Script

## Overview
This Python script automates the process of periodically backing up your LinkedIn account data. It securely handles the login process, stores session cookies to avoid frequent logins, requests and downloads your archived data from LinkedIn, and sends notifications in case of errors such as expired cookies or failed downloads. 

---

## Features
- **Automated LinkedIn Login**: Logs in automatically and saves session cookies to avoid repetitive logins.
- **Data Backup**: Automatically requests a LinkedIn archive of your data and downloads it after 24 hours.
- **Notification System**: Sends email or SMS notifications in case of errors (e.g., login issues or download failures).
- **Periodic Scheduling**: Automatically runs every 2 weeks (configurable) using the `schedule` library.
- **Cloud-Ready**: Designed for deployment on cloud platforms or VPS servers to run continuously.

---

## Prerequisites

Before using the script, ensure you have the following:

1. **Python 3.8 or higher** installed on your system.
2. **Google Chrome** browser installed and accessible on your machine.
3. **Chromedriver** installed and accessible on your machine (make sure the version matches the version of Google Chrome you're using).
4. A **LinkedIn account** with valid login credentials.
5. **SMTP credentials** for sending email notifications, or a **Twilio account** for SMS notifications.

---

## Step-by-Step Setup

### 1. Clone the repository
   First, clone the repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/linkedin-backup-script.git
   cd linkedin-backup-script

