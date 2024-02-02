# 챗봇 엔진 만들기

## 모듈 설치

```
pip install konlpy
pip install seqeval
pip install tensorflow
```

- 위의 모듈을 가상 환경에서 설치한다

<br>

## 전처리 과정

```python
from konlpy.tag import Komoran
import pickle

class Preprocess:
	# 생성자
	def __init__(self, word2index_dic="", userdic=None):
		# 단어 인덱스 사전 불러오기
		if word2index_dic != "":
			f = open(word2index_dic, "rb")
			self.word_index = pickle.load(f)
			f.close()
		else:
			self.word_index = None

		# 형태소 분석기 초기화
		self.komoran = Komoran(userdic=userdic)

		# 제외할 품사
		# 참조: https://docs.komoran.kr/firststep/postypes.html
		self.exclusion_tags = [
			"JKS", "JKC", "JKG", "JKO", "JKB", "JKV", "JKQ", "JX", "JC", # 관계언 제거
			"SF", "SP", "SS", "SE", "SO", # 기호 제거
			"EP", "EF", "EC", "ETN", "ETM", # 어미 제거
			"XSN", "XSV", "XSA", # 접미사 제거
		]

	# 형태소 분석기 POS tagger (래퍼 함수)
	def pos(self, sentence):
		return self.komoran.pos(sentence)

	# 불용어 제거 후 필요한 품사 정보만 가져오기
	def get_keywords(self, pos, without_tag=False):
		f = lambda x: x in self.exclusion_tags
		word_list = []
		for p in pos:
			if f(p[1]) is False: # 불용어 리스트에 없는 경우에만 저장
				word_list.append(p if without_tag is False else p[0])
		return word_list

	# 키워드를 단어 인덱스 시퀀스로 변환
	def get_wordidx_sequence(self, keywords):
		if self.word_index is None:
			return []
		w2i = []
		for word in keywords:
			try:
				w2i.append(self.word_index[word])
			except KeyError:
				# 해당 단어가 사전에 없는 경우 OOV 처리
				w2i.append(self.word_index["OOV"])
		return w2i
```

- /utils 폴더에 user_dic.tsv 파일 추가 (사용자 정의 사전)
- /utils 폴더에 전처리를 담당할 Preprocess.py 파일을 위의 코드로 작성한다

<br>

```python
import sys
sys.path.append('c:/src/chatbot')

from utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing

sent = "내일 오전 10시에 짬뽕 주문하고 싶어ㅋㅋ"
p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic = '../utils/user_dic.tsv')

pos = p.pos(sent)
keywords = p.get_keywords(pos, without_tag=False)

print(keywords)

# w2i = p.get_wordidx_sequence(keywords)
# sequences = [w2i]
#
# MAX_SEQ_LEN = 15    # 임베딩 벡터 크기
# padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')
#
# print(keywords)
# print(sequences)
# print(padded_seqs)
```

- /test 폴더에 preprocess_test.py 파일 생성해서 방금 만든 단어 인덱스 사전 파일을 불러와 데이터 확인하기

<img width="596" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/24035033-35e8-4e0c-a148-576a7cfd6cff">

<br><br>

## 단어 사전 구축 및 시퀀스 생성

```python
import sys
sys.path.append('c:/src/chatbot')
from utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

# 말뭉치 데이터 읽어오기
def read_corpus_data(filename):
	with open(filename, "r", encoding='utf8') as f:
		data = [line.split("\t") for line in f.read().splitlines()]
		data = data[1:] # 헤더 제거
	return data

# 말뭉치 데이터 가져오기
corpus_data = read_corpus_data("./corpus.txt")

# 말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess()
dict = []
for c in corpus_data:
	pos = p.pos(c[1])
	for k in pos:
		dict.append(k[0])

# 사전에 사용될 단어 인덱스 딕셔너리(word_index) 생성
tokenizer = preprocessing.text.Tokenizer(oov_token="OOV")
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

# 사전 파일 생성
f = open("chatbot_dict.bin", "wb")
try:
	pickle.dump(word_index, f)
except Exception as e:
	print(e)
finally:
	f.close()
```

