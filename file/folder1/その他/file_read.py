import os
import shutil

a = os.getcwd()
list = os.listdir(rf"{a}")
files = []
folders = []

for i in list:
    path = os.path.join(rf"{a}", i)
    if os.path.isfile(path):
        # ファイルの場合
        files.append(str(i))
    if os.path.isdir(path):
        # フォルダーの場合
        folders.append(str(i))

    
for i in files:
    year = i[0] + i[1] + i[2] + i[3]
    month = i[4] + i[5]
    r = year + month
    if not r in folders:
        continue
    new_path = shutil.move(rf"{a}/{i}",rf"{a}/{r}")
    print(new_path)
files.clear
folders.clear

from tkinter import messagebox

messagebox.showinfo('実行ファイル', 'ファイルの移動が完了しました！')