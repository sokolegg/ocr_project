# Description
This tool is for extracting and converting text

# Dependecies
1. textract - for extractring text from different formats in Python 
https://textract.readthedocs.io/en/stable/
2. antiword - Antiword converts the binary files from Word 2, 6, 7, 97, 2000, 2002 and 2003 to plain text and to PostScript TM
http://www.winfield.demon.nl/
3. unrtf - UnRTF is a command-line program written in C which converts documents in Rich Text Format (.rtf) to HTML, LaTeX, troff macros, and RTF itsel
https://www.gnu.org/software/unrtf/


# Installing
1. copy atiword in C://antiword
2. add antiword folder (C://antiword) to PATH:
export ANTIWORD_PATH="C:\\antiword"
export PATH=$PATH:$ANTIWORD_PATH
3. install textract
cd textract 
pip install .

# Usage
files:
python converter.py ./test_files/test.docx test_docx.pdf
python converter.py ./test_files/test.xlsx test_xlsx.pdf

convert folder with files:
python converter.py ./test_files pdf
-- it's create test_files_pdf with all files from test_files converted to pdf format