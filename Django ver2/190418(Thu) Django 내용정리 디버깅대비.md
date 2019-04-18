## 오전수업 - M:N 관계

( orm 폴더 內 manytomany 앱 作)

```bash
myccpb08:~/workspace (master) $ cd django
myccpb08:~/workspace/django (master) $ cd orm
(orm-venv) myccpb08:~/workspace/django/orm (master) $ ./manage.py startapp manytomany
```

```python
# orm / settings.py 에 앱 등록
INSTALLED_APPS = [
    'django_extensions',
    'crud',
    'onetomany',
    'manytomany',
]
```



#### 1. manytomany / models.py :  표 作  & migrate

```python
from django.db import models

# 병원에 오는 사람들을 기록하는 시스템을 만들려고 한다.
# 필수적인 모델은 환자와 의사이다.
# 어떠한 관계로 표현할 수 있는가? : 정답 = M:N

class Doctor(models.Model):
    name = models.TextField()
    
# 그냥 이렇게 하면 Doctor : Patient = 1 : N   
class Patient(models.Model):
    name = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
```

```PYTHON
✅✅✅ # 그러므로 아래와 같이 작성해야한다

from django.db import models

# 병원에 오는 사람들을 기록하는 시스템을 만들려고 한다.
# 필수적인 모델은 환자와 의사이다.
# 어떠한 관계로 표현할 수 있는가?
# >> 한 의사는 여러명의 환자를 볼 수 있고, 한 환자는 여러 명의 의사에게 진료 가능
# >> ∴ M : N 

class Doctor(models.Model):  # 1번 표
    name = models.TextField()
    
class Patient(models.Model):  # 2번 표
    name = models.TextField()
    
# Doctor : Reservation = 1:N
# Patient : Reservation = 1: N
# Doctor : Patient = M : N
class Reservation(models.Model):  # 3번표
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
# 1번과 3번은 1:n , 2번과 3번도 1:n   3번 표는 중간다리
```

![](C:\Users\student\kimkim\Django ver2\이미지\1.png)

```bash
./manage.py makemigrations
./manage.py migrate
```



#### 2. shell_plus

```bash
$ ./manage.py shell_plus
```



###### 하단부터는 shell 작업



#### 3. 환자2, 의사2 만들기 ( class Doctor  & class Patient)

```python
>>> doctor1 = Doctor.objects.create(name='Kim')
>>> doctor2 = Doctor.objects.create(name='Kang')
>>> patient1 = Patient.objects.create(name='Tom')
>>> patient2 = Patient.objects.create(name='John')
```



#### 4. 예약테이블 만들기 (의사 : 예약 = 1:N)

```python
>>> Reservation.objects.create(doctor=doctor1, patient=patient1)
<Reservation: Reservation object (1)>   # doctor_id : patient_id = 1:1  
    
>>> Reservation.objects.create(doctor=doctor1, patient=patient2)
<Reservation: Reservation object (2)>    # doctor_id : patient_id = 1:2 (위 그림과 다름)
    
>>> Reservation.objects.create(doctor=doctor2, patient=patient1)
<Reservation: Reservation object (3)>
```

```python
# 1번 의사가 예약한 환자들
>>> doctor1.reservation_set.all()  # 1이 N을 불러올 때, _set.all()
<QuerySet [<Reservation: Reservation object (1)>, <Reservation: Reservation object (2)>]>

# 2번 환자가 예약한 의사들
>>> patient2.reservation_set.all()
<QuerySet [<Reservation: Reservation object (1)>]>
```

![](C:\Users\student\kimkim\Django ver2\이미지\2.png)

```python
# 1번 의사가 예약한 환자의 이름을 出
>>> for res in doctor1.reservation_set.all():  # 1번의사가 가진 각 예약에 대하여
...     print(res.patient.name) # 그 예약의 환자 이름을 출력해
... 
John
Tom
```



#### 5. 만든 예약 테이블을, 중간자로 넣기(through)  ≒ 바로 갈 수 있는 통로 뚫기

```python
class Patient(models.Model):  # 2번 표
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation')  ✅ ← 행 추가
    # reservation 테이블을 통해서, N:N 관계를 맺겠다
    
아니면

class Doctor(models.Model):  # 1번 표
    name = models.TextField()
    patients = models.ManyToManyField(Patient, through='Reservation') 을 추가하거나
    
# class 둘 중 하나에 골라서, 상대를 넣어주면 됨
```

```mathematica
Doctor:Reservation = 1:N   ∴ Reservation = N * Doctor
Patient:Reservation = 1:M   ∴ Reservation = M * Doctor
N*Doctor = M*Patient = Reservation  ∴ Doctor : Patient = M:N
```

###### 표를 만졌으므로, exit() 로 쉘 종료 → migrate → 다시 shell open



