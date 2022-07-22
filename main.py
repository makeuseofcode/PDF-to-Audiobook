import PyPDF3
import pyttsx3
import pdfplumber

file = 'Lorem.pdf'

book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)

pages = pdfReader.numPages

finalText = ""
with pdfplumber.open(file) as pdf:
    for i in range(0, pages): 
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text