- /train_tools/dict 경로에 corpus.txt 말뭉치 파일 추가
- /train_tools/dict/ 에 create_dict.py 생성 후 위의 코드를 작성한다
- "python create_dict.py"로 해당 파일을 실행하여 chatbot.bin을 생성한다

<br>

<img width="788" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4d10f53a-2dac-4be8-b2cf-de3b019c67e4">

- cf) 만약 위와 같은 오류(JVMNotFoundException)가 발생한다면, 이는 Java가 설치되지 않았거나 Java가 설치되어도 환경 변수가 설정되지 않은 것이다
- https://chan-lab.tistory.com/15 : 이 링크에서 설명하는 방식으로 Java를 설치한 후 시스템 환경변수에서 jvm.dll이 있는 파일을 환경변수 경로로 설정해주면 오류가 해결된다

<br>

## 단어사전 테스트

```python
import sys
sys.path.append('c:/src/chatbot')
import pickle
from utils.Preprocess import Preprocess

# 단어 사전 불러오기
f = open("../train_tools/dict/chatbot_dict.bin", "rb")
word_index = pickle.load(f)
f.close()

sent = "내일 오전 10시에 탕수육 주문하고 싶어 ㅋㅋ"

# 전처리 객체 생성
p = Preprocess(userdic='../utils/user_dic.tsv')

# 형태소분석기 실행
pos = p.pos(sent)

# 품사 태그 없이 키워드 출력
keywords = p.get_keywords(pos, without_tag=True)
for word in keywords:
    try:
        print(word, word_index[word])
    except KeyError:
        # 해당 단어가 사전에 없는 경우, OOV 처리
        print(word, word_index['OOV'])
```

- /test 폴더에 chatbot_dict_test.py 파일 생성 후 아래 코드 작성
- "python chatbot_dict_test.py"로 실행하면 아래와 같은 결과가 나타난다

<img width="346" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/0a148ecd-6f07-437b-92ba-e564ea79bc22">

- "내일 오전 10시에 탕수육 주문하고 싶어 ㅋㅋ" 문장에 대해 우리가 설정한 태그 위주로 토큰을 가져왔다

<br>

## 의도 분류 모델 학습

```python
# 단어 시퀀스 벡터 크기
MAX_SEQ_LEN =15

def GlobalParams():
	global MAX_SEQ_LEN
```

