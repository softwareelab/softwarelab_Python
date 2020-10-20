from PyPDF2 import PdfFileWriter, PdfFileReader

def secure_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)

    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)

    with open(f"sifrelenmis_dosya_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"sifrelenmis_dosya_{file} oluşturuldu....")

if __name__ == "__main__":
    file = "1.pdf"
    password = "SoftwareLab"
    secure_pdf(file, password)