## **專案動機** 
最近ChatGpt-4o 表現的非常擬人，而我也很享受跟GPT聊天的過程，因此想做出能跟GPT語音交流的工具

## 專案架構

`*` 標註的資料夾僅限保存在本地，不會被推送到repo
```bash
project_root/
├── assets/ # 存放圖片, 影片等等
├── *audio/ # 存放待轉換的音檔
├── *role/ # 存放gpt自訂義內容，比如對話歷史、人物設定
├── *transcript/ # 存放轉錄文本
├── requirements.txt # 項目依賴
├── README.md # 使用說明文檔
└── stt.py # 主程式
```

## 一、安裝步驟

**環境準備**

1. `Python` : 開發時使用的版本為`3.11.3`，[點我前往下載 python-3.11.3](<https://www.python.org/downloads/release/python-3113/>)
2. `ffmpeg` : [點我前往官網下載](<https://ffmpeg.org/download.html>)，載完後在電腦搜尋`編輯系統環境變數`，找到`PATH`新增路徑並指定到剛剛下載的`ffmpeg`檔案裡的`bin`資料夾，設定完成後須重啟電腦使環境變數生效
3. `GPT自訂義` ( 選擇性 ) : 在根目錄建立`role`資料夾，並在資料夾內建立`role_config.txt`檔案，在檔案內可輸入自訂義的GPT描述

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
4. `openai` : 整合Open AI 的 gpt功能
5. json : 用於保存歷史紀錄，比如對話歷史

## 展示影片&截圖

1. Log提示(能自定義顏色)

![Log展示](./assets/log.png)
