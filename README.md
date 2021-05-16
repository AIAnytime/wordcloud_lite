# wordcloud_lite
### _Lightweight WordCloud Generator_


Wordcloud_lite is a Python package to generate Word Cloud from the text data. WordCloud is a visual representation of the most common words within the text data. It is used most often for tags on the websites.

#### Few points:

- There should not be any mising value before passing the data to the generate_wordcloud method.
- It generates a fix size of the image.
- You can pass additional parameters to customize the wordcloud.

On Pypi: https://pypi.org/project/wordcloud-lite/1.2/

### Installation
```sh
pip install wordcloud-lite
```




## Dependencies

wordcloud_lite uses a number of open source packages to work properly:

- [NLTK](https://www.nltk.org/) - For text processing
- [wordcloud](https://pypi.org/project/wordcloud/) - To work on wordcloud
- [pillow](https://pypi.org/project/Pillow/) - To deal with images
- [matplotlib](https://pypi.org/project/matplotlib/) - Data Visualization package




## Uses


<a href="https://ibb.co/rtPKjqR"><img src="https://i.ibb.co/DbXPJmH/carbon.png" alt="carbon" border="0"></a>

```sh
from wordcloud_lite.wcl import WordCloudLite
import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline

data = pd.read_csv("data.csv")

#generate wordcloud
WordCloudLite.generate_wordcloud(data['column_having_text_records'])
```



## License

MIT




