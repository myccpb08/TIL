lunch = {'돈가스':1, '라면':2, '김밥':3}

import csv

with open('lunch.csv','w',encoding='utf8',newline='') as f:
     csv_writer = csv.writer(f)
     for item in lunch.items() :   #리스트 형태로 (key.value) 나열
         csv_writer.writerow(item)
         
         #f.write(f'{item[0]},{item[1]}\n')

