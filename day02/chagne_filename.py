import os

os.chdir(r'C:\Users\student\kim\day02\dummy')
# print(os.getcwd())
for filename in os.listdir('.'):
    os.rename(filename, filename.replace('지원자', '합격자' ))

# 합격자_0_ 누구누구.txt 로 바꾸기

