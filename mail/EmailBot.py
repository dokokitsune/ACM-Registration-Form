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

class MailBot:
    sender = "acm.csula.web@gmail.com"  # update this
    credential = utility.retrieve_key()  # update this
    #print(credential)

    def __init__(self, receiver=None, subject=None, message=None):
        self.receiver = receiver
        self.subject = subject
        self.message = message

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
    def send_html_email(self, file, name, img):
        # HTML Email Template
        # html_file = (Template(Path("welcome.html").read_text())).substitute(
        # {"name": name}, "html")

        html_message = getContent(file=file, name=name, image=img)

        email = EmailMessage()

        # Email From, Email To
        email["from"] = "ACM"
        email["To"] = self.receiver
        email["subject"] = self.subject
        # email.set_content(html_file.substitute({"name": name}), "html")
        email.set_content(html_message)

        # sending email via gmail
        try:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.sender, self.credential)
                smtp.send_message(email)

        except:
            raise RuntimeError(f"Unable to send emails to {self.receiver}.")


def getContent(file, name, image):
    # Create a html template object and substitute variables in the template
    html_file = (Template(Path(file).read_text())).substitute({"name": name})

    # Create html message
    html_message = MIMEMultipart()
    html_message.attach(MIMEText(html_file, "html"))

    # load and attach the image
    try:
        with open(image, "rb") as file:
            image_data = file.read()
            image = MIMEImage(image_data)
            image.add_header("Content-ID", "<image>")
            html_message.attach(image)

            return html_message
    except:
        writer.write_txt(f"Unable to open {image}. Check whether the {image} is /assets directory")
        raise FileNotFoundError(
            f"Unable to open {image}. Check whether the {image} is /assets directory"
        )
