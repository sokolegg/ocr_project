# Description
This tool is for extracting and converting text from old formats for new ML frameworks

# Dependecies
1. xlrd - for extracting tables from xls files
http://www.python-excel.org/

2. WeasyPrint - for converting to pdf format 
https://weasyprint.org/


# Installing
## Linux
sh install.sh

# Usage
## One File
python converter.py ./test_files/test.xls test_xls.pdf
## Folder
python converter.py ./test_files txt
