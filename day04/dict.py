lunch = {'중국집':'02-123-123','양식집':'052-123-123','한식집':'031-123-123'}
print(lunch)

print(lunch['중국집'])


idol = {'bts': {'지민':24,'RM':25}}     # value 값은 리스트나 또다른 dict 가능
idol['bts']  # → {'지민':24,'RM':25}
idol['bts']['RM']   # 25출력



# 딕셔너리 반복문 활용하기
   ## 기본 활용
for key in lunch:                       # → 꼭 key 라고 입력하지 않아도, 무조건 key 가 출력됨
       print(key)
       print(lunch[key])                # → value 값 출력

    ## key만 가져오기 : 내장함수 .keys()
for key in lunch.keys() :
        print(key)

    ## value만 가져오기 : 내장함수 .values()
for value in lunch.values():
        print(value)

    ## item 가져오기 : 내장함수 .items()
    ## lunch.items()  → [('중식','02'),.....]   : 리스트 내 튜플 형태로 가져옴   → 따로 사용하기 번거롭기 때문에  아래 ## 처럼 따로
for item in lunch.items():
        print(item)       

        ## 따로 가져오기
        for key,value in lunch.items():
            print(key,value)

                        ### 2개 = 자료형 길이 2
                            a,b =(1,2)  로 입력하면 자동 인식됨