import gspread

def addData(data):
    sa = gspread.service_account(filename="/home/acmcsulaweb/ACM-Registration-Form/sheets/service_account.json")
    sheet = sa.open("ACM 2023-2024 Member Registration")
    wkt = sheet.worksheet("responses")

    wkt.append_row(data)



