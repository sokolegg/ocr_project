cd ocr_project/image_to_text
sh install.sh
python image_to_txt.py test_files/bank_test.jpg bank_test.txt
cat bank_test.txt

# python image_to_pdf.py test_files/bank_test.jpg bank_test.pdf