#-*- coding:utf-8 -*-

from wordcloud import WordCloud  
import jieba  
import PIL  
import matplotlib.pyplot as plt  
import numpy as np  

myPath = 'H:/Python/res/'


def wordcloudplot(txt):  
    path = r'H:/Python/res/font.ttf'  
    alice_mask = np.array(PIL.Image.open('H:/Python/res/butterfly.jpg'))  
    wordcloud = WordCloud(font_path=path,  
                          background_color="white",  
                          margin=5, width=1800, height=800, mask=alice_mask, max_words=2000, max_font_size=60,  
                          random_state=42)  
    wordcloud = wordcloud.generate(txt)  
    wordcloud.to_file('H:/Python/res/butterfly_result.jpg')  
    plt.imshow(wordcloud)  
    plt.axis("off")  
    plt.show()  


def main():  
    a = []  
    f = open(r'H:/Python/res/test.txt', 'r',encoding='gbk').read()  
    #f = open(r'H:\Python\res\test.txt', 'r').read()  
    words = list(jieba.cut(f))  
    for word in words:  
        if len(word) > 1:  
            a.append(word)  
    txt = r' '.join(a)  
    wordcloudplot(txt)  


if __name__ == '__main__':  
    main()  