import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set the email parameters
sender = "sender@example.com"
recipient = "recipient@example.com"
subject = "Report"
body = "Here is the report you requested."

# Create the email message
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Set the SMTP server and login credentials
smtp_server = "smtp.example.com"
username = "username"
password = "password"

# Connect to the SMTP server and send the email
server = smtplib.SMTP(smtp_server)
server.starttls()
server.login(username, password)
server.sendmail(sender, recipient, msg.as_string())
server.quit()

print("Email sent successfully.")
