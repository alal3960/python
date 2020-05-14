#geojson들어간 폴더빼고 전부 삭제
import os

dir = "C:\\Users\\alal3\\OneDrive\\바탕 화면\\test"

files = os.listdir(dir)
print(files)
#찾을 문자열
for file in files:
    filename, fileExtension = os.path.splitext(file)
    #현재 경로의 파일명만 출력#
    #print(filename)
    #현재 경로의 확장자 출력#
    #print(fileExtension)
    if "geojson" in file:
        print(file)
        continue
    else:
        dir2 = "C:\\Users\\alal3\\OneDrive\\바탕 화면\\test\\"+file
        files2 = os.listdir(dir2)
        for file2 in files2:
            os.remove("C:\\Users\\alal3\\OneDrive\\바탕 화면\\test\\"+file+"\\"+file2)
        os.rmdir("C:\\Users\\alal3\\OneDrive\\바탕 화면\\test\\"+file)