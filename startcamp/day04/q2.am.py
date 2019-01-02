#평균을 구하시오
# 학생들의 점수
scores = {'a':{'수학':80, '국어':90, '음악':100},
          'b':{'수학':100, '국어':100, '음악':100}}


# 반평균을 구하시오

total=0
subject =0

for key in scores.keys():
    subject = subject + len(scores[key])
    total = total + sum(scores[key].values())

avg = total/subject
print(avg)

# 반복을 이용해서만 풀기 (강사님)

total_score = 0
count = 0

scores.values()        #>  [{수학':80, '국어':90, '음악':100},  {'수학':100, '국어':100, '음악':100} ]   : 리스트

for person_score in scores.values():        #> {수학':80, '국어':90, '음악':100} 
    #person_score.vales()    #> [80,90,100]
    for subject_score in person_score.values():
        total_score = total_score + subject_score      #> 첫번째 시행 후 80
        count = count +1

# 현 상태 : total score = 6과목 합/  count = 6

avg_score = total_score/count
print(avg_score)