# Settings
LINE_HEIGHT = 5
LOGO_LOCATION = "fish_chip_logo_nobg_grey.png"
LOGO_WIDTH = 100
BARCODE_WIDTH = 40

# Imports
from datetime import datetime
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import barcode
from barcode.writer import ImageWriter
import blairfishchips_text as bfacs_rt


barcode_writer_class = barcode.get_barcode_class('code128')
barcode_writer = barcode_writer_class(bfacs_rt.get_receipt_id(), writer=ImageWriter())
barcode_writer.save("barcode")

def pdf_next_line_wrapper(fpdf_instance, next_line_text, is_centered=True):
    align_instruction='L'
    if (is_centered):
        align_instruction='C'

    fpdf_instance.cell(
        200,
        LINE_HEIGHT,
        text=next_line_text,
        align=align_instruction,
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT
    )

def generate_line(product_name, price_string):
    len_product = len(product_name)
    len_price = len(price_string)
    whitespace_length = bfacs_rt.get_line_width() - (len_product + len_price)

    return product_name + " " * whitespace_length + price_string

pdf = FPDF()
pdf.add_page()
pdf.set_font("Courier", size=10)

image_successfully_loaded = False
image_loading_error = None
try:
    # Add text cells
    pdf.image(LOGO_LOCATION, x=(pdf.w - LOGO_WIDTH)/2 + 5, y=22, w=LOGO_WIDTH)
    image_successfully_loaded = True
except FileNotFoundError as e:
    image_loading_error = e

headertext = bfacs_rt.gen_receipt_header()
for line in headertext:
    pdf_next_line_wrapper(pdf, line)

for i in range(0,10):
    pdf_next_line_wrapper(pdf, "")

bodytext = bfacs_rt.gen_receipt_body()
for line in bodytext:
    pdf_next_line_wrapper(pdf, line)

pdf.image("barcode.png", x=(pdf.w - BARCODE_WIDTH)/2 + 5, y=(pdf.h - 50), w=BARCODE_WIDTH)

if (image_successfully_loaded != True):
    pdf.add_page()
    pdf_next_line_wrapper(pdf, "BLAIR'S FISH AND CHIP SHOP")
    pdf_next_line_wrapper(pdf, "SYSTEM DIAGNOSTIC MESSAGE FOR STAFF")
    pdf_next_line_wrapper(pdf, "! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
    pdf_next_line_wrapper(pdf, "")
    pdf_next_line_wrapper(pdf, "SYSTEM ERROR INFORMATION:")
    pdf_next_line_wrapper(pdf, str(image_loading_error))
    pdf_next_line_wrapper(pdf, "")
    pdf_next_line_wrapper(pdf, "POS INFO = " + bfacs_rt.get_pos_info())
    pdf_next_line_wrapper(pdf, "RECEIPT = " + bfacs_rt.get_receipt_id())
    pdf_next_line_wrapper(pdf, "")
    pdf_next_line_wrapper(pdf, "If found, please return to staff for a coupon!")

pdf.output("receipt.pdf")

