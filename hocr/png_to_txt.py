import cv2
import numpy as np
import os, sys

# mxnet segmentation
import mxnet as mx
from htram.ocr.utils.iam_dataset import IAMDataset, resize_image, crop_image, crop_handwriting_page
from htram.ocr.word_and_line_segmentation import SSD as WordSegmentationNet, predict_bounding_boxes
from htram.ocr.paragraph_segmentation_dcnn import SegmentationNetwork, paragraph_segmentation_transform
from htram.ocr.utils.expand_bounding_box import expand_bounding_box
from htram.ocr.utils.word_to_line import sort_bbs_line_by_line, crop_line_images

ctx = mx.gpu(0) if mx.context.num_gpus() > 0 else mx.cpu()
print(ctx)
word_segmentation_net = WordSegmentationNet(2, ctx=ctx)
word_segmentation_net.load_parameters("htram/models/word_segmentation2.params")
word_segmentation_net.hybridize()

# word from image
from SimpleHTR.src.Model import Model, DecoderType
from SimpleHTR.src.SamplePreprocessor import preprocess
char_list = '../model/charList.txt'
decoder_type = DecoderType.BestPath
model_dump = None


def get_word_images_from_text_image(text_image, dest_images):

	img = cv2.imread(text_image, cv2.IMREAD_GRAYSCALE)
	images = [img]
	paragraph_segmented_images = images

	min_c = 0.1
	overlap_thres = 0.2
	topk = 4000

	predicted_words_bbs_array = []

	for i, paragraph_segmented_image in enumerate(paragraph_segmented_images):
		s_y, s_x = int(i/2), int(i%2)
		predicted_bb = predict_bounding_boxes(word_segmentation_net, paragraph_segmented_image, min_c, overlap_thres, topk, ctx)
		predicted_words_bbs_array.append(predicted_bb)
	
	word_images = []
	for i, bb in enumerate(predicted_words_bbs_array[0]):
		(x, y, w, h) = bb
		image_h, image_w = images[0].shape
		(x, y, w, h) = np.array((x * image_w, y * image_h, w * image_w, h * image_h), dtype=int)
		word_img = images[0][y: y + h, x: x + w]
		word_images.append(word_img)
		cv2.imwrite(dest_images + '/' + str(i) + '.png', word_img)

	return word_images


class Batch:
	"batch containing images and ground truth texts"
	def __init__(self, gtTexts, imgs):
		self.imgs = np.stack(imgs, axis=0)
		self.gtTexts = gtTexts

def image_to_str(model, img):
	"recognize text in image provided by file path"
	batch = Batch(None, [img])
	full_text = ''
	try:
		(recognized, probability) = model.inferBatch(batch, True)
		print(recognized, probability)
		full_text = ' '.join(recognized)
	except:
		print("Can't recognize")
	return full_text

def str_to_txt(str_obj, filename):
	txt = open(filename, 'w')
	txt.write(str_obj)
	txt.close()
	return str_obj

def png_to_txt(png_file, txt_file):
	convert_path = png_file.split('.')[0] + "_images"
	if not os.path.isdir(convert_path):
		os.mkdir(convert_path)
	word_images = get_word_images_from_text_image(png_file, convert_path)
	print('Find %d words' % len(word_images))
	os.chdir(os.getcwd() + '/SimpleHTR/src/')
	model = Model(open(char_list).read(), decoder_type, mustRestore=True, dump=model_dump)
	text = []
	# only first!
	for word_image in word_images:
		try:
			img = preprocess(word_image, Model.imgSize)
			text += [image_to_str(model, img)]
		except:
			continue
	text = ' '.join(text)
	os.chdir('../../')
	str_to_txt(text, txt_file)

if __name__ == '__main__':
	args = sys.argv[1:]
	png_to_txt(args[0], args[1])




