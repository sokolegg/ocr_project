import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")

import string

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

def text_to_vectors(text, vectors_size, fill_all=True):
	words = text_to_words(text)
	vectors = []
	for word in words:
		vector = word_to_vector(word)
		if vector is None:
			continue
		vectors.append(vector)
		if len(vectors) > vectors_size:
			return vectors

	if fill_all:
		# fill to correct size
		while len(vectors) < vectors_size:
			end_vector = word_to_vector('.')
			vectors.append(end_vector)
	
	return vectors




