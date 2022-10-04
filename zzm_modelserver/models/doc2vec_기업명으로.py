# -*- coding: utf-8 -*-
"""doc2vec 모델불러오기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CFOHQ3tQ14a0WqO2mVuZtqFijmJAOSFY
"""

from gensim.models.doc2vec import Doc2Vec

model0= Doc2Vec.load("/content/drive/MyDrive/4조/기능구현/model/ep250vec300_jiwon.doc2vec") # 지원
model1= Doc2Vec.load("/content/drive/MyDrive/4조/기능구현/model/ep250vec300_exp.doc2vec") # 경험
model2= Doc2Vec.load("/content/drive/MyDrive/4조/기능구현/model/ep250vec300_grow.doc2vec") # 성장
model3= Doc2Vec.load("/content/drive/MyDrive/4조/기능구현/model/ep250vec300_duty.doc2vec") # 직무
model4= Doc2Vec.load("/content/drive/MyDrive/4조/기능구현/model/ep250vec300_cha.doc2vec") #성격 장단점
model5= Doc2Vec.load("/content/drive/MyDrive/4조/기능구현/model/ep250vec300_iss.doc2vec") # 이슈
model6= Doc2Vec.load("/content/drive/MyDrive/4조/기능구현/model/ep250vec300_etc.doc2vec") #기타

"""지원항목이 비슷한 기업을 찾아준다"""

similar_doc = model0.docvecs.most_similar('롯데',topn=10)
print(similar_doc)

similar_doc = model0.docvecs.most_similar('엔씨소프트')
print(similar_doc)

similar_doc = model0.docvecs.most_similar('홈플러스')
print(similar_doc)

similar_doc = model0.docvecs.most_similar('대한항공')
print(similar_doc)

similar_doc = model0.docvecs.most_similar('롯데마트')
print(similar_doc)

"""경험항목이 비슷한 기업들"""

similar_doc = model1.docvecs.most_similar('롯데',topn=10)
print(similar_doc)

similar_doc = model1.docvecs.most_similar('삼성물산',topn=10)
print(similar_doc)

similar_doc = model1.docvecs.most_similar('코레일',topn=10)
print(similar_doc)

similar_doc = model1.docvecs.most_similar('KT',topn=10)
print(similar_doc)

"""자소서 작성시 성장과정이 유사한 기업들 """

similar_doc = model2.docvecs.most_similar('롯데',topn=10)
print(similar_doc)

similar_doc = model2.docvecs.most_similar('삼성',topn=10)
print(similar_doc)

similar_doc = model2.docvecs.most_similar('코오롱',topn=10)
print(similar_doc)

