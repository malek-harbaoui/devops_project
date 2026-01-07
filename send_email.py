import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# CONFIGURATION
SMTP_SERVER = "smtp.gmail.com"      # Use your SMTP server
SMTP_PORT = 587                     # Usually 587 for TLS
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Use an App Password if using Gmail
RECIPIENT_EMAIL = "dev_team@example.com"
SUBJECT = "Automated Test Report"

# Read HTML report
with open("reports/test-report.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Create email
msg = MIMEMultipart("alternative")
msg["From"] = SENDER_EMAIL
msg["To"] = RECIPIENT_EMAIL
msg["Subject"] = SUBJECT
msg.attach(MIMEText(html_content, "html"))

# Send email
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)
server.send_message(msg)
server.quit()

print("Email sent successfully!")
