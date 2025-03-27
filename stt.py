import whisper
import os
import sounddevice as sd
import scipy.io.wavfile as wav
from dotenv import load_dotenv
from openai import OpenAI
import json
from TTS.api import TTS
from playsound import playsound

load_dotenv(dotenv_path=".env")

# ======== 取得環境變量 ========
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CUSTOM_ROLE = open("./role/role_config.txt", "r", encoding="utf-8").read()

# ======== 初始化 ========
client = OpenAI(api_key=OPENAI_API_KEY)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2") # 語音模型, default: model_name="tts_models/multilingual/multi-dataset/xtts_v2"

# ======== sound-device 錄音設定 ========
DURATION = 5  # 錄音時間（秒）
SAMPLING_RATE = 44100  # 樣本率, default: 44100
FILE_NAME = "./audio/input.wav"
MEMORY_FILE = "./role/role_memory.json"

# ======== TTS 設定 ========
TTS_SPEAKER_WAV = "./audio/speaker.mp3" # 模仿語音
TTS_LANGUAGE = "zh" # 語言, default: "zh"
TTS_OUTPUT_FILE = "./audio/output.wav" # 輸出音檔
TTS_TEMPERATURE = 0.3 # 控制隨機性

# ======== 定義顏色代碼 ========
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

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

# ======== 載入記憶歷史 ========
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# ======== 儲存記憶歷史 ========
def save_memory(memory):
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

# ======== 呼叫 GPT 回應 ========
def get_openai_response(history):
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = history
    )
    return response.choices[0].message.content

# ======== 生成語音 ========
def speak(text):
    tts.tts_to_file(
        text=text,
        speaker_wav=TTS_SPEAKER_WAV,
        language=TTS_LANGUAGE,
        file_path=TTS_OUTPUT_FILE,
        split_sentences=True, # 長句切分
        temperature=TTS_TEMPERATURE
    )
    playsound(TTS_OUTPUT_FILE)

# ======== 主程式 ========
audio_data = record_audio()
save_audio(audio_data, FILE_NAME)

result = transcribe_audio(FILE_NAME)

if result:
    print(to_color(Colors.PURPLE, "✅ 喵~ 辨識成功!"), to_color(Colors.BLUE, f"結果: {result}"))

    memory = load_memory()
    if not memory:
        memory.append({"role": "system", "content": CUSTOM_ROLE})
    memory.append({"role": "user", "content": result})

    response = get_openai_response(memory)
    print(to_color(Colors.PURPLE, "✅ 喵~ GPT 回應:"), to_color(Colors.BLUE, f"{response}"))

    memory.append({"role": "assistant", "content": response})
    save_memory(memory)

    speak(response)
else:
    print(to_color(Colors.RED, "❌ 喵! 辨識失敗!!"))
