import csv
with open('lunch.csv','r',encoding='utf8') as f:
    #lines = f.readlines()    #리스트로 반환
    items = csv.reader(f)
    
    for item in items :
        print(item)
        #print(line.strip().split(','))   # line 안에서 , 를 기준으로 쪼갬 # 리스트로 나옴  #strip 공백제거
