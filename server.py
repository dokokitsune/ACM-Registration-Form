from flask import Flask, render_template, request
from utilities import utility, writer
from mail.EmailBot import MailBot

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    # print("submit form")
    if request.method == "POST":
        data = utility.get_data(request)

        # write_to_csv(data)
        writer.write_to_csv(data)

        # send email
        send_email(data)

        return render_template("submitted.html")


def send_email(data):
    try:
        reciever, full_name = data[1], data[3] + " " + data[4]
        mail_bot = MailBot(reciever, "Welcome New ACM Member")
        mail_bot.send_html_email(
            file="/home/acmcsulaweb/ACM-Registration-Form/static/welcome.html", name=full_name, img="/home/acmcsulaweb/ACM-Registration-Form/static/images/acm.png"
        )

    except:
        pass
        writer.write_txt(f"Unable to send email to {data[1]}")
