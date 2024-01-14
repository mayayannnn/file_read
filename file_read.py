import os
import shutil

list = os.listdir(r"../test\folder1")
files = []
time = []

for i in list:
    path = os.path.join(r"../test\folder1", i)
    if os.path.isfile(path):
        files.append(str(i))

for i in files:
    target = '.'
    idx = i.find(target)
    r = i[idx:] 
    K = r
    year = i[0] + i[1] + i[2] + i[3]
    if i[4] == "0":
        if i[5] == "1":
            month = "01"
        elif i[5] == "2":
            month = "02"

        elif i[5] == "3":
            month = "03"

        elif i[5] == "4":
            month = "04"

        elif i[5] == "5":
            month = "05"

        elif i[5] == "6":
            month = "06"

        elif i[5] == "7":
            month = "07"

        elif i[5] == "8":
            month = "08"

        elif i[5] == "9":
            month = "09"
    if i[4] == "1":
        if i[5] == "0":
            month = "10"

        elif i[5] == "1":
            month = "11"

        elif i[5] == "2":
            month = "12"

    time.append(year + month + K)
files.clear

for i in time:
    target = '.'
    idx = i.find(target)
    r = i[:idx] 
    new_path = shutil.move(rf"../test\folder1\{i}",rf"../test\folder2\{r}")
    print(new_path)
time.clear

