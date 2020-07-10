import pyttsx3
import PyPDF2

book = open('object_oriented_python_tutorial.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

shishir = pyttsx3.init()

page = pdfReader.getPage(15)

text = page.extractText()
shishir.say(text)

shishir.runAndWait()