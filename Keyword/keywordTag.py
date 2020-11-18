from konlpy.tag import Kkma
from konlpy.tag import Okt
from krwordrank.sentence import summarize_with_sentences

kkma = Kkma()
okt = Okt()

import sys
import os
import re
sys.path.append(os.path.dirname('PyKoSpacing/'))
# from pykospacing import spacing


def preprocessing(review):
    total_review = ''

    sentence = review
    sentence = re.sub('\n', '', sentence)
    sentence = re.sub('\u200b', '', sentence)
    sentence = re.sub('\xa0', '', sentence)
    sentence = re.sub('([a-zA-Z])', '', sentence)
    sentence = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', '', sentence)
    sentence = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '',
                      sentence)
    sentence = okt.pos(sentence, stem=True)
    word = []
    for i in sentence:
        if not i[1] == 'Noun':
            continue
        if len(i[0]) == 1:
            continue
        word.append(i[0])
    word = ' '.join(word)
    word += '. '
    total_review += word
    return total_review


texts = [
    '밥도둑 지코바 양념치킨~~', '한번 우동 사리를 추가 해 먹어봤어요', '강추드려요!!!!', '지코바는 마무리로 치밥인거 알죠?'
]
text = ['밥도둑 지코바 양념치킨~~ 한번 우동 사리를 추가 해 먹어봤어요 강추드려요!!!! 지코바는 마무리로 치밥인거 알죠?']

# blog_list = []

# for k in blog.keys():
#     if len(blog[k]) == 0:
#         continue
#     blog_list.append(k)

stop = 0

test = text
st = ''
for r in range(len(test)):
    texts = test[r]
    texts = preprocessing(texts)
    st += texts
texts = st.split('. ')

stopwords = {}
keywords, sents = summarize_with_sentences(texts,
                                           stopwords=stopwords,
                                           num_keywords=100,
                                           num_keysents=10)

print(keywords)
for word, r in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:5]:
    #print('%8s:\t%.4f' % (word, r))
    print('#%s' % word)
print()