import gspread
sa = gspread.service_account(filename="./sheets/service_account.json")
sheet = sa.open("ACM 2023-2024 Member Registration")

wkt = sheet.worksheet("responses")


class ACMSheet:
    def __init__(self, data):
        wkt.append_row(data)


