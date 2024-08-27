import pymupdf
import pathlib
import os
import sys


def extract_pdf_to_txt(input_filepath):
    doc = pymupdf.open(input_filepath)
    output_filepath = os.path.splitext(input_filepath)[0] + ".txt"
    out = open(output_filepath, "wb")
    
    for page in doc:
        text = page.get_text().encode("utf8")
        out.write(text)
        out.write(bytes((12,)))
        
    out.close()


if __name__ == "__main__":
    input_filepath = sys.argv[1]
    extract_pdf_to_txt(input_filepath)