# import io
# import img2pdf
# from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
 
c = canvas.Canvas('page.pdf')
c.drawImage('carte_temoin.png', 0, 0, 10*cm, 10*cm)
c.showPage()
c.save()
 
# def merge_pdf(pdf_data):
#     writer = PdfFileWriter()
#     for document in pdf_data:
#         reader = PdfFileReader(io.BytesIO(document), strict=False)
#         for page in range(0, reader.getNumPages()):
#             writer.addPage(reader.getPage(page))
#     _buffer = io.BytesIO()
#     writer.write(_buffer)
#     merged_pdf = _buffer.getvalue()
#     _buffer.close()
#     return merged_pdf
 
 
# with open("fichier.pdf", "rb") as pdf, open("carte_temoin.png", "rb") as image:
#     pdf_final = merge_pdf([pdf.read(), img2pdf.convert(image.read())])
 
# with open("fichier_final.pdf", "wb") as file:
#     file.write(pdf_final)