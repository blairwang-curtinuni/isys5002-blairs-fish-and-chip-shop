# Settings
POS_TERMINAL = "123A"
TRANSACTION_ID = "4567/1"
RECEIPT_ID = "314159265358979"
MY_TIMEZONE = "Australia/Perth"
LINE_WIDTH=50

# Imports
from datetime import datetime
from zoneinfo import ZoneInfo

def get_pos_info():
    pos_info = ""
    pos_info += "POS " + POS_TERMINAL + " "
    pos_info += "TRANS " + TRANSACTION_ID + " "
    pos_info += str(datetime.now().astimezone(ZoneInfo(MY_TIMEZONE)).strftime("%c %Z"))
    return pos_info

def get_receipt_id():
    return RECEIPT_ID

def get_line_width():
    return LINE_WIDTH

def make_2part_line(product_name, price_string):
    len_product = len(product_name)
    len_price = len(price_string)
    whitespace_length = LINE_WIDTH - (len_product + len_price)

    return product_name + " " * whitespace_length + price_string

def gen_receipt_header():
    texts = []
    texts.append("Blair's ISYS5002 Fish and Chips Shop")
    texts.append("**  This is not a real fish and chip shop!  **")
    texts.append("** It is a demo for ISYS5002 students! ^__^ **")
    return texts

def gen_receipt_body():
    texts = []
    texts.append("School of Mgmt and Mrkting  PH: 08 1234 5678")
    texts.append("Building 402, Curtin University, Bentley WA")
    texts.append("TAX INVOICE - ABN 88 000 000 000")
    texts.append(get_pos_info())
    texts.append("")
    texts.append("")
    texts.append(make_2part_line("ITEM PURCHASED", "PRICE ($)"))
    texts.append(make_2part_line("--------------", "---------"))
    texts.append(make_2part_line("fish and chips", "20.60"))
    texts.append(make_2part_line("king lobster DAILY SPECIAL", "99.99"))
    texts.append(make_2part_line("garlic bread", "9.60"))
    texts.append(make_2part_line("special tartare sauce", "5.60"))
    texts.append("")
    texts.append(make_2part_line("TOTAL", "TBC"))
    texts.append(make_2part_line("TOTAL includes GST", "TBC"))
    texts.append("")
    texts.append("")
    texts.append("")
    texts.append("Paid with card xx1234")
    texts.append("")
    texts.append("Thank you for visiting today!")
    texts.append("'Sea' you next time!")
    texts.append("")
    texts.append("")
    texts.append("")
    texts.append("Logo generated using Google AI Mode:")
    texts.append("https://share.google/aimode/lVbccGsO5RAgTE1KK")
    texts.append("")
    texts.append("DISCLAIMER: THIS IS NOT A REAL DOCKET!")
    texts.append("GENERATED FOR ISYS5002 INTRODUCTION TO PROGRAMMING")
    return texts

def gen_receipt_footer():
    texts = []
    texts.append("Receipt ID:")
    texts.append(get_receipt_id())
    return texts


def main():
    headertext = gen_receipt_header()
    bodytext = gen_receipt_body()
    footertext = gen_receipt_footer()

    with open("receipt.txt", "w", encoding="utf-8") as file:
        for line in headertext:
            file.write(line + "\n")
        
        file.write("\n")

        for line in bodytext:
            file.write(line + "\n")

        file.write("\n")

        for line in footertext:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
