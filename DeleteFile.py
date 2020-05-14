#디렉토리 내 특정 폴더명만 삭제
#SPOT들어간 파일 빼고 삭제
import os

dir = "C:\\Users\\alal3\\OneDrive\\바탕 화면\\새 폴더\\mountain-원본"
files = os.listdir(dir)
print(files)
#찾을 문자열
search = "SPOT"
for file in files:
    filename, fileExtension = os.path.splitext(file)
    #현재 경로의 파일명만 출력#
    #print(filename)
    #현재 경로의 확장자 출력#
    #print(fileExtension)
    if "SPOT" in file:
        print(file)
        continue
    else:
        os.remove("C:\\Users\\alal3\\OneDrive\\바탕 화면\\새 폴더\\mountain-원본\\"+file)