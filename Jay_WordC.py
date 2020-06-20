from wordcloud import WordCloud
from PIL import Image
import numpy as np

f3 = open('Update2.txt','r')
text = f3.read()
jay_mask = np.array(Image.open('Jay_mask.png'))
wc = WordCloud(background_color='white',
               mask=jay_mask,
               prefer_horizontal=0.95,
               font_path='msyh.ttf',
               max_font_size=42,
               contour_width=2,
               contour_color='steelblue')

wc.generate(text)
wc.to_file('Jay_WordC.png')
f3.close()