```python
# 필요한 모듈 임포트
import pandas as pd
import tensorflow as tf
from tensorflow.keras import preprocessing
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout, Conv1D, GlobalMaxPool1D, concatenate

# 데이터 읽어오기
train_file = "total_train_data.csv"
data = pd.read_csv(train_file, delimiter=',')
queries = data['query'].tolist()
intents = data['intent'].tolist()

import sys
sys.path.append('c:/src/chatbot')
from utils.Preprocess import Preprocess
p = Preprocess(word2index_dic='../../train_tools/dict/chatbot_dict.bin',
               userdic='../../utils/user_dic.tsv')

# 단어 시퀀스 생성
sequences = []
for sentence in queries:
    pos = p.pos(sentence)
    keywords = p.get_keywords(pos, without_tag=True)
    seq = p.get_wordidx_sequence(keywords)
    sequences.append(seq)

# 단어 인덱스 시퀀스 벡터 
# 단어 시퀀스 벡터 크기
from config.globalparams import MAX_SEQ_LEN
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

# (105658, 15)
print(padded_seqs.shape)
print(len(intents)) #105658

# 학습용, 검증용, 테스트용 데이터셋 생성 
# 학습셋:검증셋:테스트셋 = 7:2:1
ds = tf.data.Dataset.from_tensor_slices((padded_seqs, intents))
ds = ds.shuffle(len(queries))

train_size = int(len(padded_seqs) * 0.7)
val_size = int(len(padded_seqs) * 0.2)
test_size = int(len(padded_seqs) * 0.1)

train_ds = ds.take(train_size).batch(20)
val_ds = ds.skip(train_size).take(val_size).batch(20)
test_ds = ds.skip(train_size + val_size).take(test_size).batch(20)

# 하이퍼 파라미터 설정
dropout_prob = 0.5
EMB_SIZE = 128
EPOCH = 5
VOCAB_SIZE = len(p.word_index) + 1 #전체 단어 개수

# CNN 모델 정의 
input_layer = Input(shape=(MAX_SEQ_LEN,))
embedding_layer = Embedding(VOCAB_SIZE, EMB_SIZE, input_length=MAX_SEQ_LEN)(input_layer)
dropout_emb = Dropout(rate=dropout_prob)(embedding_layer)

conv1 = Conv1D(
    filters=128,
    kernel_size=3,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool1 = GlobalMaxPool1D()(conv1)

conv2 = Conv1D(
    filters=128,
    kernel_size=4,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool2 = GlobalMaxPool1D()(conv2)

conv3 = Conv1D(
    filters=128,
    kernel_size=5,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool3 = GlobalMaxPool1D()(conv3)

# 3,4,5gram 이후 합치기
concat = concatenate([pool1, pool2, pool3])

hidden = Dense(128, activation=tf.nn.relu)(concat)
dropout_hidden = Dropout(rate=dropout_prob)(hidden)
logits = Dense(5, name='logits')(dropout_hidden)
predictions = Dense(5, activation=tf.nn.softmax)(logits)

# 모델 생성 
model = Model(inputs=input_layer, outputs=predictions)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습 
model.fit(train_ds, validation_data=val_ds, epochs=EPOCH, verbose=1)

# 모델 평가(테스트 데이터 셋 이용) 
loss, accuracy = model.evaluate(test_ds, verbose=1)
print('Accuracy: %f' % (accuracy * 100))
print('loss: %f' % (loss))

# 모델 저장  
model.save('intent_model.h5')
```

- 문장의 의도 클래스별로 분류하기 위해 이전에 사용한 CNN 사용
- /config 폴더에 globalparams.py 파일 생성 후 코드 작성
- /model/intent 폴더에 total_train_data.csv 추가
- /model/intent 폴더에 train_model.py 생성 후 코드 작성
- "python train_model.py"로 실행하여 학습한 모델을 생성(intent_model.h5 생성)

<img width="746" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/08e057ab-928d-446f-9c55-74e9facff690">

<br><br>

### 의도 분류 모듈 생성

```python
import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing


# 의도 분류 모델 모듈
class IntentModel:
    def __init__(self, model_name, proprocess):

        # 의도 클래스 별 레이블
        self.labels = {0: "인사", 1: "욕설", 2: "주문", 3: "예약", 4: "기타"}

        # 의도 분류 모델 불러오기
        self.model = load_model(model_name)

        # 챗봇 Preprocess 객체
        self.p = proprocess


    # 의도 클래스 예측
    def predict_class(self, query):
        # 형태소 분석
        pos = self.p.pos(query)

        # 문장내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]

        # 단어 시퀀스 벡터 크기
        from config.GlobalParams import MAX_SEQ_LEN

        # 패딩처리
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

        predict = self.model.predict(padded_seqs)
        predict_class = tf.math.argmax(predict, axis=1)
        return predict_class.numpy()[0]
```

```python
import sys
sys.path.append('c:/src/chatbot')
from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.tsv')

intent = IntentModel(model_name='../models/intent/intent_model.h5', proprocess=p)

query = "오늘 탕수육 주문 가능한가요?"
# query = "씨벌 전화좀 받아라"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 :", predict)
print("의도 예측 레이블 :", predict_label)
```

- /model/intent 폴더에 IntentModel.py 파일 생성 후 아래 코드 작성
- /test 폴더에 model_intent_test.py 파일 추가
- "python model_intent_test.py" 실행하여 결과 확인

<img width="300" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4062188b-d830-49d4-8249-8c5aed0b9fb8">
<img width="300" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d05c2934-e7d1-4c71-884a-868af5589673">

