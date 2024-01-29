import openai
import streamlit as st

OPENAI_API_KEY = '6e65e9d2d05c4c9a8560cdc88595e14f'
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