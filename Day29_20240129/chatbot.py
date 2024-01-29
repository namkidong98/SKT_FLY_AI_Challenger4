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

st.header("Welcome to GPT Bot", divider='rainbow')
st.write("궁금한 것을 물어보세요!")

query = st.text_input("Query? ")  # terminal이 아닌 browser의 사용자에게 입력 받기

button_click = st.button("run")   # run이라는 버튼
if button_click:                  # button이 클릭되었을 때만
    with st.spinner("Please wait..."):
        result = openai.chat.completions.create(
            model='dev-model',
            temperature=1,  # 0이 기본값이고 1이면 보다 창의적인 답을 제시
            messages=[
                {'role' : 'system', 'content' : 'You are a helpful assistant.'},
                {'role':'user','content' : query}
            ]
        )
    st.success("Done!:sunglasses:")
    st.write(result.choices[0].message.content)    # 0번째 대답을 가져와서 화면에 출력