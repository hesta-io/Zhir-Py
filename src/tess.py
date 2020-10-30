# - argparse: https://docs.python.org/3/library/argparse.html
# - pytesseract: https://pypi.org/project/pytesseract/

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import argparse
import sys

parser = argparse.ArgumentParser(
    description="Runs tesseract on an image and saves the result.")

parser.add_argument(
    "source", help="The path for the source image.")

parser.add_argument(
    "dest", help="The destination path of the result.")

parser.add_argument(
    "--format", help="Result format.", choices=["pdf", "text"], default="pdf"
)

args = parser.parse_args()

if format == 'text':
    result = pytesseract.image_to_string(
        Image.open(args.source), lang='ckb')
    with open(args.dest, "w") as f:
        f.write(result)
    print("Done :)")

elif format == 'pdf':
    pdf = pytesseract.image_to_pdf_or_hocr(
        args.source, extension='pdf', lang='ckb')
    with open(args.dest, 'w+b') as f:
        f.write(pdf)  # pdf type is bytes by default
    print("Done :)")
else:
    print("lol wut?")
    sys.exit(-1)
