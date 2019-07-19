from . import image_to_text
from . import pdf_to_png
from . import text_to_vector
from .text_to_vector import text_to_embeddings 

import numpy as np
import pandas as pd


class PDFToVectors():
	'''processor for direct converting from pdf to words vectors
	'''
	def __init__(self, words_num=20, vectors_num=1000):
		self.words_num = words_num
		self.vectors_num = vectors_num

	def process(self, inp):
		# input is one pdf file
		print('Processing %s' % inp)
		images = pdf_to_png.pdf_to_images(inp)
		texts = ''

		# ocr part
		for img in images:
			text = image_to_text.image_to_str(img)
			texts += (text + ' ')

		print('Processed full text: %s' % texts[:100])
		# generate vectors
		vectors = None
		for i in range(self.vectors_num):
			random_char_start = np.random.choice(range(len(texts)))
			cutted_text = texts[random_char_start:]
			text_vector = text_to_embeddings.text_to_vectors(text=cutted_text, words_num=self.words_num, fill_all=True)
			flatten_vector = text_vector.reshape(1, -1)
			vectors = flatten_vector if vectors is None else np.vstack([flatten_vector, vectors])

		print('Processed %d vectors with %d features for file %s' % (self.vectors_num, vectors.shape[1], inp))

		return images, texts, vectors

def run(files_csv, processor, file_column_name='file'):
	files_df = pd.read_csv(files_csv)
	files = files_df[file_column_name].values

	vectors = []
	for f in files:
		_, _, vector = processor.process(f)
		vectors.append(vector)

	print('Collected!')

	files_df['features'] = vectors
	return files_df

