# 오전수업: orm폴더 / orm 프로젝트 / crud 앱

#### 1. 용어정리

* class Post: Django 에서는 model 이라고 부름
                    DB에서는 table 이라고 부름

* post = Post() : Post 클래스의 인스턴스 = post
             Django 에서는 instance or Object 라고 부름 ( ∵ OOP 에서 Object)
             DB에서는 Record or Row

* title : Django 에서는 Field
           DB 에서는 Column 이라고 불림

  

#### 2. 기본 설정 순서

1. django / orm 폴더 作 후에 해당 폴더로 이동

   ```bash
   myccpb08:~/workspace (master) $ cd django
   ```

2. orm 폴더로 이동  :  가상환경만들기 : 장고설치하기

   ```bash
   myccpb08:~/workspace/django (master) $ cd orm
   myccpb08:~/workspace/django/orm (master) $ pyenv virtualenv 3.6.7 orm-venv
   myccpb08:~/workspace/django/orm (master) $ pyenv local orm-venv
   (orm-venv) myccpb08:~/workspace/django/orm (master) $ pip install django==2.1.8
   ```

3. 현재 폴더에 새로운 프로젝트 作

   ```bash
   (orm-venv) myccpb08:~/workspace/django/orm (master) $ django-admin startproject orm .
   # startproject 프로젝트名 .  (점 필수)
   ```

4. 앱 생성

   ```bash
   (orm-venv) myccpb08:~/workspace/django/orm (master) $ ./manage.py startapp crud
   # startproject 앱名 .  (점 필수)
   ```

5. settings.py 앱등록: 40line

   ```python
   INSTALLED_APPS = [
       'crud',
   ]
   ```

6. 앱의 모델 만들기

   ```python
   # models.py
   from django.db import models
   
   # Create your models here.
   class Post(models.Model):
       title = models.TextField()
   ```

7. migration 하기

   ```bash
   (orm-venv) myccpb08:~/workspace/django/orm (master) $ ./manage.py makemigrations
   (orm-venv) myccpb08:~/workspace/django/orm (master) $ ./manage.py migrate
   ```

   

#### 3. 장고 extensions

1. 설치

   ```bash
   (orm-venv) myccpb08:~/workspace/django/orm (master) $ pip install django_extensions
   ```

2. settings.py 에 설치사항 알려주기

   ```python
   INSTALLED_APPS = [
       'django_extensions',
       'crud',
   ]
   ```

3. bash 에서 장고 모듈 불러와서, 여러가지 테스트 할 수 있는 장고 shell 사용하기 ( 기본 shell, extension 사용 x)

   ```bash
   (orm-venv) myccpb08:~/workspace/django/orm (master) $ ./manage.py shell
   
   # 이렇게만 입력하면
   # Post 클래스를 사용하려면
   from crud.models import Post 라고 쳐야 했는데, extension 쓰면 안 해도 됨
   
   # shell 종료
   exit()
   ```

4. 기본 shell 은 불편하니까, shell plus 를 쓰자 (shell plus 는 알아서 import 해 줌)

   ```bash
   (orm-venv) myccpb08:~/workspace/django/orm (master) $ ./manage.py shell_plus
   
   # 위와 같이 입력하면 아래와 같은 결과 뜸
   
   # Shell Plus Model Imports
   from crud.models import Post
   from django.contrib.admin.models import LogEntry
   from django.contrib.auth.models import Group, Permission, User
   from django.contrib.contenttypes.models import ContentType
   from django.contrib.sessions.models import Session
   # Shell Plus Django Imports
   from django.core.cache import cache
   from django.conf import settings
   from django.contrib.auth import get_user_model
   from django.db import transaction
   from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
   from django.utils import timezone
   from django.urls import reverse
   
   ```

   

### 

## CRUD

######  지금부터는 python shell 에서 작업 (bash칸을 shell plus 로 바꿨음)

### 1. Create (방법 3가지)

```python
# 아래 작업에서 Post 는 models.py 에서 정의한 class Post 말하는 것
class Post(models.Model):
    title = models.TextField()

    
# python shell 에서 작업
# 방법 1️⃣
>>> post = Post(title='hello-1')
>>> post
<Post: Post object (None)>  # 실제 DB 에 저장된 게 아니라서, 아이디 값 x
>>> post.title
'hello-1'
>>> post.save()   # 라고 하면 , DB에 저장됨
>>> post
<Post: Post object (1)>  # 이제 DB 에 저장되었으니, 1번 row 로 등록
    
    
# 방법 2️⃣ : create 라는 method 가 save 까지 쭉 해줌
>>> post2 = Post.objects.create(title='hello-2')
>>> post2
<Post: Post object (2)>
    

# 방법 3️⃣ : 1번 방법과 유사
>>> post3 = Post()
>>> post3.title = 'hello-3'
>>> post3.save()
>>> post3
<Post: Post object (3)>
```



