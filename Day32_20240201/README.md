## 감정분석 모델

<br>

## 챗봇 학습 툴 만들기

### 챗봇 엔진 입력 처리 과정

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/23edd061-6664-4fd2-8333-693c09e4f2b5">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/71c9eac0-9030-47fe-b14a-6890c8e1cf71">

- 입력되는 문장을 자연어 처리하여 해당 문장의 의도, 개체명, 키워드 정보 등을 추출
- 엔진에서 해석한 결과를 이용해 학습 DB 내용을 검색
- 이때 해석 결과(의도, 개체명)에 매칭되는 답변 정보가 DB에 존재하면 데이터를 불러와 사용자에게 답변으로 제공

<br>

### 프로젝트 구조

<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e4eede76-4380-404d-9e9f-3081003bf012">
- train_tools: 챗봇 학습툴 관련 파일
- models: 챗봇 엔진에서 사용하는 딥러닝 모델 관련 파일
- intent: 의도 분류 모델 관련 파일
- ner: 개체 인식 모델 관련 파일
- utils: 챗봇 개발에 필요한 유틸리티 라이브러리
- config: 챗봇 개발에 필요한 설정
- test: 챗봇 개발에 필요한 테스트 코드

<br>

### 학습용 데이터베이스 설계 및 데이터 테이블 생성

<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/9b24f5cf-0e6b-4744-81b6-39fab03f9f44">

<br><br>

### 유dp 

```shell
DB_HOST = "172.23.254.237" # ipconfig로 본인 무선 LAN의 IP로 설정
DB_USER = "root"
DB_PASSWORD = "apptools"
DB_NAME = "flyai"

def DatabaseConfig():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
```

<img width="442" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/2f045279-d58f-4e3c-b729-79559a83d3c2">

- /config 폴더에 DatabaseConfig.py 파일 추가 후 위의 코드 작성
- IP는 자신의 IP 확인 후 수정 (명령 프롬프트에서 ipconfig 실행 후 무선 LAN IP 확인)

<br>

### 

```python
import pymysql
import sys
sys.path.append('c:/src/chatbot')
from config.DatabaseConfig import * # DB 접속 정보 불러오기

db = None
try:
		db = pymysql.connect(
					host=DB_HOST,
					user=DB_USER,
					passwd=DB_PASSWORD,
					db=DB_NAME,
					charset='utf8'
		)

		# 테이블 생성 sql 정의
		sql = '''
            CREATE TABLE IF NOT EXISTS chatbot_train_data (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                intent VARCHAR(45) NULL,
                ner VARCHAR(1024) NULL,
                query TEXT NULL,
                answer TEXT NOT NULL,
                answer_image VARCHAR(2048) NULL,
                PRIMARY KEY (id)
            );
		'''

		# 테이블 생성
		with db.cursor() as cursor:
				cursor.execute(sql)

except Exception as e:
		print(e)

finally:
		if db is not None:
				db.close()
```

- /train_tools/qna 폴더에 create_train_data_table.py 파일 추가 후 위의 코드 작성

 <br>
 
<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/9fe78f06-f3bc-418e-832d-700929f1f6ca">
<img width="300" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/c995ac97-420f-4261-a289-a306e87f1141">

- 명령 프롬프트에서 "python ./create_train_data_table.py"로 파일을 실행시킨다
- mysql에 접속되어 있는 프롬프트에서 "show tables;"를 하면 chatbot_train_data 테이블이 추가된 것을 알 수 있다

<br>

