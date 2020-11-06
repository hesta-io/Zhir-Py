# - argparse: https://docs.python.org/3/library/argparse.html
# - pytesseract: https://pypi.org/project/pytesseract/

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import argparse
import sys
import fitz # PyMuPDF

parser = argparse.ArgumentParser(
    description="Runs tesseract on an image and saves the result. The result will be in both PDF format and Plain text format.")

parser.add_argument(
    "source", help="The path for the source image.")

parser.add_argument(
    "dest", help="The destination path of the result. Two files will be created: dest.pdf and dest.txt")

parser.add_argument(
    "--langs", help="Language models to be used for the OCR. Examples: ckb or ckb+eng", default="ckb"
)

args = parser.parse_args()

pdf_path = args.dest + '.pdf'
text_path = args.dest + '.txt'

pdf = pytesseract.image_to_pdf_or_hocr(
        args.source, extension='pdf', lang=args.langs, config = 'out pdf txt')
with open(pdf_path, 'w+b') as f:
    f.write(pdf)  # pdf type is bytes by default

doc = fitz.open(pdf_path)
page = doc.loadPage(0) # Our pdfs only have one page!
text = page.getText("text")

with open(text_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Done :)")