# -*- coding: utf-8 -*-

#required libraries
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt


#content related
df = pd.read_csv("scrappedReviews.csv")
text = " ".join(reviews for reviews in df.reviews)
#print('There are {} words in the combination of all reviews'.format(len(text))) #816463 words
stopwords = set(STOPWORDS)


#appearance of the image
custom_mask = np.array(Image.open('cloud00.png'))

wc = WordCloud(background_color='white',
               stopwords = stopwords,
               mask = custom_mask,
               max_words = 170,
               contour_color='black',
               contour_width = 2
               )

wc.generate(text)
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)


#plotting
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()


#saving the image
wc.to_file("wc_image.png")

