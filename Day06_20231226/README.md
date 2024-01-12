## 01. WordCloud_기본.ipynb   
- 사용하는 파일: alice.txt, alice_mask.png      
- WordCloud의 기본 학습 데이터로 사용되는 'alice.txt'를 사용하여 WordCloud를 그린다
- 불용어(stopwords), mask 적용을 추가적으로 학습한다   
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/72223549-94d8-4f41-b69e-64c1f260d513)

<br> 

## 02. 프로그래머스_WordCloud.ipynb   
- 데이터 크롤링을 통해 프로그래머스 질문 게시판의 질문에 달린 태그를 수집한다   
- 수집한 태그를 통해 어떤 언어나 문제들이 많이 질문되는지를 파악해볼 수 있도록 WordCloud를 그린다   
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/84c2373c-344c-4085-bdaa-bc9f69f93420)

<br> 

## 03. 크리스마스_기사_WordCloud.ipynb   
- 사용하는 파일: movie.png, NanumGothic.ttf
#### 1) 영화 키워드로 12월 25일 기사 Crawling & WordCloud
-  데이터 크롤링으로 네이버에서 2023년 12월 25일의 '영화' 키워드로 기사들의 제목을 수집한다
-  불용어(stopwords)와 mask 적용을 실습한다
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f109a08d-433b-4019-989b-3300d6e6c11e)

#### 2) 2023년 12월 25일 랭킹 기사 Crawling & WordCloud
- 2023년 12월 25일의 네이버 랭킹 기사의 제목을 데이터 크롤링으로 수집한다
- 불용어(stopwords)와 mask 적용을 실습한다
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/2d97521b-a2eb-409a-85e8-8e293866ce09)

<br> 

## 04. 한글 텍스트_WordCloud.ipynb
- 사용하는 파일: hangul_text.txt, star.png, music.png, NanumGothic.ttf
- hangul_text.txt의 한글 텍스트에 대해 불용어 처리 후 counter를 기반으로 WordCloud를 만든다
- 한글 텍스트를 간단히 처리하여 wordcloud를 그린 결과 해당 텍스트가 마포구, 상암의 맛집에 대한 리뷰를 담고 있다는 것을 추론해볼 수 있다
- konlpy(한국어 자연어 처리를 위한 라이브러리, 한국어 형태소 분석기를 포함)를 활용하여 처리한 후 WordCloud를 그려 비교
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/40305ba4-e0cf-4f6c-810d-336965139711)
