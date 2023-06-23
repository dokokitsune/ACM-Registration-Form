import csv


def write_to_csv(data):
    with open("database.csv", newline="", mode="a") as csv_database:
        csv_writer = csv.writer(
            csv_database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow(data)


# makes a log of any component failure
def write_txt(data):
    with open("./Log/log.txt", mode="a") as text_file:
        text_file.write(data + "\n")
