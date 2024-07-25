#All in one - 
from flask import Flask
import PyPDF2

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi Tejal, You are the Best"

#frog_book = 'C:/Users/tejal/OneDrive/Desktop/Project_git/Prescription/Backend/Eat-That-Frog.pdf'

@app.route('/convert')
def PDF_to_text():
    reader = PyPDF2.PdfReader('C:/Users/tejal/OneDrive/Desktop/Project_git/Prescription/Backend/Syllabus.pdf')
    str = ''
    for page in reader.pages:
        str += page.extract_text()
    
    #with open("text2_server.txt", "w", encoding='utf-8') as f:
    #    f.write(str)
    return str

#if __name__ == "__main__":
app.run(debug=True)