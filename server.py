from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    print("submit form")
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        print(data["project-workshop"])
        return "Submitted"


def write_to_csv(data):
    with open("database.csv", newline="", mode="a") as csv_database:
        email, message, subject = (
            data["firstName"],
            data["lastName"],
            data["project-workshop"],
        )
        csv_writer = csv.writer(
            csv_database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, message])
