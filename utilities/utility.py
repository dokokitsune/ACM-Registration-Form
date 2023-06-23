from datetime import date


# takes the raw data from dictonary and turns them into list
def get_data(request):
    data = request.form.to_dict()
    student_info = []
    student_info.append(get_date_stamp())
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


# returns the current time
def get_date_stamp():
    return date.today()
