#디렉토리내 geojson제외한 파일 삭제

import os
import glob

dir = "C:\\Users\\alal3\\OneDrive\\바탕 화면\\새 폴더\\mountain-원본"
files = os.listdir(dir)
print(files)

for file in files:
    if "geojson" in file:
        continue
    else:
        os.remove("C:\\Users\\alal3\\OneDrive\\바탕 화면\\새 폴더\\mountain-원본\\" + file)
#[os.remove(f) for f in glob.glob("C:\\Users\\alal3\\OneDrive\\바탕 화면\\test\\*.zip")]