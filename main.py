import os
import whisper
import pandas as pd
from dotenv import load_dotenv
from utils import transcribe_file, is_emergency


def main():
    # Whisper 모델 로드
    model = whisper.load_model("large-v2", device="cuda:0")

    folder_path = "emergence/"
    files = os.listdir(folder_path)  # 폴더 안의 모든 파일을 가져옵니다.
    # .m4a 파일만 필터링합니다.
    m4a_files = [file for file in files if file.endswith(".m4a")]
    results = []

    # 각 .m4a 파일을 전사 처리합니다.
    for m4a_file in m4a_files:
        file_path = os.path.join(folder_path, m4a_file)
        transcription = transcribe_file(file_path)
        if transcription:
            results.append((m4a_file, transcription))

    # 결과를 DataFrame으로 변환하고 Excel 파일로 저장합니다.
    df = pd.DataFrame(results, columns=["Filename", "Transcription"])
    df.to_excel("emergence_transcriptions.xlsx", index=False)

    file_path = "C:/Users/kgw57/PycharmProjects/Sonic-AI/emergence_transcriptions.xlsx"
    data = pd.read_excel(file_path)

    # 모든 텍스트에 대해 판단 수행
    results = []
    for text in data["Transcription"]:
        result = is_emergency(text)
        results.append((text, result))

    # 결과 출력 (또는 필요에 따라 다른 방식으로 처리)
    for text, result in results:
        print(f"Text: {text}")
        print(f"Classification: {result}")
        print("---")


if __name__ == "__main__":
    load_dotenv()
    main()
