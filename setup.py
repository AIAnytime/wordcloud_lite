from distutils.core import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'wordcloud_lite',    
  long_description=long_description,
  long_description_content_type='text/markdown',    
  packages = ['wordcloud_lite'],   
  version = '1.2',      
  license='MIT',        
  description = 'Generate Word Cloud with ease.',   
  author = 'Sonu Kumar',                   
  author_email = 'sonu1000raw@gmail.com',      
  url = 'https://github.com/sonucr7/wordcloud_lite',   
  download_url = 'https://github.com/sonucr7/wordcloud_lite/archive/v_01.tar.gz',   
  keywords = ['WordCloud', 'NLP', 'nltk'],   
  install_requires=[            #dependencies
          'wordcloud',
          'matplotlib',
          'nltk',
          'pillow'
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