import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()

def recognize_from_microphone():
    # 환경 변수 로딩
    speech_config = speechsdk.SpeechConfig(
        subscription=os.environ.get("SPEECH_KEY"), \
        region=os.environ.get("SPEECH_REGION"))
    speech_config.speech_recognition_language="en-US"
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    print("텍스트로 변환할 메시지로 마이크를 통해 말하세요.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("음성 인식됨 : [{}]".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("음성 인식불가 : {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("음성을 텍스트로 변환 취소됨: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("에러 : {}".format(cancellation_details.error_details))
            print("키(key)와 지역(region)을 설정하셨나요?")

recognize_from_microphone()