### 2. Read

```python
# 모든 row 가져오기
>>> posts = Post.objects.all()
>>> posts
<QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)>]>

# 특정 row 가져오기 (get, filter)
# 	방법 1️⃣ id 나 pk 로 호출
>>> post = Post.objects.get(id=1)
>>> post
<Post: Post object (1)>
    
>>> Post.objects.get(pk=1)
<Post: Post object (1)>
    

#	방법 2️⃣ 어떤 column 값을 정확히 입력함으로써 호출
>>> post = Post.objects.get(title='hello-2')
>>> post
<Post: Post object (2)>
    		# 만약에 title='hello-1' 인 글이 여러 개 있으면 get 은 id 번호가 가장 낮은 거 1개만 찾아줌
    

# 	방법 3️⃣ views.py 한정
>>> from django.shortcuts import get_objects_or_404
>>> post = get_object_or_404(Post, pk=1)  # id=1, title='hello-1' 도 가능


#	방법 4️⃣ : filter 사용
>>> post = Post.objects.filter(pk=1)[0]  # id=1, title='hello-1' 도 가능
>>> post = Post.objects.filter(pk=1).first()  # last()  도 있음

# 만약에 title='hello-1' 인 글이 여러 개 있으면 filter 는 모든 글을 가져옴
# 모든 글을 가져와서 리스트에 들어있을 테니까 (post 에) 뒤에 [0] 을 붙이면, 아이디 가장 작은 글 가져옴
↓↓↓↓
>>> Post.objects.create(title='hello-1')
<Post: Post object (4)>
>>> Post.objects.filter(title='hello-1')
<QuerySet [<Post: Post object (1)>, <Post: Post object (4)>]>
>>> Post.objects.filter(title='hello-1').first()
>>> posts = Post.objects.filter(title='hello-1')
>>> post.first()  # 와 동치

>>> Post.objects.filter(title='hello')  # hello 라는 제목이 없으면
<QuerySet []> # 빈리스트 return
>>> >>> print(Post.objects.filter(title='hello').first()) # 빈 리스트의 fisrt 는 없으니까
None

# 'lo' 가 들어간 애들 가져오기
>>> Post.objects.filter(title__contains='lo')  # __  언더바 2개  : sql 에서 like 와 같음
<QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)>, <Post: Post object (4)>]>

# 정렬
>>> Post.objects.order_by('title')  # column 명 넣어줌: 현재 1번과 4번의 제목이 hello-1 인 상태
<QuerySet [<Post: Post object (1)>, <Post: Post object (4)>, <Post: Post object (2)>, <Post: Post object (3)>]>

	# 내림차순
>>> Post.objects.order_by('-title')
<QuerySet [<Post: Post object (3)>, <Post: Post object (2)>, <Post: Post object (1)>, <Post: Post object (4)>]>
>>> Post.objects.order_by('-id')
<QuerySet [<Post: Post object (4)>, <Post: Post object (3)>, <Post: Post object (2)>, <Post: Post object (1)>]>
>>> Post.objects.filter(title__contains='-1').order_by('-id')
<QuerySet [<Post: Post object (4)>, <Post: Post object (1)>]>



# offset  💘💘💘💘💘💘 시!!!!!! 험!!!!!!!!!

>>> Post.objects.all()[0]	: #> offset = 0 이고, limit = 1 인 상태와 同
<Post: Post object (1)>		
>>> Post.objects.all()[1]   :  # offset = 1 이고, limit = 1 
<Post: Post object (1)
>>> Post.objects.all()[1:3]  :  # offset = 1 이고, limit = 2
<QuerySet [<Post: Post object (2)>, <Post: Post object (3)>]>
```



### 3. Update

```python
>>> post1 = Post.objects.get(pk=1)
>>> post1
<Post: Post object (1)>
>>> post1.title
'hello-1'
>>> post1.title = 'hello-5'
>>> post1.title
'hello-5'   # 현재 instance 값만 바뀐 상태,  저장은 x
>>> post1.save()  # 여기서 저장
>>> post1
<Post: Post object (1)>
>>> post = Post.objects.get(pk=1)
>>> post.title
'hello-5'
```



### 4. Delete

