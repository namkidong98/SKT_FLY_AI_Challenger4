## Generative AI

### chabot.py 생성하여 질문 작성 및 답변 얻어오기
```shell
python -m venv venv  # 가상 환경 생성
venv\Scripts\activate # 가상 환경 활성화

# 뒤에서부터는 (venv)로 시작
pip install openai     # (venv) C:\src\GenAI>pip install openai
pip install streamlit  # (venv) C:\src\GenAI>pip install streamlit

# chatbot.py 파일 생성
python chatbot.py  # 답변 출력
```

```python
import openai

OPENAI_API_KEY = ''                 # Azure의 키를 복사해서 붙여 넣기
OPENAI_API_ENDPOINT = 'https://sktfly2.openai.azure.com/'
OPENAI_API_TYPE = 'azure'
OPENAI_API_VERSION = '2023-05-15'   # 모델의 버전이 아니라 openai의 api의 버젼
                                    # ChatGPT의 버전이랑은 무관

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION

query = "Who is Helen Keller?"

result = openai.chat.completions.create(
    model='dev-model',
    messages=[
        {'role' : 'system', 'content' : 'You are a helpful assistant.'},
        {'role':'user','content' : query}
    ]
)

print(result.choices[0].message.content)    # 0번째 대답을 가져올 것이다
```
<img width="900" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a2bf6157-417e-456a-86c8-79ad492fc347">
<img width="900" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/75f30e7d-0200-4b62-a4be-e1d054ad7c98">

- print(result)일 때의 출력을 보고 "result.choices[0].message.content"으로 변경한다
- print(result.choices[0].message.content)로 변경한 이후 2번째 사진처럼 필요한 내용만 출력하는 것을 확인할 수 있다

<br>

<img width="578" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/63d5de9e-63ee-4284-a25f-b7ad074a7ff0">
<img width="578" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/65249d12-052e-4017-b914-5eb24c4d378e">

- query를 "input("Query? ")"로 수정하고 실행하면, 질문을 입력 받아서 위와 같이 답변을 출력하는 구조가 된다
- temperature를 추가하면 보다 다양한 답을 얻을 수 있다

<br>

### Streamlit으로 웹에 출력

<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5fcdecd3-1497-47e9-a4c3-2778f49f94ab">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/8204e183-7b44-41c4-be93-6c4bee9cff19">

```python
# streamlit.py를 생성

import streamlit as st

st.header("Welcome to GPTBot",
          divider = "rainbow")

st.write("궁금한 것을 물어보세요!")
```

- streamlit.py를 생성하고 terminal에서 streamlit run streamlit.py을 실행하면 창이 나타난다
- Markdown 문법을 사용해서 출력을 변경할 수 있다(header, write 등을 사용)

<br>

<img width="587" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/32c671d4-69e6-4eea-a4fa-d2f300b0d05a">

```python
import openai
import streamlit as st

OPENAI_API_KEY = ''
OPENAI_API_ENDPOINT = 'https://sktfly2.openai.azure.com/'
OPENAI_API_TYPE = 'azure'
OPENAI_API_VERSION = '2023-05-15'   # 모델의 버전이 아니라 openai의 api의 버젼
                                    # ChatGPT의 버전이랑은 무관

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION

st.header("Welcome to GPT Bot", divider='rainbow')
st.write("궁금한 것을 물어보세요!")

query = st.text_input("Query? ")  # terminal이 아닌 browser의 사용자에게 입력 받기

button_click = st.button("run")   # run이라는 버튼
if button_click:                  # button이 클릭되었을 때만
    result = openai.chat.completions.create(
        model='dev-model',
        temperature=1,  # 0이 기본값이고 1이면 보다 창의적인 답을 제시
        messages=[
            {'role' : 'system', 'content' : 'You are a helpful assistant.'},
            {'role':'user','content' : query}
        ]
    )
    st.write(result.choices[0].message.content)    # 0번째 대답을 가져와서 화면에 출력 
```

- chatbot.py를 위와 같이 수정한 이후, streamlit run chatbot.py를 terminal에서 실행하면 위와 같은 웹 페이지가 나오게 된다
- 텍스트 공간에 질문을 입력한 이후 run 버튼을 누르면 답을 아래에 적는게 나오게 된다

<br>

<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/1ff3785a-3ad4-475a-98b7-5d016e4c34a9">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d73b0a48-adcb-45a7-9b7d-759b6fd7d51a">

- Spinner는 웹에서 걸리는 시간에 버퍼링처럼 나타나는 부분을 의미한다
- st.spinner와 st.success를 추가하여 위와 같이 화면을 표현할 수 있다

<br>

<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7a596391-794e-4334-93b2-8a4cb81edc71">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/11c2efb4-88b3-48ef-ad07-1ffc8beee045">

```python
import openai
import streamlit as st

OPENAI_API_KEY = ''
OPENAI_API_ENDPOINT = 'https://sktfly2.openai.azure.com/'
OPENAI_API_TYPE = 'azure'
OPENAI_API_VERSION = '2023-05-15'   # 모델의 버전이 아니라 openai의 api의 버젼
                                    # ChatGPT의 버전이랑은 무관

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION


st.header("Welcome to AI Poem", divider='rainbow')
st.write("아름다운 시를 함께 지어BoA Yo~~!!")

name = st.text_input("작가의 이름을 입력하세요")
if name:
    st.write(name + '님 반갑습니다')

subject = st.text_input("시의 주제를 입력하세요")
content = st.text_area("시의 내용을 입력하세요")

button_click = st.button("Run")
if button_click:
    with st.spinner("Please wait..."):
        result = openai.chat.completions.create(
            model='dev-model',
            temperature=1,  # 0이 기본값이고 1이면 보다 창의적인 답을 제시
            messages=[
                {'role' : 'system', 'content' : 'You are a helpful assistant.'},
                {'role':'user','content' : "작가의 이름은 " + name},
                {'role':'user','content' : "시의 주제는 " + subject},
                {'role':'user','content' : "시의 내용은 " + content},
                {'role':'user','content' : "이 정보로 시를 생성해줘"},  # 명령을 내리는 부분
            ]
        )
    st.success("Done!:sunglasses:")
    st.write(result.choices[0].message.content)    # 0번째 대답을 가져와서 화면에 출력
```

- 이처럼 이름, 시의 주제와 내용을 입력 받아 시를 창작해주는 작업도 수행할 수 있다


<br>

