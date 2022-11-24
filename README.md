# Pdf2Docx-in-docker
This repo provides a container which converts pdf into docx.

Used component for the conversion [pdf2docx](https://github.com/dothinking/pdf2docx).

How to run the container:

```
cd src
docker build -t pdfconverter .
docker run -d -p 5000:5000 --name converter pdfconverter
```

Sample request:
```
curl --location --request POST 'http://127.0.0.1:5000/convertpdf' \
--form 'file=@"{FilePath}"'
```
