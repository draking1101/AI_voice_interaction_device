# 這是使用whisper模型進行語音辨識(Speech-to-Text, STT)的程式碼

import whisper
import os

# 檢查音頻文件路徑
audio_path = "./audio/test1.wav"

# 載入模型和處理音頻
if os.path.exists(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    print(result["text"])
else:
    print(f"找不到音檔：{audio_path}")

# 輸出辨識結果
print(result["text"])

# 將辨識結果寫入txt檔案
transcript_dir = "./transcript"
transcript_path = "./transcript/這是一段錄音測試.txt"
try:
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
except Exception as e:
    print(f"無法保存文件: {e}")
    exit()
