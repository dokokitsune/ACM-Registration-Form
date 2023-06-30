import gspread
from utilities.writer import write_txt


def addData(data):
    try:
        sa = gspread.service_account(filename="./sheets/service_account.json")
        sheet = sa.open("ACM 2023-2024 Member Registration")
        wkt = sheet.worksheet("responses")

        wkt.append_row(data)

    except:
        write_txt("Unable to append information to google sheets")
        return
