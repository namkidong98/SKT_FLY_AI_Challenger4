from flask import Flask, url_for, request, render_template, session
import requests, os, uuid, json
from dotenv import load_dotenv

# .env에 저장된 값들 로딩
load_dotenv()

# 앱
app = Flask(__name__)

# 경로 추가
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # form에서 입력된 값 읽기
    original_text = request.form['text']
    target_language = request.form['language']

    # 키 로딩
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    # translator api 버전 설정
    path = '/translate?api-version=3.0'
    # target 언어 추가
    target_language_parameter = '&to=' + target_language
    # 전체 URL
    full_url = endpoint + path + target_language_parameter

    # 헤더 정보 설정
    headers= {
        'Ocp-Apim-Subscription-Key' : key,
        'Ocp-Apim Subscription-Region' : location,
        'Content-type' : 'application/json',
        'X-ClientTraceId' : str(uuid.uuid4())
    }

    # 번역 요청할 본문 생성
    body = [{'text' : original_text}]

    # post로 translator 서비스 호출
    translator_request = requests.post(full_url, headers=headers, json=body)

    # 응답받은 json 탐색
    translator_response = translator_request.json()

    # 번역 검색
    translated_text = translator_response[0]['translations'][0]['text']
    
    # 렌더링 템플릿 호출, 번역된 텍스트, 원본 텍스트 및 대상 언어를 템플릿에 전달
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )