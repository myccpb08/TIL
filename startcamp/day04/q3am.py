# 도시별 최근 3일의 온도입니다
city = {
    '서울' : [-6, -10, 6],
    '대전' : [-3, -6, 2],
    '광주' : [0, -2, 10],
    '구미' : [2, -2, 9]
 }


 # 3-1. 도시별 최근 3일의 온도 평균은?


# 내 꺼
for i,j in zip(city.values(),city.keys()) :
    print(f"{j}: {round(sum(i)/len(i),2)}")

    
# 강사님꺼
for name, temp in city.items():
    #1. 반복이용
    total_temp = 0
    for t in temp:
        # 1번째 시행
        # t #> -6
        total_temp = total_temp + t
    avg_temp = total_temp / len(temp)
    print(f'{name} : {avg_temp}') 


    #2. 내장 함수이용
    avg_temp = sum(temp)/len(temp)
    
    

