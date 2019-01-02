ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gm":  {
            "lecturer": "junwoo",
            "manager": "pro-gm",
            "class president": "엄윤주",
            "groups": {
                "1조": ["강대현", "권민재", "서민수", "이규진"],
                "2조": ["박재형", "서민호", "윤종원", "이지현"],
                "3조": ["김미진", "김영훈", "엄윤주", "여성우"],
                "4조": ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"],
            }
        },
        "gj": {
            "lecturer": "change",
            "manager": "pro-gj"
        }
    }
}

# 난이도* 1. 지역(location)은 몇개 있나요? : list length
print(len(ssafy["location"]))

# 난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
library = ssafy["language"]["python"]["python standard library"]
count = 0
for i in library :
    if i == "requests":
        print("ok")
        break
    else :
        if count==len(library)-1:
            print("false")
        count = count +1
##### 강사님 풀이
    ## library 똑같이 설정
       #print('requests' in library)       

# 난이도** 3. gm반의 반장의 이름을 출력하세요. : depth 있는 접근
print(ssafy["classes"]["gm"]["class president"])


# 난이도*** 4. ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
for i in ssafy["language"].keys():
    print(i)

# 난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
classes= ssafy["classes"]["gm"]
for i in classes :
    if i =="lecturer":
        print(classes[i])
    elif i == "manager" :
        print(classes[i])

# 난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
frameworks = ssafy["language"]["python"]["frameworks"]
for i in frameworks :
    print(f'{i} 는 {frameworks[i]}이다.')

    ### 강사님 방법
    frameworks = ssafy["language"]["python"]["frameworks"]
    for key,value in frameworks.items():
        print(f'{key}는 {value}이다 ')

# 난이도***** 7. 오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.

groups = ssafy["classes"]["gm"]["groups"]["4조"]
import random as r
print(f'오늘의 당번은 {r.choice(groups)}')

choicegroup = list(ssafy["classes"]["gm"]["groups"].keys())
groupss = ssafy["classes"]["gm"]["groups"][r.choice(choicegroup)]
b = r.choice(groupss)
print(f'오늘의 당번은 {b}')