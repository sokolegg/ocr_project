import os, sys
import common_utils as cu
import locale
locale.setlocale(locale.LC_ALL, 'C')
import xlrd
from weasyprint import HTML

def xls_to_str(filename):
	text = ""
	book = xlrd.open_workbook(filename)
	for sheet_index in range(book.nsheets):
		sheet =  book.sheet_by_index(sheet_index)
		for row_num in range(sheet.nrows):
			row = sheet.row(row_num)
			values = [str(el.value) for el in row]
			text += ','.join(values) + '\n'
	return text

def str_to_pdf(text, filename='last_text.pdf'):   
	HTML(string=text).write_pdf(filename)
	return text

def pdf_convert(source_file, destination_folder):
	combineText = xls_to_str(source_file)
	text = combineText.encode("utf-8").decode("utf-8").encode("ascii","ignore").decode("utf-8")
	with open(destination_folder, "w+b") as f:
		out_file = cu.get_out_filename(source_file, destination_folder, '.pdf')
		str_to_pdf(text, out_file)