import fitz

def extract_text(pdf_path):
    text = []

    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text.append(page.get_text())

    return "".join(text)