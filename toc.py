from PyPDF2 import PdfReader, PdfWriter
filename = "/Users/uk/Documents/GitHub/PDFMerger/tu-ilmenau-ccse2023-finals/merged_pdf_all.pdf"

with open(filename, "rb") as f:
    r = PdfReader(f)

    bookmarks = list(map(lambda x: (x.title, r.get_destination_page_number(x)), r.outline))
    print(bookmarks)
    for i, b in enumerate(bookmarks):
        begin = b[1]
        end  = bookmarks[i+1][1] if i < len(bookmarks) - 1 else len(r.pages)
        # print(len(r.pages[begin:end]))
        name = b[0] + ".pdf"
        print(f"{name=}: {begin=}, {end=}")
        with open(name, "wb") as f:
            w = PdfWriter(f)
            for p in r.pages[begin:end]:
                w.add_page(p)
            w.write(f)