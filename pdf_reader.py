import pdfplumber
import PyPDF2
import re

def detect_ieee_paper_format(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        
        page_width = first_page.width
        
        text_boxes = first_page.extract_words()
        
        if not text_boxes:
            return "Unable to detect format"
        
        max_x1 = max(box['x1'] for box in text_boxes)
        
        text_width_ratio = max_x1 / page_width
        
        if text_width_ratio < 0.85:
            return "1-column"
        else:
            return "2-column"

def extract_abstract_1col(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    abstract = ''
    
    for i in range(num_pages):
        page = pdf_reader.pages[i]
        text = page.extract_text()
        
        match = re.search(r'(abstract\s*[:.-]*\s*)(.*?)(\n\s*[1-9]\s*\.\s*|introduction)', text, re.IGNORECASE | re.DOTALL)
        
        if match:
            abstract = match.group(2).strip()
            break

    return abstract

def extract_abstract_2col(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        page = pdf.pages[0]
        
        words = page.extract_words()
        
        left_half_words = [word['text'] for word in words if word['x0'] < page.width / 2]
        left_half_text = ' '.join(left_half_words)

        match = re.search(r'(?i)(abstract\s*[:.-]*\s*)(.*?)(\n\s*[1-9]\s*\.\s*|introduction)', 
                          left_half_text, re.DOTALL)

        if match:
            return match.group(2).strip()
        else:
            return "Abstract not found or couldn't be extracted."

def extract_abstract(pdf_path):
    format = detect_ieee_paper_format(pdf_path)
    
    if format == "1-column":
        abstract = extract_abstract_1col(pdf_path)
    elif format == "2-column":
        abstract = extract_abstract_2col(pdf_path)
    else:
        abstract = "Unable to extract abstract due to unknown format."
    
    return format, abstract


pdf_path = 'paper_1.pdf'
format, abstract = extract_abstract(pdf_path)
print(f"Paper format: {format}")
print(f"Abstract:\n{abstract}")