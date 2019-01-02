#도시 중에 최근 3일 중 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    '서울' : [-6, -10, 6],
    '대전' : [-3, -6, 2],
    '광주' : [0, -2, 10],
    '구미' : [2, -2, 9]
 }
maxcity = ""
mincity = ""
maxtmp = -100
mintmp = 100
for cit in city.keys():
    for tmp in city[cit] :
        if tmp > maxtmp :
            maxtmp = tmp
            maxcity = cit
        if tmp < mintmp :
            mintmp = tmp
            mincity = cit

print(maxcity,maxtmp, mincity, mintmp)

#서울은 영상 2도였던 적이 있나요?
count = 0
for i in city['서울']:
    if i == 2:
        print("네 있습니다")
        break
    else:
        if count==len(city['서울'])-1:
            print("없습니다")
        count = count +1