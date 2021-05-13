from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import pandas as pd 
import matplotlib.pyplot as plt


from wordcloud import WordCloud
from PIL import Image

class WordCloudLite:

    def generate_wordcloud(data, bg_color = 'white',max_words=200, max_font_size=40,random_state=42,output_filename='wordCloud.png', dpi=900):
        
        words = " ".join(data)
        
        #tokenize the words to get inidividual words
        tokens = word_tokenize(words)
        
        #make it lowercases
        tokens = [t.lower() for t in tokens]
        
        #removing stopwords
        tokens = [t for t in tokens if t not in stopwords.words('english')]
        
        #removing emojis if any
        tokens = [t for t in tokens if t.isalpha()]
        
        #lemmatize word
        lemmatizer = WordNetLemmatizer()
        
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
        
        #rejoining the words
        bag_of_words = " ".join(tokens)

        generate_wc = WordCloud(background_color=bg_color,
                                max_words=max_words,
                                max_font_size=max_font_size, 
                                random_state=random_state
                                ).generate(bag_of_words)

        fig = plt.figure(1)
        plt.imshow(generate_wc)
        plt.axis('off')
        plt.show()
        fig.savefig(output_filename, dpi=dpi)


   