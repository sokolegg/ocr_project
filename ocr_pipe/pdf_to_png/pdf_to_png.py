try:
	from PIL import Image
except ImportError:
	import Image

from pdf2image import convert_from_path
import sys, os

def pdf_to_images(pdf_path):
	images = convert_from_path(pdf_path)
	return images

def convert_pdf_to_images(pdf_path, output_path):
	if not os.path.isdir(output_path):
		os.mkdir(output_path)
	images = pdf_to_images(pdf_path)
	paths = []
	for i, img in enumerate(images):
		output_img_path = output_path + '/' + str(i) + '.png'
		img.save(output_img_path, 'PNG')
		paths.append(output_img_path)
	return paths

if __name__ == '__main__':
	args = sys.argv[1:]
	convert_pdf_to_images(args[0], args[1])