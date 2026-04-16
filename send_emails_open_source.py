import smtplib
import csv
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# ─────────────────────────────────────────────
#  ✏️  CONFIGURE THESE BEFORE RUNNING
# ─────────────────────────────────────────────

SENDER_EMAIL    = "your_email@gmail.com"       # Your Gmail address
SENDER_PASSWORD = "your_app_password_here"     # Gmail App Password (NOT your normal password)
YOUR_NAME       = "Your Full Name"             # Your name for the signature
CV_FILE_PATH    = "cv.pdf"                     # Path to your CV file (e.g. "cv.pdf" or "/home/user/cv.pdf")
CSV_FILE        = "companies.csv"              # Path to the CSV file with emails

EMAIL_SUBJECT   = "Job Application – Seeking a Professional Opportunity"

EMAIL_BODY = f"""Dear Hiring Manager,

I hope this message finds you well. I am writing to express my sincere interest in joining your esteemed organization.

After thorough research, I believe your company offers an excellent environment for professional growth. I am eager to contribute my skills and experience to your team.

Please find my CV attached for your kind consideration. I would be grateful for the opportunity to discuss how I can add value to your organization.

Thank you for your time, and I look forward to hearing from you.

Best regards,
{YOUR_NAME}
"""

# ─────────────────────────────────────────────
#  📨  SEND FUNCTION  (don't edit below)
# ─────────────────────────────────────────────

def send_email(sender, password, recipient, subject, body, cv_path):
    msg = MIMEMultipart()
    msg["From"]    = sender
    msg["To"]      = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Attach CV
    if cv_path and os.path.exists(cv_path):
        with open(cv_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f'attachment; filename="{os.path.basename(cv_path)}"'
        )
        msg.attach(part)
    else:
        print(f"  ⚠️  CV file not found at '{cv_path}' — sending without attachment.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())


def main():
    if not os.path.exists(CSV_FILE):
        print(f"❌  CSV file '{CSV_FILE}' not found. Make sure it's in the same folder.")
        return

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        emails = [row["email"].strip() for row in reader if row.get("email", "").strip()]

    print(f"📋  Found {len(emails)} emails in {CSV_FILE}")
    print(f"📎  CV file : {CV_FILE_PATH}")
    print(f"📤  Sender  : {SENDER_EMAIL}\n")
    print("─" * 50)

    success, failed = 0, []

    for i, email in enumerate(emails, 1):
        try:
            print(f"[{i}/{len(emails)}] Sending to {email} ...", end=" ")
            send_email(SENDER_EMAIL, SENDER_PASSWORD, email, EMAIL_SUBJECT, EMAIL_BODY, CV_FILE_PATH)
            print("✅ Sent")
            success += 1
            time.sleep(2)   # Small delay to avoid being flagged as spam
        except Exception as e:
            print(f"❌ Failed — {e}")
            failed.append((email, str(e)))

    print("\n" + "─" * 50)
    print(f"✅  Successfully sent : {success}")
    print(f"❌  Failed            : {len(failed)}")
    if failed:
        print("\nFailed addresses:")
        for addr, err in failed:
            print(f"  • {addr} → {err}")


if __name__ == "__main__":
    main()
