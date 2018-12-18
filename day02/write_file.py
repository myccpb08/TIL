f = open('ssafy.txt','w')   # w: write, r:read, a:append
f.write('This is SSAFY!')
f.close()     # 꼭 써줘야 함

with open('ssafy.txt','w',encoding='utf8') as f:      # with : context manager
    f.write('This is SSAFY!, with 이용했다.')