<br><br>

## 개체명 인식 모델 학습

```python
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
import sys
sys.path.append('c:/flyai/chatbot')
from utils.Preprocess import Preprocess

# 학습 파일 불러오기
def read_file(file_name):
    sents = []
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for idx, l in enumerate(lines):
            if l[0] == ';' and lines[idx + 1][0] == '$':
                this_sent = []
            elif l[0] == '$' and lines[idx - 1][0] == ';':
                continue
            elif l[0] == '\n':
                sents.append(this_sent)
            else:
                this_sent.append(tuple(l.split()))
    return sents

p = Preprocess(word2index_dic='../../train_tools/dict/chatbot_dict.bin',
               userdic='../../utils/user_dic.tsv')

# 학습용 말뭉치 데이터를 불러옴
corpus = read_file('ner_train.txt')

# 말뭉치 데이터에서 단어와 BIO 태그만 불러와 학습용 데이터셋 생성
sentences, tags = [], []
for t in corpus:
    tagged_sentence = []
    sentence, bio_tag = [], []
    for w in t:
        tagged_sentence.append((w[1], w[3]))
        sentence.append(w[1])
        bio_tag.append(w[3])
    
    sentences.append(sentence)
    tags.append(bio_tag)


print("샘플 크기 : \n", len(sentences))
print("0번 째 샘플 단어 시퀀스 : \n", sentences[0])
print("0번 째 샘플 bio 태그 : \n", tags[0])
print("샘플 단어 시퀀스 최대 길이 :", max(len(l) for l in sentences))
print("샘플 단어 시퀀스 평균 길이 :", (sum(map(len, sentences))/len(sentences)))

# 토크나이저 정의
tag_tokenizer = preprocessing.text.Tokenizer(lower=False) # 태그 정보는 lower=False 소문자로 변환하지 않는다.
tag_tokenizer.fit_on_texts(tags)

# 단어사전 및 태그 사전 크기
vocab_size = len(p.word_index) + 1
tag_size = len(tag_tokenizer.word_index) + 1
print("BIO 태그 사전 크기 :", tag_size)
print("단어 사전 크기 :", vocab_size)

# 학습용 단어 시퀀스 생성
x_train = [p.get_wordidx_sequence(sent) for sent in sentences]
y_train = tag_tokenizer.texts_to_sequences(tags)

index_to_ner = tag_tokenizer.index_word # 시퀀스 인덱스를 NER로 변환 하기 위해 사용
index_to_ner[0] = 'PAD'

# 시퀀스 패딩 처리
max_len = 40
x_train = preprocessing.sequence.pad_sequences(x_train, padding='post', maxlen=max_len)
y_train = preprocessing.sequence.pad_sequences(y_train, padding='post', maxlen=max_len)

# 학습 데이터와 테스트 데이터를 8:2의 비율로 분리
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train,
                                                    test_size=.2,
                                                    random_state=1234)

# 출력 데이터를 one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train, num_classes=tag_size)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=tag_size)

print("학습 샘플 시퀀스 형상 : ", x_train.shape)
print("학습 샘플 레이블 형상 : ", y_train.shape)
print("테스트 샘플 시퀀스 형상 : ", x_test.shape)
print("테스트 샘플 레이블 형상 : ", y_test.shape)


# 모델 정의 (Bi-LSTM)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
from tensorflow.keras.optimizers import Adam

model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=30, input_length=max_len, mask_zero=True))
model.add(Bidirectional(LSTM(200, return_sequences=True, dropout=0.50, recurrent_dropout=0.25)))
model.add(TimeDistributed(Dense(tag_size, activation='softmax')))
model.compile(loss='categorical_crossentropy', optimizer=Adam(0.01), metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=128, epochs=10)

print("평가 결과 : ", model.evaluate(x_test, y_test)[1])
model.save('ner_model.h5')


# 시퀀스를 NER 태그로 변환
def sequences_to_tag(sequences):  # 예측값을 index_to_ner를 사용하여 태깅 정보로 변경하는 함수.
    result = []
    for sequence in sequences:  # 전체 시퀀스로부터 시퀀스를 하나씩 꺼낸다.
        temp = []
        for pred in sequence:  # 시퀀스로부터 예측값을 하나씩 꺼낸다.
            pred_index = np.argmax(pred)  # 예를 들어 [0, 0, 1, 0 ,0]라면 1의 인덱스인 2를 리턴한다.
            temp.append(index_to_ner[pred_index].replace("PAD", "O"))  # 'PAD'는 'O'로 변경
        result.append(temp)
    return result


# f1 스코어 계산을 위해 사용
from seqeval.metrics import f1_score, classification_report

# 테스트 데이터셋의 NER 예측
y_predicted = model.predict(x_test)
pred_tags = sequences_to_tag(y_predicted) # 예측된 NER
test_tags = sequences_to_tag(y_test)    # 실제 NER

# F1 평가 결과
print(classification_report(test_tags, pred_tags))
print("F1-score: {:.1%}".format(f1_score(test_tags, pred_tags)))
```