```python
>>> doctor1 = Doctor.objects.get(pk=1)  # doctor1 = id가 1인 의사
>>> doctor1
<Doctor: Doctor object (1)>
    
>>> patient1 = Patient.objects.get(pk=1)  # patient1 = id가 1인 환자
>>> patient1
<Patient: Patient object (1)>
    
>>> patient1.doctors.all()  # 환자1과 연결된, 의사쌤의 목록
<QuerySet [<Doctor: Doctor object (1)>, <Doctor: Doctor object (2)>]>

>>> doctor1.patient_set.all()  # 의사1과 연결된, 환자들의 목록  ✅✅ 6번 표현과 비교
							# Patient 에  through 를 加 때문 (Patient 에 이름표가 달려있으므로)
    						# doctor 를 주어로 하는 문장은 _Set.all() 을 써야함
        					# 만약 5번 단계에서 아래 표현을 선택한다면, all 과 _Set.all 이 바뀜
<QuerySet [<Patient: Patient object (2)>, <Patient: Patient object (1)>]>
```



#### 6. 누가 주어냐에 따라,  `patient_set`  표현과  `doctors` 헷갈리니까,  `related_name` 으로 바꿔줌

```python
# models.py

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')  
    # reservation 테이블을 통해서, N:N 관계를 맺겠다
    # related_name = patient_set.all() = 'patients'
    # ∴  doctor1.patient_set.all() = doctor1.patients.all() ✅✅✅
```

###### 표를 만졌으므로, exit() 로 쉘 종료 → migrate → 다시 shell open  (exit() 하고 다시 open 해야 shell 이 바뀐 표로 인식함)

```python
>>> doctor1 = Doctor.objects.get(pk=1)
>>> doctor1.patients.all()
<QuerySet [<Patient: Patient object (2)>, <Patient: Patient object (1)>]>
```



#### 7. through 구문 안 쓰고 manytomany 하기 : 굳이 through 안 써도, Django가 알아서 만들어줌

- 📌 [appname]_patient_doctors  라는 클래스를 장고가 자동으로 만들어줌

- 우리가 만들었던 reservation 과 같다

- 하지만 얘는 진짜 id 와 id ⭕연결만!⭕ 을 한다. (딱 관계설정만)

  ∴ 現 의사-환자 관계만 쓰고 있으니 이렇게 하는 게 간편

  하지만, 예약시간이나, 장소 등을 넣으려면  위에서 처럼 별도의 reservation 테이블을 만들어서 用

- 우리가 만들면 reservation 에 접근가능하지만, django가 자동으로 만든 테이블은 우리가 별도 접근 不

===================================================================================

* db.sqlite 파일 삭제
* migrations 폴더 내에 `__init__` 제외하고 다 지우기
* 새롭게 migrations & migrate
* shell_plus 다시 on

```python
# reservation 클래스 삭제
# class Patient 수정

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients') ✅ through 삭제
```

```python
# db 날렸으니까 데이터 다시 넣어줌
>>> doctor1 = Doctor.objects.create(name='Kim')
>>> doctor2 = Doctor.objects.create(name='Kang')
>>> patient1 = Patient.objects.create(name='Tom')
>>> patient2 = Patient.objects.create(name='John')

>>> doctor1.patients.all() # 의사1과 연결된 환자는?
<QuerySet []>
>>> patient2.doctors.all() # 환자2와 연결된 의사는?
<QuerySet []>

>>> doctor1.patients.add(patient2)  # 의사1 예약환자에 환자2를 추가해
>>> doctor1.patients.all()
<QuerySet [<Patient: Patient object (2)>]>
>>> patient2.doctors.all()
<QuerySet [<Doctor: Doctor object (1)>]>

>>> doctor1.patients.remove(patient2)  # 의사1 예약목록에서 환자2 지워
									# patient2.doctors.remove(doctor1) 해도 상관없다
>>> doctor1.patients.all()
<QuerySet []>
```





## 오후수업 : 디버깅 연습(에러메시지가 있을 때)

#### 1. template syntax error : 

* 파이썬 코드 문제 x , 
* html 파일의 문제
  * `{` 빠짐
  *  `%` 빠짐
  *  `load`안 함 (부트스트랩 등)  >> `{% load bootstrap4 %}`



#### 2. Forbidden : csrf

* form 태그 內 csrf_token 이 빠짐 >> {% csrf_token %} 입력



#### 3. New Post 를 눌렀는데, page not found 

* 주소관련 문제
* 아예 urls.py 에 주소가 존재하지않거나  `path('create/', views.create, name='create')`
* 주소가 존재하지만, 링크된 주소가 잘못되었거나 (html 에 주소 )
* urls.py (장고) 는 끝날때만 `/`
* html 은 앞과 뒤 모두 `/` 



