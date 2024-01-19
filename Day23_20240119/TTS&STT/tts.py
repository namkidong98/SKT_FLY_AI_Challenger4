import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

# .env에 저장된 값들 로딩
load_dotenv()

speech_config = speechsdk.SpeechConfig(
    subscription=os.environ.get("SPEECH_KEY"), \
    region=os.environ.get("SPEECH_REGION"))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# voice 설정
# speech_config.speech_synthesis_voice_name='en-US-JennyNeural'
speech_config.speech_synthesis_voice_name='ko-KR-JiMinNeural'
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# 음성으로 변환할 텍스트를 입력
print("음성으로 변환할 텍스트를 입력해주세요.")
text = input()
speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("음성으로 변환된 텍스트 [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("음성 변환 취소됨: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("에러 : {}".format(cancellation_details.error_details))
            print("키(key)와 지역(region)을 설정하셨나요?")
                         