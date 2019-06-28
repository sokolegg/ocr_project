# This script can convert docx, doc 2 pdf
# You need python=3.6
# textract, docx, fpdf

import sys
import docx
import textract
from fpdf import FPDF

def docx2str(filename):
	doc = docx.Document(filename)
	text = []
	for para in doc.paragraphs:
		text.append(para.text)
	return '\n'.join(text)

def xlsx2str(filename):
	text = textract.process(filename)
	return str(text)

def doc2pdf(filename):
	pass

def str2pdf(str_obj, filename='string.pdf'):   
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size=12)
	pdf.cell(200, 10, txt=str_obj, ln=1, align="C")
	pdf.output(filename)
	return open(filename, "rb").read()

if __name__ == '__main__':
	args = sys.argv[1:]
	# if file.endswith('.doc'):
	file_in = args[0]
	file_out = args[1]
	if file_in.endswith('xlsx'):
		text =xlsx2str(file_in)
	if file_in.endswith('docx'):
		text = docx2str(file_in)
	print('Text in file ', file_in, ' : ', text[:50], '...')
	pdf = str2pdf(text, file_out)
	print('Pdf : ', pdf[:50], '... saved as: ', file_out)