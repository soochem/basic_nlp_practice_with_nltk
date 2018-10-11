# -*- coding: utf-8 -*-
# Sumin Seo
# Computer Linguistic Basic

import nltk
#nltk.download()
from nltk.stem import PorterStemmer
from nltk.book import *

## python basics
# <, ==, !=
# functions: startswith(), endswith(), t in s, islower(), isupper(), isalpha()
# isalnum(), isdigit(), istitle()

# ~으로 끝나는 text1의 모든 단어를 정렬하라
sorted(w for w in set(text1) if w.endswith('ableness'))

# function set()
# 문장의 길이와 set 길이 차이를 알아보자
print(len(text1))
print(len(set(word.lower() for word in text1)))

## file load
f = open("example.txt")
for line in f.readlines():
    print(line)
f.close()

## collocation with words
text1.concordance('monstrous')
text2.common_contexts(["monstrous", "very"])

### Text Normalization
#1 Segmenting(tokenizing)
#2 Normalizing - case folding, lemmatization, stemming

## tokenization
from nltk.tokenize import word_tokenize

f = open("example.txt")
tokens = []

for line in f.readlines():
    token = word_tokenize(line)
    for i in token:
        tokens.append(i)
print(tokens)
f.close()

## POS tagging
tagged = nltk.pos_tag(tokens)
print(tagged)

## stemming
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()

text1 = "He is running faster than her."
text2 = "My cats are swimming in the pool with the birds"
text3 = "He is taller than me"

ps.stem("loving")
ps.stem("cars")
ps.stem("children")  # not work
ps.stem("feet")  # not work

# 토큰화 먼저 해야함, 잘못된 예시
for w in text1:
    print(ps.stem(w))

## lemmatization
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()

# 동사랑 형용사는 잘 안됨
lem.lemmatize("running")
lem.lemmatize("supported")
lem.lemmatize("best")

# lemmatize 함수는 2 arguments를 취하는 함수, 토큰과 품사(default = 'n')
lem.lemmatize("running", pos='v')
lem.lemmatize("supported", pos='v')
lem.lemmatize("been", pos='v')
lem.lemmatize("happier", pos='a')
lem.lemmatize("worst", pos='a')
lem.lemmatize("worse", pos='a')

sent = "The children were given a book."
tokens = nltk.word_tokenize(sent)
tag = nltk.pos_tag(tokens)

# sent의 token을 모두 원형(lemma) 형태로 반환해보자
# 1번째 방법
lemList = []
for i in tag :
    if (i[1] in ('VBP','VBG','VBN','VBD','VBZ')):
        lemWord = lem.lemmatize(i[0], pos='v')
    else:
        lemWord = lem.lemmatize(i[0])
    lemList.append(lemWord)

# 2번째 방법
lemList2 = []
for (a, b) in tag:
    if a != '.':
        if b.startswith('JJ'):
            lemList2 += [lem.lemmatize(a, pos='a')]
        elif b.startswith('V'):
            lemList2 += [lem.lemmatize(a, pos='v')]
        elif b.startswith('R'):
            lemList2 += [lem.lemmatize(a, pos='r')]
        else:
            lemList2 += [lem.lemmatize(a)]
    else:
        lemList2 += [a]

print(lemList)
print(lemList2)

# 주의사항
# for word in tag -> (token, pos) 형식으로 되어 있어야함
# word [1] -> 'nns' -> n 으로 바꾸기
# tuple unchangable


from nltk.corpus import wordnet as wn
print(wn.synsets('coffee'))
print(wn.synsets('net'))

cat = wn.synset("cat.n.01")

coffee = wn.synsets("coffee")[0]
bus = wn.synsets("bus")[0]
ship = wn.synsets("ship")[0]

print(ship.wup_similarity(coffee))
print(ship.wup_similarity(bus))