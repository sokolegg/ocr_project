from setuptools import setup
from setuptools import find_packages

long_description = '''
Full Preprocessing tool for documents
'''

setup(name='ocr_pipe',
      version='0.1.0',
      description='Prcess your documents',
      long_description=long_description,
      author='Oleg Sokolov & Sergei Levashkin',
      author_email='sokolegg@yandex.ru',
      url='https://github.com/sokolegg/ocr_pipe',
      license='MIT',
      install_requires=['numpy',
                        'gensim',
                        'Pillow',
                        'pdf2image',
                        'pytesseract',
                        'weasyprint',
                        'pandas',
                        'tensorflow',
                        'opencv-python',
                        'keras'],
      packages=find_packages())