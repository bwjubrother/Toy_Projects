from soykeyword.lasso import LassoKeywordExtractor

# lassobased_extractor = LassoKeywordExtractor(min_tf=20, min_df=10)
# lassobased_extractor.train(x, index2word) # x: sparse matrix

lassobased_extractor = LassoKeywordExtractor(
    costs=[500, 200, 100, 50, 10, 5, 1, 0.1], min_tf=20, min_df=10)

documents = [
    '밥도둑 지코바 양념치킨~~ 한번 우동 사리를 추가 해 먹어봤어요 강추드려요!!!! 지코바는 마무리로 치밥인거 알죠?'
]

keywords = lassobased_extractor.extract_from_docs(documents,
                                                  min_num_of_keywords=30)

lassobased_extractor.extract_from_word('음식', min_num_of_keywords=30)

print(keywords)