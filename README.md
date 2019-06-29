# COPY ANTIWORD IN C://antiword
# ADD ANTIWORD TO PATH
export ANTIWORD_PATH="C:\\antiword"
export PATH=$PATH:$ANTIWORD_PATH

# INSTALL TEXTRACT FOR WINDOWS
cd textract 
pip install .

# USAGE
python converter.py ./test_files/test.docx test_docx.pdf
python converter.py ./test_files/test.xlsx test_xlsx.pdf
python converter.py ./test_files/test.doc test_doc.pdf