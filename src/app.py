from flask import Flask, request,send_file
from fileinput import filename
from pdf2docx import parse
import json

app = Flask(__name__)

@app.route('/convertpdf', methods = ['POST'])  
def convertpdf():  
    if request.method == 'POST':  
        f = request.files['file']
        pdfFileNmae = "pdf.pdf"
        f.save(pdfFileNmae)  
        doc = f.filename.replace("pdf","docx")
        parse(pdfFileNmae, doc)
        
        return send_file(doc)
