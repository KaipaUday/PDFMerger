from PyPDF2 import PdfMerger,PdfReader, PdfWriter

#set path files
import os
os.chdir('/Users/uk/Documents/GitHub/PDFMerger/tu-ilmenau-ccse2023-finals')
cwd = os.path.abspath('')
files = os.listdir(cwd)

def merge_pdf_files():
    merger = PdfMerger()
    pdf_files = [x for x in files if x.endswith(".pdf")]
    # Sort pdfs
    pdf_files.sort()
    print(pdf_files)
    # print(pdf_files.MediaBox)
    #number starts with pages
    # add preface with roman numbering
    [merger.append(pdf) for pdf in pdf_files]
    with open("all_merged_pdf_all.pdf", "wb") as new_file:
        merger.write(new_file,)
    # return "merged_pdf_all.pdf"
def prependToC(file):
    # create table of contents
    reader = PdfReader(open(file, 'rb'))
    print(reader.outline)

def compress(file):
    reader = PdfReader(file)
    writer = PdfWriter()
    for page in reader.pages:
        page.compress_content_streams()  # This is CPU intensive!
        writer.add_page(page)

    with open("out.pdf", "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    # merged=merge_pdf_files()
    compress("Cover_page.pdf") # did not reduce size
    # prependToC(merged)

# from PyPDF2 import PdfReader, PdfWriter

# reader = PdfReader("example.pdf")
# writer = PdfWriter()

# for page in reader.pages:
#     page.compress_content_streams()  # This is CPU intensive!
#     writer.add_page(page)

# with open("out.pdf", "wb") as f:
#     writer.write(f)