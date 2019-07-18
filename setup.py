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
      install_requires=['numpy>=1.9.1',
                        'scipy>=0.14',
                        'six>=1.9.0',
                        'pyyaml',
                        'h5py',
                        'keras_applications>=1.0.6',
                        'keras_preprocessing>=1.0.5'],
      extras_require={
          'visualize': ['pydot>=1.2.4'],
          'tests': ['pytest',
                    'pytest-pep8',
                    'pytest-xdist',
                    'flaky',
                    'pytest-cov',
                    'pandas',
                    'requests',
                    'markdown'],
      },
      packages=find_packages())