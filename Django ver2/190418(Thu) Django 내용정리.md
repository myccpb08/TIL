## 오전수업 - N:N 관계

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
# 어떠한 관계로 표현할 수 있는가? : 정답 = N:N

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
# >> ∴ N : N 

class Doctor(models.Model):  # 1번 표
    name = models.TextField()
    
class Patient(models.Model):  # 2번 표
    name = models.TextField()
    
# Doctor : Reservation = 1:N
# Patient : Reservation = 1: N
class Reservation(models.Model):  # 3번표
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
# 1번과 3번은 1:n , 2번과 3번도 1:n   3번 표는 중간다리
```

![](C:\Users\student\kimkim\Django ver2\1.png)

```bash
./manage.py makemigrations
./manage.py migrate
```