```python
>>> post = Post.objects.get(pk=1)
>>> post
<Post: Post object (1)>
>>> post.delete()
(1, {'crud.Post': 1})  # 어떤 게시글이 삭제되었는지에 대한 정보를 반환
>>> post
<Post: Post object (None)> # 삭제되어서 더 이상 사용 불가

>>> post.title
'hello-5'  # DB 에서는 사라졌지만, Class instance 는 파이썬 메모리에서 살아있어서 나오는 거임

>>> Post.objects.all()
<QuerySet [<Post: Post object (2)>, <Post: Post object (3)>, <Post: Post object (4)>]>
# DB 에서 삭제는 된 상태
```



##### 강사님이 주석으로 정리해준 거

|                                                              |
| ------------------------------------------------------------ |
| # class Post: Django 에서는 model 이라고 부름
            # DB에서는 table 이라고 부름
            
# post = Post() : Post 클래스의 인스턴스 = post
            # Django 에서는 instance or Object 라고 부름 ( ∵ OOP 에서 Object)
            # DB에서는 Record or Row

# title : Django 에서는 Field
         # DB 에서는 Column 이라고 불림
         
# 마이그레이션
# ./manage.py makemigrations
# ./manage.py migrate

# CRUD
# 1. Create
#   방법1) 
#       post = Post(title='hello-1')
#       post.save()

#   방법2)
#       post2 = Post.objects.create(title='hello-2')

#   방법3)
#       post3 = Post()
#       post3.title = 'hello-3'
#       post3.save()

# 2. Read
# 2-1. All
# posts = Post.objects.all()

# 2-2. One
# 방법 1
# post = Post.objects.get(pk=1)  : id=1, title='hello-1' 도 가능
# 만약에 title='hello-1' 인 글이 여러 개 있으면 get 은 id 번호가 가장 낮은 거 1개만 찾아줌

# 방법 2 (views.py 한정)
# from django.shortcuts import get_objects_or_404
# post = get_object_or_404(Post, pk=1)  # id=1, title='hello-1' 도 가능

# 방법 3
# post = Post.objects.filter(pk=1)[0]  # id=1, title='hello-1' 도 가능
# post = Post.objects.filter(pk=1).first()  # last()  도 있음
# 만약에 title='hello-1' 인 글이 여러 개 있으면 filter 는 모든 글을 가져옴
# 모든 글을 가져와서 리스트에 들어있을 테니까 (post 에) 뒤에 [0] 을 붙이면, 아이디 가장 작은 글 가져옴

# 2-3. Where(filter)
# posts = Post.objects.filter(title='hello-1')
# post = Post.objects.filter(title='hello-1').first()  # 또는 [0]

# LIKE
# posts = Post.objects.filter(title__contains='lo')

# 정렬 : order_by
# posts = Post.objects.order_by('title')  # 제목 오름차순
# posts = Post.objects.order_by('-title')  # 제목 내림차순

# offset & limit  : offset = 앞에 빈 공간을 두는 것
# post = Post.objects.all()[0]  #=> offset=0 limit=1
# post = Post.objects.all()[1]  #=> offset=1 limit=1
# post = Post.objects.all()[1:3]  :  # offset = 1 이고, limit = 2
# post = Post.objects.all()[offset:offset+limit]


# 3. update
# post = Post.objects.get(pk=1)
# post.title = 'hello-5'
# post.save()  # 실제 데이터베이스에 저장


# 4. Delete
# post = Post.objects.get(pk=1)
# post.delete()
# 한 줄로 쓰고 싶다면 
# Post.objects.get(pk=1).delete() |



# 오후수업: orm폴더 / orm 프로젝트 / onetomany 앱

1. 앱생성

   ```bash
   (orm-venv) myccpb08:~/workspace/django/orm (master) $ ./manage.py startapp onetomany
   ```

2. settings.py

   ```python
   INSTALLED_APPS = [
       'onetomany',
   ]
   ```

3. 앱의 모델 만들기

   ```python
   # models.py
   
   from django.db import models
   
   # Create your models here.
   class User(models.Model):
       name = models.TextField()  # 글쓴이의 이름을 담는 column
       
   # User : Post = 1: N
   # ForeignKey : 참조되는 릴레이션의 '기본키'와 대응되어 릴레이션 간에 참조 관계를 표현
   class Post(models.Model):
       title = models.TextField()
       user = models.ForeignKey(User, on_delete=models.CASCADE)  # 이 글을 누가 썼는지 그 사람의 id를 저장?  ex) post.user = 그 사람의 id 
       # USER 라는 COLUMN 에 1이라는 ID 가 저장되어 있음? 
       # 그냥 글쓴이의 이름만 가져오면, user 에는 다양한 정보가 있지만 이름밖에 못 가져옴.
       # 그래서 foreignkey 로 그냥 관계를 만들어 놓으면 다양한 정보를 가져올 수 있음? ㅜㅜㅜㅜ
       
   # User : Comment = 1: N
   # Post : Comment = 1: N
   class Comment(models.Model):
       content = models.TextField()
       user = models.ForeignKey(User, on_delete=models.CASCADE)  # 어떤 유저가 쓴 댓글이냐   물건에 이름을 적어야 누군지 아는 것처럼, 댓글(N쪽) 에 이름(user)을 써야 됨
       post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 어떤 게시글에 대한 댓글이냐
   ```