- 챗봇 엔진에 입력된 문장 의도 분류 후, 문장 내 개체명 인식(Named Entity Regocnition, NER) 모델 만들기
- /models/ner 폴더에 ner_train.txt 파일 추가 (학습 데이터셋)
- /models/ner 폴더에 train_model.py 파일 생성 아래 코드 작성
- "python train_model.py"로 실행하여 학습된 NER 모델 파일 생성(ner_model.h5)

<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d24c693e-def8-42ac-ae45-ee39f9fea490">

<br><br>

## 개체명 인식 모듈 생성

```python
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing


# 개체명 인식 모델 모듈
class NerModel:
    def __init__(self, model_name, proprocess):

        # BIO 태그 클래스 별 레이블
        self.index_to_ner = {1: 'O', 2: 'B_DT', 3: 'B_FOOD', 4: 'I', 5: 'B_OG', 6: 'B_PS', 7: 'B_LC', 8: 'NNP', 9: 'B_TI', 0: 'PAD'}

        # 의도 분류 모델 불러오기
        self.model = load_model(model_name)

        # 챗봇 Preprocess 객체
        self.p = proprocess


    # 개체명 클래스 예측
    def predict(self, query):
        # 형태소 분석
        pos = self.p.pos(query)

        # 문장내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]

        # 패딩처리
        max_len = 40
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, padding="post", value=0, maxlen=max_len)

        predict = self.model.predict(np.array([padded_seqs[0]]))
        predict_class = tf.math.argmax(predict, axis=-1)

        tags = [self.index_to_ner[i] for i in predict_class.numpy()[0]]
        return list(zip(keywords, tags))

    def predict_tags(self, query):
        # 형태소 분석
        pos = self.p.pos(query)

        # 문장내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]

        # 패딩처리
        max_len = 40
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, padding="post", value=0, maxlen=max_len)

        predict = self.model.predict(np.array([padded_seqs[0]]))
        predict_class = tf.math.argmax(predict, axis=-1)

        tags = []
        for tag_idx in predict_class.numpy()[0]:
            if tag_idx == 1: continue
            tags.append(self.index_to_ner[tag_idx])

        if len(tags) == 0: return None
        return tags
```

```python
import sys
sys.path.append('c:/flyai/chatbot')
from utils.Preprocess import Preprocess
from models.ner.NerModel import NerModel

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.tsv')


ner = NerModel(model_name='../models/ner/ner_model.h5', proprocess=p)
query = '오늘 오전 13시 2분에 탕수육 주문 하고 싶어요'
predicts = ner.predict(query)
tags = ner.predict_tags(query)
print(predicts)
print(tags)
```

- 앞서 학습한 개체명 인식 모델 파일을 활용해 입력 문장 내부의 개체명을 인식하는 챗봇 엔진의 개체명 인식 모듈을 만들기
- /models/ner 폴더에 NerModel.py 파일 생성 후 코드 작성(챗봇 엔진 NER 모델 모듈)
- /test 폴더에 model_ner_test.py 파일 생성 후 아래 코드 작성(NerModel 객체 사용)
- "python model_ner_test.py" 실행하여 개체명 인식이 잘 되는지 확인

