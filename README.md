# CV Email Sender

A simple Python script that reads a list of company emails from a CSV file and automatically sends your CV to all of them via Gmail.

---

## Files

| File | Description |
|------|-------------|
| `send_emails.py` | The main script |
| `companies.csv` | List of company emails |
| `cv.pdf` | Your CV file (you provide this) |

---

## Requirements

- Python 3.x
- A Gmail account with an App Password

No third-party libraries needed. The script uses only Python built-in modules: `smtplib`, `csv`, `time`, `email`, `os`.

---

## Setup

**1.** Download all files into the same folder.

**2.** Place your CV in the same folder and rename it to `cv.pdf`, or update the path in the script.

**3.** Open `send_emails.py` and edit the config section at the top:

```python
SENDER_EMAIL    = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password_here"
YOUR_NAME       = "Your Full Name"
CV_FILE_PATH    = "cv.pdf"
```

---

## Gmail App Password

Gmail does not allow normal passwords for scripts. You need to generate an App Password:

1. Go to myaccount.google.com/security
2. Enable 2-Step Verification
3. Go to myaccount.google.com/apppasswords
4. Create a new App Password and name it Mail
5. Copy the 16-character code and paste it as `SENDER_PASSWORD` in the script with no spaces

---

The script will go through each email in `companies.csv`, send the email with your CV attached, and print the result for each one.

---

## Adding or Removing Emails

Open `companies.csv` in any text editor or Excel. The file has one column called `email`. Add or remove addresses as needed, one per line.

---

## Notes

- The script adds a 2-second delay between each email to avoid being flagged as spam.
- If an email address no longer exists or the server rejects it, the script will log it as failed and continue to the next one.
- Bounced emails are normal for old email lists and are not a bug in the script.

---

## Customizing the Message

Open `send_emails.py` and edit the `EMAIL_SUBJECT` and `EMAIL_BODY` variables at the top of the file to change the subject line and message body.