import datetime
import os
from utilities import writer


# takes the raw data from dictonary and turns them into list
def get_data(request):
    data = request.form.to_dict()
    student_info = []
    student_info.append(datetime.date.today().strftime("%B %d, %Y"))
    for key in data.keys():
        if (
            key == "hear"
            or key == "gain"
            or key == "project-workshop"
            or key == "availability"
        ):
            # request.form.getlist(key) gets multiple answers in an array
            student_info.append(extract_string_from_list(request.form.getlist(key)))

        else:
            student_info.append(data[key])

    return student_info


# takes list of strings and turns them into string
# example: ['apple', 'banana'] = "apple banana"
def extract_string_from_list(arr):
    result = ""
    count = 0
    for word in arr:
        # no space added for the first element
        if count != 0:
            result += " "

        result += word
        count += 1

    return result


def retrieve_key():
    file_path = os.path.expanduser("~/.bashrc")
    variable_name = "secret_key"

    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("export") and variable_name in line:
                value = line.split("=")[1].strip().strip('"')
                return value

        writer.write_txt("key not found")
        raise NameError("key not found")
