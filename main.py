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

engine = pyttsx3.init()
engine.save_to_file(finalText, 'lorem.mp3')
engine.runAndWait()

# Use the following code if you only want the script to recite the PDF file
# engine = pyttsx3.init()
# engine.say(finalText)
# engine.runAndWait()