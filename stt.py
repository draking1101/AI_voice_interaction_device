import whisper
import os
import sounddevice as sd
import scipy.io.wavfile as wav

# ======== sound-device 錄音設定 ========
DURATION = 5  # 錄音時間（秒）
SAMPLING_RATE = 44100  # 樣本率
CHUNK_DURATION = 0.1  # 每次錄音的時間長度（秒）

# ======== 定義顏色代碼 ========
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

# ======== 轉換文字顏色 ========
def to_color(color_code, text):
    return f"{color_code}{text}{Colors.RESET}"

# ======== 錄音 ========
def record_audio():
    print(to_color(Colors.GREEN, "🟢 喵~開始錄音囉! 請對著麥克風說話..."))
    audio_data = sd.rec(int(DURATION * SAMPLING_RATE), samplerate=SAMPLING_RATE, channels=1, dtype='int16')
    sd.wait()
    print(to_color(Colors.GREEN, "✅ 錄音完成! 喵~"))
    return audio_data

# ======== 保存音頻 ========
def save_audio(audio_data, filename):
    wav.write(filename, SAMPLING_RATE, audio_data)
    print(to_color(Colors.GREEN, "✅ 喵~音頻已保存"), to_color(Colors.BLUE, f"檔名: {filename}"))

# ======== 語音辨識(Speech-to-Text) ========
def transcribe_audio(filename):
    if os.path.exists(filename):
        model = whisper.load_model("base")
        result = model.transcribe(filename, language="zh")
        return result["text"]
    else:
        print(to_color(Colors.RED, "❌ 喵嗚嗚找不到音檔: "), to_color(Colors.BLUE, filename))
        return None

# ======== 主程式 ========

# 檢查音頻文件路徑
FILE_NAME = "./audio/test1.wav"

audio_data = record_audio()
save_audio(audio_data, FILE_NAME)
result = transcribe_audio(FILE_NAME)

if result:
    print(to_color(Colors.PURPLE, "✅ 喵~ 辨識成功!"), to_color(Colors.BLUE, f"結果: {result}"))
else:
    print(to_color(Colors.RED, "❌ 喵! 辨識失敗!!"))
