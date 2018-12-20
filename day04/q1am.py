score = {'수학':80, '국어':90, '음악':100}

#평균을 구하시오

# 내 풀이
scores = score.values()

a=0
for i in scores :
    a=a+i

print(a/len(score))

# 강사님 풀이 (sum 자체 함수 이용)

total_score = sum(score.values())  # →  sum([80,90,100]) → 270
avg_score = total_score / len(score)    # → 270/3
print(avg_score)