4. migration 하기

   ```bash
   ./manage.py makemigrations
   ./manage.py migrate
   ```

5. shell_plus  (3. 장고 extension 설치 후에)

   ```bash
   (orm-venv) myccpb08:~/workspace/django/orm (master) $ ./manage.py shell_plus
   ```

   ```python
   >>> user1 = User.objects.create(name='Kim') # User 라는 표에 name='Kim' 으로 작성한 row
   >>> user2 = User.objects.create(name='Lee') # User 라는 표에 name='Lee' 으로 작성한 row
   >>> 
   >>> post1 = Post.objects.create(title='1글', user=user1)
   >>> post2 = Post.objects.create(title='2글', user=user1)
   >>> post3 = Post.objects.create(title='3글', user=user2)
   >>> # # user_id = user1.id , user_id=1, user=user1  완전히 같은 말
   
   >>> c1 = Comment.objects.create(content='1글1댓글', user=user1, post=post1)
   >>> c2 = Comment.objects.create(content='1글2댓글', user=user2, post=post1)
   >>> c3 = Comment.objects.create(content='1글3댓글', user=user1, post=post1)
   >>> c4 = Comment.objects.create(content='1글4댓글', user=user2, post=post1)
   >>> c5 = Comment.objects.create(content='2글1댓글', user=user1, post=post2)
   >>> c6 = Comment.objects.create(content='!1글5댓글', user=user2, post=post1)
   >>> c7 = Comment.objects.create(content='!2글2댓글', user=user2, post=post2)
   ```

   ```python
   # 1. 1번 사람이 작성한 게시글은?
   >>> user1.post_set.all()  # 리스트형식 ∴ 반복문 可
   <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>
   
   # 2. 1번 사람이 작성한 게시글의 댓글의 내용을 출력  (1번사용자가 쓴 글에 1번 사용자가 쓴 댓글 x )
   >>> for post in user1.post_set.all():  # 1번 사람이 작성한 글에 대하여
   ...     for comment in post.comment_set.all():  # 그 글에 달린 모든 댓글 (다른 사람이 쓴 댓글도)
   ...             print(comment.content)   # 출력하라
   
   # 3. c2 를 누가 썼는지
   >>> c2.user
   <User: User object (2)>
   
   # 4. c2 를 작성한 사람이 쓴 글은?
   >>> c2.user.post_set.all()
   <QuerySet [<Post: Post object (3)>]>
   
   # 1이 n 을 부를 때는  _set   ex) user1.post_set.all()
   # n이 1을 부를 때는 그냥 . 만 찍으면 됨  ex) c2.user
   
   # 5. 1번 글의 첫번째 댓글을 쓴 사람의 이름은?
   >>> post1.comment_set.all()[0].user.name  또는
   >>> post1.comment_set.first().user.name
   
   # 6. '1글' 이 제목인 게시글은?
   >>> Post.objects.filter(title='1글')
   <QuerySet [<Post: Post object (1)>]>
   
   # 6-1. 1번 게시글의 댓글들
   >>> Comment.objects.filter(post=post1)
   <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>, <Comment: Comment object (3)>, <Comment: Comment object (4)>, <Comment: Comment object (6)>]>
   
   # 7. 댓글 중에 해당 게시글의 제목이 1글인 것은?
   # 방법1
   >>> Comment.objects.filter(post__title='1글')
   <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>, <Comment: Comment object (3)>, <Comment: Comment object (4)>, <Comment: Comment object (6)>]>
   # 방법2
   >>> post1 = Post.objects.get(title='1글')
   >>> Comment.objects.filter(post=post1)
   <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>, <Comment: Comment object (3)>, <Comment: Comment object (4)>, <Comment: Comment object (6)>]>
   
   # 8. 댓글 중에 해당 게시글의 제목에 '1'이 들어가 있는 것은?
   >>> Comment.objects.filter(post__title__contains='1')
   <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>, <Comment: Comment object (3)>, <Comment: Comment object (4)>, <Comment: Comment object (6)>]>
   ```

   

##### 시험문제

- [ ] 1:1 하려면 어떻게 해야하는가?
- [ ] n:n 하려면 어떻게 해야하는가?
- [ ] offset



