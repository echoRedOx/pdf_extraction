import pymupdf4llm
import pymupdf
import pathlib
import os
import sys


def extract_pdf_to_md(input_filepath: str):
    """
    Extract .pdf file contents into .md format using pymupdf4llm's to_markdown method. Markdown is often used in llm training and fine-tuning with parsers built into most chat interfaces.
    """
    doc = pymupdf.open(input_filepath)
    output_filepath = os.path.splitext(input_filepath)[0] + ".md"
    md_text = pymupdf4llm.to_markdown(doc)
    pathlib.Path(output_filepath).write_bytes(md_text.encode())
    print(md_text)


if __name__ == "__main__":
    input_filepath = sys.argv[1]
    extract_pdf_to_md(input_filepath)