#### 4. Nameerror at /nwith/  : name 'user' is not defiend

* 변수명 문제 : 무조건 파이썬문제 = views.py 에서 찾아라
* /nwith/ 라는 주소로 가려고 할 때, 문제가 생겼음을 보여줌
* user 라는 변수로 지정된 게 없는데, user 를 사용하려고 했다



#### 5. 댓글 작성하고 제출 눌렀을 때,  IntegrityError at  /posts/7/comments/create

* NOT NULL contraint failed : posts_comment.post_id ( comment 테이블의 post_id 가 無)
* 댓글과 포스트는 n:1 관계라서 댓글이 만들어질 때는 부모에 대한 정보가 있어야 하는데 그 정보가 x
* views.py 에서 수정해야 한다
* `comment.post_id = post_id`  筆
* `post = get_object_or_404(Post, id=post_id)`
  `comment.post = post` 두 줄 입력 



#### 6. 댓글 작성하고 제출 눌렀을 때, `페이지가 작동하지 않습니다. http error 405` 發

* terminal 內 error 메시지 : method (get) = 위 주소는 get 방식으로 요청받을 수 없다
* @required_post 라고 views.py 에 적혀있읐을 거임
* 그러면 해당 함수로 요청보내는 form 태그를 고쳐야 한다 >> html 로 감
* 가서 form 의 method 를 "POST" 로 바꿈



#### 7. NoeverseMatch at /posts/  : matching 되는 주소가 없다

* reverse for 'comment' not found. 'comment' is not a valid view function or pattern name
* urls.py 에 우리가 지은 name 중 comment 가 無
* 2가지 체크
  * urls.py 에 name = comment 가 제대로 되어 있는지 확인
  * name 에 잘 적혀있다면,  해당 주소를 호출한 곳 (html) 에서 name을 잘못 썼거나



#### 8. raise FieldError (무조건 forms.py 수정)

* django.core.exceptions.FieldError : Unknow field(s)
* 서버는 실행 안 되고, terminal 에 error 발생
* forms.py 에서 해당 field 名 없거나, 있거나  
* ∴ models.py 에 없는 field 를 forms.py 에 적었는지 확인하면 됨
* 추가) `OperationalError at [URL]`
  * no such column : movies_score.movie_id    : `앱명_테이블名.column名`
  * 이 경우에는 modesl.py 에 column 이 제대로 있는지 확인
  * 입력했는데, migrations 안 했거나 



📌📌📌 이걸 이용해서 푸는 거 시험

#### 9. you are trying to add a non-nullable field 'content' to article without a default; 1과, 2중 선택해라고 나옴

* title 이라는 column 만 만들어져있는 상태에서 자료를 입력해놨는데,
* content 라는 column 을 추가 생정했을 때 보이는 에러 
* 즉, content 라는 column 이 새로 생겼는데, 그 내용 없는 애들 어떻게 처리할거야?
* [2선택] blank=True, default=``, default='123' 등 값을 content 에 넣어줌
* [1선택] terminal 에서 default 넣거나
* `content = models.TextField(blank=True)`  또는
* `content = models.TextField(default=' ')` 라고 입력하고 migration 하면,
* 아예 위의 알림이 뜨지 않음
* ✅ 게시판에다가 어떤 사람이 와서 글을 쓰고 제출버튼 눌렀음. 근데 detail 페이지에서 화면 뜨는 걸 봤떠니 제목에만 값이 들어가있다. 이 상황을 해결할 방법은? : migration 할며녀 알림 뜨니까 위의 해법 쓰고 migrations 하면 됨



## 디버깅연습 (logic error)

##### 에러메시지 x = 코드상 문제 無 : 하지만 원하는 대로 실행 안 됨 = logic error)



#### 1. list 페이지에서 글 목록이 안 보인다

* 해당 페이지를 보여주는 html 의 문제
* block 名 잘못됨
* base.htm 에는  {% block container %} 라고 되어있는데
* list.html 에서 {% block body %} 라고 되어 있으면 페이지가 안 보인다
* ⭕ {% block container %} 로 바꾸면 됨



#### 2. settings.py 에  설정 5가지 ( 각 설정이 프로젝트에 무엇을 영향 미치는지)

* LANGUAGE_CODE = 'en-us'  →  `ko-kr`
* TIME_ZONE = 'UTC'    → `Asia/Seoul`
* USE_I18N = True  : true 이면 language_code 에 설정한 언어를 사용하겠다, 만약 false 면 위에 설정을 어떻게 하든 영어로만 됨
* USE_L10N = True   ( 몰라도 됨 )
* USE_TZ = True  : true 이면 설명한 time-zone 을 사용, 만약 false 면 시간바꿔도 반영 안 됨



<https://github.com/chulsea/debuggingtest>