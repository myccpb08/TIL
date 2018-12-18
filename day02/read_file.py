with open('ssafy.txt','r',encoding='utf8') as f:
    lines = f.readlines()    #리스트로 반환
    for line in lines:
        print(line.strip())