from soynlp.tokenizer import RegexTokenizer
from soynlp.noun import LRNounExtractor
# import pandas as pd
# import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import re


content = '밥도둑 지코바 양념치킨~~ 한번 우동 사리를 추가 해 먹어봤어요 강추드려요!!!! 지코바는 마무리로 치밥인거 알죠?'

tokenizer = RegexTokenizer()
tokened_content = tokenizer.tokenize(content)
print(tokened_content)

# def preprocessing(text):
#     text = re.sub('\\\\n', ' ', text)
#     return text

# sentences = care['content'].apply(preprocessing)
# sentences = preprocessing(content)
# tokens = tokenizer.tokenize(content)
# print(tokens)
# print(sentences)



fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=9)

stopwords_kr = ['하지만', '그리고', '그런데', '저는','제가',
                '그럼', '이런', '저런', '합니다',
                '많은', '많이', '정말', '너무'] 


def displayWordCloud(data = None, backgroundcolor = 'white', width=800, height=600 ):
    wordcloud = WordCloud(
                        font_path = fontpath, 
                        stopwords = stopwords_kr, 
                        background_color = backgroundcolor, 
                        width = width, height = height).generate(data)
    plt.figure(figsize = (15 , 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


# noun_extractor = LRNounExtractor(verbose=True)
noun_extractor = LRNounExtractor()
nouns = noun_extractor.train_extract(content)
# nouns = noun_extractor.extract()

print(nouns)
# displayWordCloud(' '.join(nouns))