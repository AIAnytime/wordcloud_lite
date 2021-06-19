# from distutils.core import setup
from setuptools import setup
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'Similarity_Score_Module',    
  long_description = long_description,
  long_description_content_type = 'text/markdown',    
  packages = ['Similarity_Score_Module'],   
  version = '1.0',      
  license='MIT',        
  description = 'Check Similarity Score',   
  author = 'Sonu Kumar',                   
  author_email = 'sonu1000raw@gmail.com',      
  url = 'https://github.com/sonucr7/Similarity_Score_Module',   
  download_url = 'https://github.com/sonucr7/Similarity_Score_Module/archive/v_01.tar.gz',   
  keywords = ['Similarity_Score', 'Pandas', 'neattext', 'sklearn'],   
  install_requires=[            #dependencies
          'pandas',
          'neattext',
          'numpy',
          'scikit_learn',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
  ],
)
