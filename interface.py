import tkinter as tk
from PIL import Image, ImageTk
import sys
import os

# 添加專案根目錄到 Python 路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

# 然後直接引用
from app.convertion import converstion

# ======== 主視覺介面設定 ========
window = tk.Tk()
window.title('傲嬌貓娘語音: 姬')
window.geometry('380x400')
window.resizable(False, False)
# window.iconbitmap('icon.ico')

# ======== 管理函數 ========

def close_program():
    window.destroy()  # 關閉視窗
    sys.exit()       # 結束程式

# ======== 管理GUI物件 ========

# 觸發 converstion 函數
button = tk.Button(
    window, 
    text="開始對話", 
    command=converstion  # 直接綁定函數
)
button.place(relx=0.5, rely=0.4, anchor="center")  # relx=0.5 表示水平置中

# 關閉視窗
button_close = tk.Button(
    window,
    text="關閉視窗",
    command=close_program
)
button_close.place(relx=0.5, rely=0.6, anchor="center")

# ======== 主程式 ========
window.mainloop()
