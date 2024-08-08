from flask import Flask, render_template, request, jsonify, abort
from flask_cors import CORS
import stripe
from urllib import parse
from functools import wraps
from utilities import utility, writer
from mail.EmailBot import MailBot
from sheets.googlesheets import addData
from mail.HtmlTemplate import HtmlTemplate

stripe.api_key = "pk_live_51H0yOZEr4ylg7vlAnEDF4YfjfRe1VAEKjRMuW2Lh7zlMG9Lh68k4LZmuTm0RtR5MeNLJzkxUT0p53pdnQKgeIY1800N4Sipf5y"

app = Flask(__name__)
CORS(app, resourses={r"/*": {"origins": "https://acm-calstatela.com/"}})

@app.before_request
def check_referrer():
    allowed_hosts = ["https://acm-calstatela.com", "127.0.0.1:5000", "localhost:3000"]
    referrer = request.headers.get("Referer")
    if referrer:
        referrer_host = parse.urlparse(referrer).netloc
        if referrer_host not in allowed_hosts:
            abort(403)
# @app.route("/")
# def main_page():
#     return render_template("index.html")

@app.route("/")
def main_page():
    session_id = request.args.get('session_id')
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        if session.payment_status == "paid":
            return render_template("index.html")
        else:
            return "Payment not completed.", 400
    except stripe.error.InvalidRequestError:
        return "Invalid session ID", 400


# @app.route('/success')
# def success():
#     session_id = request.args.get('session_id')
#     try:
#         session = stripe.checkout.Session.retrieve(session_id)
#         if session.payment_status == "paid":
#             return render_template("index.html")
#         else:
#             return "Payment not completed.", 400
#     except stripe.error.InvalidRequestError:
#         return "Invalid session ID", 400

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
