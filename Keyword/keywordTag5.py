from konlpy.tag import Okt

text = '밥도둑 지코바 양념치킨~~ 한번 우동 사리를 추가 해 먹어봤어요 강추드려요!!!! 지코바는 마무리로 치밥인거 알죠?'

spliter = Okt()
nouns = spliter.nouns(text)

print(nouns)
