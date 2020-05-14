#SPOT들어간 파일만 다른 폴더로
import os
import shutil
dir = "C:\\Users\\alal3\\OneDrive\\바탕 화면\\test"

files = os.listdir(dir)
print(files)

for file in files:
    dir2 = "C:\\Users\\alal3\\OneDrive\\바탕 화면\\test\\"+file
    files2 = os.listdir(dir2)
    for file2 in files2:
        if "SPOT" in file2:
            print(file2)
            #shutil.copy(src, dst)
            shutil.copy("C:\\Users\\alal3\\OneDrive\\바탕 화면\\test\\" + file + "\\" + file2, "C:\\Users\\alal3\\OneDrive\\바탕 화면\\Copyfile")