from flask import Flask, render_template, request
import csv
from mail import EmailBot

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    print("submit form")
    if request.method == "POST":
        data = request.form.to_dict()
        data['gain'] = request.form.getlist('gain')
        data['project-workshop'] = request.form.getlist('project-workshop')
        data['hear'] = request.form.getlist('hear')
        data['availability'] = request.form.getlist('availability')

        write_to_csv(data)
        print(request.form.get("Email"))
        EmailBot.MailBot("joloh18@yahoo.com",
                  "Welcome to the ACM club 2023-2024!").send_html_email("./static/welcome.html",request.form.get("firstName"), "./static/images/acm.png")
        return "Submitted"


def write_to_csv(data):
    with open("database.csv", newline="", mode="a") as csv_database:
        first, last, gender, major, gradyear = (
            data["firstName"],
            data["lastName"],
            data["gender"],
            data["major"],
            data["gradyear"],
        )
        csv_writer = csv.writer(
            csv_database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([first, last, gender, major, gradyear])