<br><br>

## 답변 검색

- 다양한 플랫폼에서 언제든지 사용할 수 있도록 서버용 프로그램을 만들기
  
```python
import pymysql
import pymysql.cursors
import logging

class Database:
    '''
    database 제어
    '''

    def __init__(self, host, user, password, db_name, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.db_name = db_name
        self.conn = None

    # DB 연결
    def connect(self):
        if self.conn != None:
            return

        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db_name,
            charset=self.charset
        )

    # DB 연결 닫기
    def close(self):
        if self.conn is None:
            return

        if not self.conn.open:
            self.conn = None
            return
        self.conn.close()
        self.conn = None

    # SQL 구문 실행
    def execute(self, sql):
        last_row_id = -1
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
            self.conn.commit()
            last_row_id = cursor.lastrowid
            # logging.debug("excute last_row_id : %d", last_row_id)
        except Exception as ex:
            logging.error(ex)

        finally:
            return last_row_id

    # SELECT 구문 실행 후, 단 1개의 데이터 ROW만 불러옴
    def select_one(self, sql):
        result = None

        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        except Exception as ex:
            logging.error(ex)

        finally:
            return result

    # SELECT 구문 실행 후, 전체 데이터 ROW만 불러옴
    def select_all(self, sql):
        result = None

        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception as ex:
            logging.error(ex)

        finally:
            return result
```

- 다양한 플랫폼에서 언제든지 사용할 수 있도록 서버용 프로그램을 만들기
  
```python
class FindAnswer:
    def __init__(self, db):
        self.db = db

    # 검색 쿼리 생성
    def _make_query(self, intent_name, ner_tags):
        sql = "select * from chatbot_train_data"
        if intent_name != None and ner_tags == None:
            sql = sql + " where intent='{}' ".format(intent_name)

        elif intent_name != None and ner_tags != None:
            where = ' where intent="%s" ' % intent_name
            if (len(ner_tags) > 0):
                where += 'and ('
                for ne in ner_tags:
                    where += " ner like '%{}%' or ".format(ne)
                where = where[:-3] + ')'
            sql = sql + where

        # 동일한 답변이 2개 이상인 경우, 랜덤으로 선택
        sql = sql + " order by rand() limit 1"
        return sql

    # 답변 검색
    def search(self, intent_name, ner_tags):
        # 의도명, 개체명으로 답변 검색
        sql = self._make_query(intent_name, ner_tags)
        answer = self.db.select_one(sql)

        # 검색되는 답변이 없으면 의도명만 검색
        if answer is None:
            sql = self._make_query(intent_name, None)
            answer = self.db.select_one(sql)

        return (answer['answer'], answer['answer_image'])

    # NER 태그를 실제 입력된 단어로 변환
    def tag_to_word(self, ner_predicts, answer):
        for word, tag in ner_predicts:

            # 변환해야하는 태그가 있는 경우 추가
            if tag == 'B_FOOD' or tag == 'B_DT' or tag == 'B_TI':
                answer = answer.replace(tag, word)

        answer = answer.replace('{', '')
        answer = answer.replace('}', '')
        return answer
```

- 챗봇의 답변 검색은 그 자체만으로도 방대한 양의 지식을 필요로 하는 분야이지만 이 게시글에서는 단순한 SQL구문을 사용해 룰 베이스 기반으로 답변을 검색하는 방법
- /utils 폴더에 Database.py 파일 생성 후 위의 코드 작성(데이터베이스 제어 모듈 생성)
- /utils 폴더에 FindAnswer.py 파일 생성 후 아래 코드 작성(답변 검색 모듈 생성)

<br>

## 챗봇 엔진 서버 개발

