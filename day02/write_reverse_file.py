with open('ssafy.txt','r',encoding='utf8') as f:
    lines = f.readlines()    #리스트로 반환
    lines.reverse()
    for line in lines:
        print(line.strip())

with open('ssafy.reverse.txt','w',encoding='utf8') as g:
    for i in lines:
        g.write(i)