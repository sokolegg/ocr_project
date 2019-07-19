import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")

import string
import numpy as np

def is_word_in_vocab(word):
	return word in model.vocab

def word_to_vector(word):
	if is_word_in_vocab(word):
		return model[word]

def text_to_words(text):
	for char in string.punctuation:
		text = text.replace(char, '')
	text = text.lower()
	words = text.split(' ')
	return words

def text_to_vectors(text, words_num, fill_all=True):
	words = text_to_words(text)
	vectors = None
	for word in words:
		# stop is filled
		if vectors is not None:
			if len(vectors) == words_num:
				# completed
				return vectors
		# fill by next vector
		vector = word_to_vector(word)
		if vector is None:
			continue
		vector = vector.reshape(1, -1)
		vectors = vector if vectors is None else np.vstack([vector, vectors]) 

	if fill_all:
		# fill to correct size
		if vectors is None:
			vectors = word_to_vector('.').reshape(1, -1)
		while len(vectors) < words_num:
			vector = word_to_vector('.').reshape(1, -1)
			vectors = vector if vectors is None else np.vstack([vector, vectors])
	
	return vectors