```python
import socket

class BotServer:
    def __init__(self, srv_port, listen_num):
        self.port = srv_port
        self.listen = listen_num
        self.mySock = None

    # sock 생성
    def create_sock(self):
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySock.bind(("0.0.0.0", int(self.port)))
        self.mySock.listen(int(self.listen))
        return self.mySock

    # client 대기
    def ready_for_client(self):
        return self.mySock.accept()

    # sock 반환
    def get_sock(self):
        return self.mySock
```

- /utils 폴더에 BotServer.py 파일 생성 후 아래 코드 작성(다중 접속을 위한 TCP 소켓 서버)

```python
import threading
import json

from config.DatabaseConfig import *
from utils.Database import Database
from utils.BotServer import BotServer
from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel
from models.ner.NerModel import NerModel
from utils.FindAnswer import FindAnswer


# 전처리 객체 생성
p = Preprocess(word2index_dic='train_tools/dict/chatbot_dict.bin',
               userdic='utils/user_dic.tsv')

# 의도 파악 모델
intent = IntentModel(model_name='models/intent/intent_model.h5', proprocess=p)

# 개체명 인식 모델
ner = NerModel(model_name='models/ner/ner_model.h5', proprocess=p)


def to_client(conn, addr, params):
    db = params['db']

    try:
        db.connect()  # 디비 연결

        # 데이터 수신
        read = conn.recv(2048)  # 수신 데이터가 있을 때 까지 블로킹
        print('===========================')
        print('Connection from: %s' % str(addr))

        if read is None or not read:
            # 클라이언트 연결이 끊어지거나, 오류가 있는 경우
            print('클라이언트 연결 끊어짐')
            exit(0)


        # json 데이터로 변환
        recv_json_data = json.loads(read.decode())
        print("데이터 수신 : ", recv_json_data)
        query = recv_json_data['Query']

        # 의도 파악
        intent_predict = intent.predict_class(query)
        intent_name = intent.labels[intent_predict]

        # 개체명 파악
        ner_predicts = ner.predict(query)
        ner_tags = ner.predict_tags(query)


        # 답변 검색
        try:
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(ner_predicts, answer_text)

        except:
            answer = "죄송해요 무슨 말인지 모르겠어요. 조금 더 공부 할게요."
            answer_image = None

        send_json_data_str = {
            "Query" : query,
            "Answer": answer,
            "AnswerImageUrl" : answer_image,
            "Intent": intent_name,
            "NER": str(ner_predicts)
        }
        message = json.dumps(send_json_data_str)
        conn.send(message.encode())

    except Exception as ex:
        print(ex)

    finally:
        if db is not None: # db 연결 끊기
            db.close()
        conn.close()


if __name__ == '__main__':

    # 질문/답변 학습 디비 연결 객체 생성
    db = Database(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
    )
    print("DB 접속")

    port = 5050
    listen = 100

    # 봇 서버 동작
    bot = BotServer(port, listen)
    bot.create_sock()
    print("bot start")

    while True:
        conn, addr = bot.ready_for_client()
        params = {
            "db": db
        }

        client = threading.Thread(target=to_client, args=(
            conn,
            addr,
            params
        ))
        client.start()
```

- /chatbot/ 루트 폴드에 bot.py 파일 추가후 코드 작성
- python bot.py으로 파일 실행행

```python
import socket
import json

# 챗봇 엔진 서버 접속 정보
host = "127.0.0.1"  # 챗봇 엔진 서버 IP 주소
port = 5050  # 챗봇 엔진 서버 통신 포트

# 클라이언트 프로그램 시작
while True:
    print("질문 : ")
    query = input()  # 질문 입력
    if(query == "exit"):
        exit(0)
    print("-" * 40)

    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
        'BotType': "MyService"
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)
    print("답변 : ")
    print(ret_data['Answer'])
    print(ret_data)
    print(type(ret_data))
    print("\n")

    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()
```

- /test 폴더에 chatbot_client_test.py 파일 생성 후 코드 작성 (챗봇 테스트 클라이언트 프로그램)
- python chatbot_client_test.py로 파일 실행


