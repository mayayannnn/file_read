import os
import shutil

list = os.listdir(r"file/folder1")
files = []
time = []

for i in list:
    path = os.path.join(r"file/folder1", i)
    if os.path.isfile(path):
        files.append(str(i))

for i in files:
    target = '.'
    idx = i.find(target)
    k = i[idx:]
    year = i[0] + i[1] + i[2] + i[3]
    month = i[4] + i[5]
    time.append(year + month + k)
files.clear
for i in time:
    target = '.'
    idx = i.find(target)
    r = i[:idx]
    new_path = shutil.move(rf"file/folder1/{i}",rf"file/folder2/{r}")
    print(new_path)
time.clear

