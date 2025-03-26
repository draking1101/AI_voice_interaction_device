## **專案動機** 
最近ChatGpt-4o 表現的非常擬人，而我也很享受跟GPT聊天的過程，因此想做出能跟GPT語音交流的工具

## 一、安裝步驟

**環境準備**

1. `Python` : 開發時使用的版本為`3.11.3`，[點我前往下載 python-3.11.3](<https://www.python.org/downloads/release/python-3113/>)
2. `ffmpeg` : [點我前往官網下載](<https://ffmpeg.org/download.html>)，載完後在電腦搜尋`編輯系統環境變數`，找到`PATH`新增路徑並指定到剛剛下載的`ffmpeg`檔案裡的`bin`資料夾，設定完成後須重啟電腦使環境變數生效

**安裝所需套件**

```bash
pip install -r requirements.txt
```

**執行**

```bash
py stt.py
```

## 二、使用的套件

1. `Whisper` : 辨識語音並轉成文字檔，依賴`ffmpeg`所以ffmpeg務必確實安裝
2. `sounddevice` : 及時從麥克風錄音
3. `scipy` : 將聲音資料儲存為`wav`檔
