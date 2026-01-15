import os
from PyPDF2 import PdfReader, PdfWriter

CHUNK_SIZE = 5

def chunk_pdf(pdf_path):
    if not os.path.isfile(pdf_path):
        print("Error: File does not exist")
        return

    if not pdf_path.lower().endswith(".pdf"):
        print("Error: Input file must be a PDF")
        return

    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)

    base_dir = os.path.dirname(pdf_path)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_dir = os.path.join(base_dir, f"{pdf_name}_chunks")
    os.makedirs(output_dir, exist_ok=True)

    chunk_number = 1
    for start in range(0, total_pages, CHUNK_SIZE):
        writer = PdfWriter()
        end = min(start + CHUNK_SIZE, total_pages)

        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        output_path = os.path.join(
            output_dir,
            f"{pdf_name}_part_{chunk_number}.pdf"
        )

        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"Created: {output_path}")
        chunk_number += 1

    print(f"\nDone. PDFs saved in:\n{output_dir}")

if __name__ == "__main__":
    pdf_path = input("Enter full path of the PDF file: ").strip()
    chunk_pdf(pdf_path)
