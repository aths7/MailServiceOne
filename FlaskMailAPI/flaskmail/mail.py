# Python script to send mail using Gmail
import smtplib
from email.message import EmailMessage

SENDING_EMAIL_ADDRESS = ""
SENDING_EMAIL_PASSWORD = ""


def send_gmail(email_address, email_subject, email_body):
    print("Setting mail information")
    message = EmailMessage()
    message['From'] = SENDING_EMAIL_ADDRESS
    message['Subject'] = email_subject
    message['To'] = email_address
    message.set_content(email_body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDING_EMAIL_ADDRESS, SENDING_EMAIL_PASSWORD)
        smtp.send_message(message)
        print("Mail sent!")

    return
