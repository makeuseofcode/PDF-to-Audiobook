import PyPDF3
import pyttsx3
import pdfplumber

file = 'Lorem.pdf'

book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)

pages = pdfReader.numPages

