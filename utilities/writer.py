import csv


def write_to_csv(data):
    with open("database.csv", newline="", mode="a") as csv_database:
        csv_writer = csv.writer(
            csv_database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow(data)


# makes a log of any component failure
def write_txt(data):
    with open("log.txt", mode="a") as text_file:  # change this to absolute path
        text_file.write(data + "\n")
