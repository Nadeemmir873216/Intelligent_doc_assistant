# importing libraries

from pypdf import PdfReader
from pathlib import Path

# Create document loader

def load_pdf(file_path):

    reader = PdfReader(file_path)

    document = []

    for page_number , page in enumerate(reader.pages):
        text = page.extract_text()

        if not text:
            continue
        
        document.append(
            {
                "page_number": page_number + 1,
                "text": text,
                "source": Path(file_path).name
            }
        )
    
    return document

