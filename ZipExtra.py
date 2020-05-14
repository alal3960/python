import os
import zipfile

dir = "C:\\Users\\alal3\\OneDrive\\바탕 화면\\닭"
files = os.listdir(dir)
print(files)

for file in files:
    fan_zip = zipfile.ZipFile('C:\\Users\\alal3\\OneDrive\\바탕 화면\\닭\\'+file)
    fan_zip.extractall('C:\\Users\\alal3\\OneDrive\\바탕 화면\\찌르레기')
    fan_zip.close()