# This script can convert docx, doc, xls, xlsx .. to pdf
# You need python=3.6
# textract, fpdf

import sys
import textract
from fpdf import FPDF
import os

def str2pdf(str_obj, filename='last_text.pdf'):   
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size=12)
	pdf.cell(200, 10, txt=str_obj, ln=1, align="C")
	pdf.output(filename)
	return open(filename, "rb").read()

def str2txt(str_obj, filename='last_text.txt'):
	txt = open(filename, 'w')
	txt.write(str_obj)
	txt.close()
	return str_obj

def file2str(filename):
	text = textract.process(filename)
	return remove_rtf_info(text.decode('utf-8'))

def remove_rtf_info(str_obj):
	return str_obj.split('-----------------')[-1]


def convert_file(file_in, file_out):
	text = file2str(file_in)
	print('Text in file ', file_in, ' : ', text[:50], '...')

	# write to specific format
	if file_out.endswith('pdf'):
		returned_info = str2pdf(text, file_out)
	else:
		returned_info = str2txt(text, file_out)
	print('File data: ', returned_info[:50], '... saved as: ', file_out)

def convert_path(path, convert_format):
	convert_path = path + '_' + convert_format
	if not os.path.isdir(convert_path):
		os.mkdir(convert_path)

	for file_in in os.listdir(path):
		full_file_in = f"{path}/{file_in}"
		full_file_out = f"{convert_path}/{file_in}.{convert_format}"
		convert_file(full_file_in, full_file_out)


if __name__ == '__main__':
	args = sys.argv[1:]
	if os.path.isdir(args[0]):
		convert_path(args[0], args[1])
	else:
		convert_file(args[0], args[1])



