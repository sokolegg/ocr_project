# FULL OCR PREPROCESSING TOOL

This tool for full pipeline from pdf files to prepared for Machine learning data from files

# Pipeline 
## Classification problem:
We have set of pairs (pdf, target)
For example (receipt.pdf, [1 if fraud else 0])

Pipeline for that problem:
1. pdf documents -> images (using module pdf_to_png)
2. png files -> ocr tool to recognize text from png (using image_to_txt)
3. text from png files -> glove vectors (using text_to_vector module)
4. collect for all pairs (pdf, target) pairs like (vectors, target) 
5. now we have numerical data -> train your model to classify fraud!

# Installation 

1. download this repo as zip or using git clone
2. In directory of ocr_pipe run pip install .

# Usage
1. Prepare your dataset in csv like (or use labeled folders):
files.csv

pdf, target
data_dir\good_ticket1.pdf, 0
data_dir\bad_ticket1.pdf, 1
data_dir\bad_ticket2.pdf, 1
....

2. Right script
```python
import ocr_pipe

preprocessor = ocr_pipe.PDFToVectors(words_num = 50)
processed_frame = ocr_pipe.run(files.csv, preprocessor)
print(processed_frame.head())

# pdf, target, partition, words, features (word embeddings)
# ticket1.pdf, 0, 0, "first page text..", [0.4, 0.5, 0.7 ...]
# ticket1.pdf, 0, 1, "second page text..", [0.4, 0.6, 0.9 ...]
# ticket2.pdf, 1, 0, "fraud text in another document", [0.4, 0.6, 0.9 ...]

X = processed_frame.features.values
print(X.shape) # for length of embeddings 25 and 50 words it will be [dataset size, 50, 25]

y = processed_frame.target.values
print(y.shape) # same length as datset size

X_train, X_test, y_train, y_test = ...
model.fit()
....

# Train your model!

```





