import openai
import whisper
import os
import pandas as pd

# Whisper 모델 로드
model = whisper.load_model("large-v2", device="cuda:0")

def transcribe_file(filepath):
    try:
        # 주어진 파일을 전사하여 결과 텍스트를 반환합니다.
        result = model.transcribe(
            filepath, language="ko", temperature=0
        )  # temperature:
        return result["text"]
    except Exception as e:
        print(f"Error processing file {filepath}: {e}")
        return None

def is_emergency(text):
    # openai API를 사용하여 텍스트 분류
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": ""},
            {
                "role": "user",
                "content": f"다음의 텍스트를 읽고 위급 상황인지 아닌지 판단하시오. 위급상황이라면 "
                f'"위급상황입니다. 신속히 상황 파악을 해주십쇼." 라하고 '
                f'위급 상황이 아니라면 "위급상황이 아닙니다". 라고 해줘: {text}',
            },
        ],
    )
    return response["choices"][0]["message"]["content"]
