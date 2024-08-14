from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for
from flask_cors import CORS
from urllib import parse
from functools import wraps
from uuid import UUID
from utilities import utility, writer
from mail.EmailBot import MailBot
from sheets.googlesheets import addData
from mail.HtmlTemplate import HtmlTemplate

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    # print("submit form")
    if request.method == "POST":
        # Processing dictonary data into list
        data = utility.get_data(request)

        # Using the list to save all data as csv for backup
        writer.write_to_csv(data)

        # sending a welcome email using the email & name recieved from the form
        send_email(data)

        # Appending the recieved data to google sheets
        addData(data)

        return render_template("submitted.html")


def send_email(data):
    try:
        reciever, full_name = data[1], data[3] + " " + data[4]
        mail_bot = MailBot(reciever, "Welcome New ACM Member", full_name=full_name)

        html_file = HtmlTemplate(
            "./static/welcome.html", full_name
        )  # change to absolute path
        html_file.add_image(
            "./static/images/acm.png", "<image>"
        )  # change to absolute path
        html_file.add_image(
            "./static/images/donate.png", "<paypal>"
        )  # change to absolute path

        mail_bot.send_html_email()
    except:
        pass
        writer.write_txt(f"Unable to send email to {data[1]}")
