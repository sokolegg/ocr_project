# This script can convert docx, doc, xls, xlsx .. to pdf
# You need python=3.6
# textract, fpdf

import sys
import xlrd
from weasyprint import HTML
import os
import string

def str2pdf(str_obj, filename='last_text.pdf'):   
	html = HTML(string=str_obj).write_pdf(filename)
	return str_obj

def str2txt(str_obj, filename='last_text.txt'):
	txt = open(filename, 'w')
	txt.write(str_obj)
	txt.close()
	return str_obj

def xls2str(filename):
	str_obj = ""
	book = xlrd.open_workbook(filename)
	for sheet_index in range(book.nsheets):
		sheet =  book.sheet_by_index(sheet_index)
		for row_num in range(sheet.nrows):
			row = sheet.row(row_num)
			values = [str(el.value) for el in row]
			str_obj += ','.join(values) + '\n'
	return str_obj

def filter_str(str_obj):
	delete_if_repeat = list('\t\n\r' + ' ' + string.punctuation)
	previous_symbol = None
	new_str_obj = []
	for symbol in str_obj:
		if symbol in delete_if_repeat and previous_symbol in delete_if_repeat:
			continue
		else:
			new_str_obj.append(f"{symbol}")
		previous_symbol = symbol
	return ''.join(new_str_obj)


def convert_file(file_in, file_out):
	if not file_in.endswith('.xls'):
		print('Tool works only with xls format')
		return
	text = xls2str(file_in)
	text = filter_str(text)
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



