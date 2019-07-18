try:
	from PIL import Image
except ImportError:
	import Image

import pytesseract
import sys
import string
from weasyprint import HTML


def image_to_str(img):
	text = pytesseract.image_to_string(Image.open(img))
	return text


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


def str_to_pdf(str_obj, filename):   
	html = HTML(string=str_obj).write_pdf(filename)
	return str_obj


def convert_file(file_in, file_out):
	text = image_to_str(file_in)
	text = filter_str(text)
	print('Text in file ', file_in, ' : ', text[:50], '...')
	returned_info = str_to_pdf(text, file_out)
	print('File data: ', returned_info[:50], '... saved as: ', file_out)

if __name__ == '__main__':
	args = sys.argv[1:]
	convert_file(args[0], args[1])


