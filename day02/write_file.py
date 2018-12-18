f = open('ssafy.txt','w')   # w: write, r:read, a:append
f.write('This is SSAFY!')
f.close()     # 꼭 써줘야 함

with open('ssafy.txt','w',encoding='utf8') as f:      # with : context manager
    f.writelines(['1\n', '2\n', '3\n'])
    #for i in range(10):
        #f.write(f'This is SSAFY! {i}\n)
