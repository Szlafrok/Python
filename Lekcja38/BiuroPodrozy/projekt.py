file_path = "Lekcja38/BiuroPodrozy/"
# pip install -r requirements.txt.

from fpdf import FPDF
from fpdf.enums import XPos, YPos
import glob

A4H = 297
A4W = 210


pdf = FPDF()
pdf.add_page()

pdf.add_font("DejaVu", "", f"{file_path}DejaVuSansCondensed.ttf")
pdf.set_font("DejaVu", size = 32)
pdf.set_text_color(255, 0, 0)
pdf.text(text = "Oferta biura podróży Hurricane Travels", x = 5, y = 20)

pdf.image(f"{file_path}logo.png", x = 0.25 * A4W, y = A4H * 0.25, w = 0.5 * A4W, h = 0.5 * A4W)

pdf.set_text_color(0, 0, 0)
pdf.set_font("DejaVu", size = 24)
pdf.text(x = 50, y = A4H*0.75, text = "Oferta wycieczki - słońce pustyni")

pdf.set_font("DejaVu", size = 8)
pdf.text(x = 10, y = A4H - 20, text = "Wygenerowane przy pomocy Pythona oraz modelu AI")


for image_path in glob.glob(f"{file_path}atrakcje_grafiki/*"):
    attraction = image_path[:-4].replace("atrakcje_grafiki\\", "")
    attraction = attraction.replace(file_path, "")

    text_path = f"{file_path}atrakcje_opisy/{attraction}.txt"
    pdf.add_page()

    pdf.set_font("DejaVu", size = 24)
    pdf.cell(200, 20, text = f"Nazwa atrakcji: {attraction.replace("_", " ").capitalize()}", new_x = XPos.LEFT, new_y = YPos.NEXT, align = "C")

    pdf.cell(200, 10, link = pdf.image(image_path, w = 195, h = 120), new_x = XPos.LEFT, new_y = YPos.NEXT, align = "L")

    pdf.set_font("DejaVu", size = 12)

    with open(text_path, "r", encoding = "utf-8") as file:
        description = file.read()
    pdf.multi_cell(200, 10, text = f"Opis atrakcji: {description}", new_x = XPos.LEFT, new_y = YPos.NEXT, align = "L")

# ----------------------------------------------
pdf.output(f"{file_path}OfertaGotowa.pdf")
