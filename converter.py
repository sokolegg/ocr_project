# This script can convert docx, doc, xls, xlsx .. to pdf
# You need python=3.6
# textract, fpdf

import sys
import textract
from fpdf import FPDF

def str2pdf(str_obj, filename='string.pdf'):   
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size=12)
	pdf.cell(200, 10, txt=str_obj, ln=1, align="C")
	pdf.output(filename)
	return open(filename, "rb").read()

def file2str(filename):
	text = textract.process(filename)
	return str(text)

if __name__ == '__main__':
	args = sys.argv[1:]
	file_in = args[0]
	file_out = args[1]
	text = file2str(file_in)
	print('Text in file ', file_in, ' : ', text[:50], '...')
	pdf = str2pdf(text, file_out)
	print('Pdf : ', pdf[:50], '... saved as: ', file_out)