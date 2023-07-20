import smtplib
from email.message import EmailMessage
import os
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from utilities import utility
from utilities import writer
from mail.HtmlTemplate import HtmlTemplate


class MailBot:
    sender = "jarvismark01v@gmail.com"  # update this
    credential = "onrvwrkofhtuxqzl"  # update this
    # print(credential)

    def __init__(self, receiver=None, subject=None, message=None, full_name=None):
        self.receiver = receiver
        self.subject = subject
        self.message = message
        self.full_name = full_name

    def setReceiver(self, new_receiver):
        self.receiver = new_receiver

    def setSubject(self, new_subject):
        self.receiver = new_subject

    def setMessage(self, new_message):
        self.message = new_message

    # Normal text email
    def send_email(self):
        if self.receiver and self.subject and self.message:
            email = EmailMessage()

            # Email From, Email To
            email["from"] = "ACM"
            email["To"] = self.receiver
            email["subject"] = self.subject
            email.set_content(self.message)

            # Sending email via gmail
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.sender, self.credential)
                smtp.send_message(email)

        else:
            raise ValueError("receiver or subject or message is undefined")

    # Sending a html email
    def send_html_email(self):
        # Setting up html email
        html_file = HtmlTemplate(
            "./static/welcome.html", self.full_name
        )  # change to absolute path

        # Adding acm logo into the html email
        html_file.add_image(
            "./static/images/acm.png", "<image>"
        )  # change to absolute path

        # Adding paypal logo into the html email
        html_file.add_image(
            "./static/images/donate.png", "<paypal>"
        )  # change to absolute path

        # Email From, Email To
        email = EmailMessage()
        email["from"] = "ACM"
        email["To"] = self.receiver
        email["subject"] = self.subject
        email.set_content(html_file.html_message)

        # sending email via gmail
        try:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.sender, self.credential)
                smtp.send_message(email)

        except:
            writer.write_txt(f"Unable to send email to {self.receiver}")
