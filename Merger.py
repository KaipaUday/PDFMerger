from PyPDF2 import PdfMerger

#set path files
import os
os.chdir('/Users/uk/Documents/GitHub/PDFMerger/tu-ilmenau-ccse2023-finals')
cwd = os.path.abspath('')
files = os.listdir(cwd)

def merge_pdf_files():
    merger = PdfMerger()
    pdf_files = [x for x in files if x.endswith(".pdf")]
    # Sort pdfs
    # create table of contents
    #number starts with pages
    # add preface with roman numbering
    
    [merger.append(pdf) for pdf in pdf_files]
    with open("merged_pdf_all.pdf", "wb") as new_file:
        merger.write(new_file)

if __name__ == "__main__":
    merge_pdf_files()