import pymupdf

def pdf_to_txt(pdf_file_path : str)-> str: 
    full_text = ''
    doc = pymupdf.open(pdf_file_path)
    for page in doc :
        text = page.get_text()
        full_text += text + '\n-----------------\n'
    return full_text

