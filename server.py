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
        # data = request.form.to_dict()
        # print(request.form.getlist("availability"))
        # print(data)
        get_data(request)

        # write_to_csv(data)
        return "Submitted"


def write_to_csv(data):
    email = data["Email"]
    membership_status = data["membership"]
    first_name = data["firstName"]
    last_name = data["lastName"]
    id = data["cin"]
    phone_number = data["phone-number"]
    discord_tag = data["discordTag"]
    gender = data["gender"]
    major = data["major"]
    grade = data["standing"]
    senior_design = data["senior-design"]
    graduation_year = data["gradyear"]
    hear = data["hear"]
    buddy_system = data["buddy"]
    project_workshop = data["project-workshop"]
    avalibility = data["avalibility"]
    suggestion = data["recommendations"]
    confirm_email = data["confirmation"]

    with open("database.csv", newline="", mode="a") as csv_database:
        first, last, gender, major, gradyear = (
            data["firstName"],
            data["lastName"],
            data["gender"],
            data["major"],
            data["gradyear"],
        )
        # csv_writer = csv.writer(
        #    csv_database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        # )
        # csv_writer.writerow([email, subject, message])


def get_data(request):
    data = request.form.to_dict()
    print(data)
    """email = data['Email']
    membership_status = data["membership"]
    first_name = data["firstName"]
    last_name = data["lastName"]
    id = data["cin"]
    phone_number = data["phone-number"]
    discord_tag = data["discordTag"]
    gender = data["gender"]
    major = data["major"]
    grade = data['standing']
    senior_design = data['senior-design']
    graduation_year = data['gradyear']
    hear = data['hear']
    career_expectation = data['gain']
    buddy_system = data['buddy']
    project_workshop = data['project-workshop']
    avalibility = data['avalibility']
    suggestion = data['recommendations']
    confirm_email = data['confirmation']"""

    hear = request.form.getlist("hear")
    career_expectation = request.form.getlist("gain")
    project_workshop = request.form.getlist("project-workshop")
    availability = request.form.getlist("availability")

    print(extract_from_list(hear))
    print(extract_from_list(career_expectation))
    print(extract_from_list(project_workshop))
    print(extract_from_list(availability))


# Takes an array and returns a string
def extract_from_list(arr):
    result = ""
    for word in arr:
        result += word + " "

    return result
