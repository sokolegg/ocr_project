# Model for one word image to text
git clone https://github.com/githubharald/SimpleHTR.git
unzip SimpleHTR/model/model.zip -d SimpleHTR/model/
SimpleHTR/src && python main.py

# Framework for segmentation of text image
git clone --recursive https://github.com/awslabs/handwritten-text-recognition-for-apache-mxnet htram
pip install mxnet
pip install mxboard
cd htram && python get_models.py
pip install editdistance
