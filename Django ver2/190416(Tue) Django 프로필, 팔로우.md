## 오늘의 할 일1.  :  프로필 만들기

#### 1. '프로필' 이라는 model 만들기 (User : 프로필 = 1:1)

- 프로필은 계정과 관련된 model  	∴  accounts / models.py 에 筆

  ```python
  # accounts / models.py
  
  from django.db import models
  from imagekit.models import ProcessedImageField
  from imagekit.processors import ResizeToFill
  from django.conf import settings
  
  class Profile(models.Model):
      user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 📌📌
      # user 삭제되면 프로필도 필요없으니 CASCADE 옵션
      
      # 아래, 닉네임과, 소개, 이미지는 회원가입시 필수사항이 아니므로 빈칸 허용
      nickname = models.CharField(max_length=40, blank=True)  # 닉네임 작성
      introduction = models.TextField(blank=True)  # 자기소개 작성
      image = ProcessedImageField(  # 프로필 이미지
          	    blank=True,
                  upload_to = 'profile/images',  #이미지 저장 위치
                  processors=[ResizeToFill(300,300)], # 처리할 작업 목록
                  format = 'JPEG', # 저장 포맷
                  options = {'quality':90}, # 옵션
          )
  ```

  ```bash
  # migrte 하기
  ./manage.py makemigrations
  ./manage.py migrate
  ```



* admin 페이지에서 프로필을 확인할 수 있도록 admin.py 에 등록

  ```python
  # accounts / admin.py
  
  from django.contrib import admin
  from .models import Profile
  
  admin.site.register(Profile)
  ```



* 회원가입하는 과정에서 바로 프로필 만들어주기

  ```python
  # views.py
  
  from django.shortcuts import render, redirect, get_object_or_404
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
  from django.contrib.auth import login as auth_login
  from django.contrib.auth import logout as auth_logout
  from django.contrib.auth import get_user_model, update_session_auth_hash
  from django.contrib.auth.decorators import login_required
  from .forms import CustomUserChangeForm
  ✅ from .models import Profile
  
  def signup(request):
      if request.user.is_authenticated:
          return redirect('posts:list')
          
      if request.method == 'POST':
          signup_form = UserCreationForm(request.POST)
          if signup_form.is_valid():
              # 회원가입하면, 바로 로그인 시켜주도록 하기
              user = signup_form.save()
              Profile.objects.create(user=user)  # 📌User의 Profile 생성
              auth_login(request,user)
              return redirect('posts:list')
          
      else:
          signup_form = UserCreationForm()
      return render(request, 'accounts/signup.html', {'signup_form': signup_form})
  ```

  ​	+) db.sqlite3 삭제하면 그동안 만든 user 들 다 날아감

  

#### 2. 프로필 업데이트 페이지 만들기 ( 페이지 만듦 = views.py 에 筆, form 이용)

```python
# views.py
def profile_update(request):
    return render(request, 'accounts/profile_update.html')
```

```python
# urls.py
path('profile/update/', views.profile_update, name='profile_update'),
```

```html
<!-- profile_update.html 作 → 筆 -->
{% extends 'base.html' %}
{% block container %}
<h1>Profile Edit</h1>

{% endblock %}
```

* 수정할 時 사용할 form 만들기

  ```python
  # forms.py
  
  from django import forms
  from django.contrib.auth.forms import UserChangeForm
  from django.contrib.auth import get_user_model
  from .models import Profile
  
  class ProfileForm(forms.ModelForm):
      class Meta:
          model = Profile
          fields = ['nickname', 'introduction', 'image',]
  ```

* views.py 추가 수정

  ```python
  from .forms import CustomUserChangeForm, ProfileForm
  
  def profile_update(request):
      profile = request.user.profile
      if request.method == 'POST':
          profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
          if profile_form.is_valid():
              profile_form.save()
              return redirect('people', request.user.username)
              
      else:
          profile_form = ProfileForm(instance=profile)
      return render(request, 'accounts/profile_update.html', {'profile_form':profile_form})
  ```

* profile_update.html 수정

  ```html
  {% extends 'base.html' %}
  {% load bootstrap4 %}
  {% block container %}
  <h1>Profile Edit</h1>
  
  <form method="POST" enctype="multipart/form-data"> <!--프로필 사진올릴때 enctype 필요 -->
      {% csrf_token %}
      {% bootstrap_form profile_form %}
      <input type="submit" value="Submit"/>
  </form>
  
  {% endblock %}
  ```



#### 3. 프로필을 개인페이지에 보여주기

```html
<!-- people.html -->

{% extends 'base.html' %}
{% block container %}

<div class="container">
    
    📌📌📌📌 <!-- 여기부터 筆 -->
    <div class="row">
        <div class="col-3">
             {% if people.profile.image %}
            <img src="{{ people.profile.image.url }}" width="50" 
                 alt="{{ people.profile.image }}"></img>
            {% endif %}
            <h1>{{ people.username }}</h1>
        </div>
        <div class="col-9">
            <div>
                <strong>{{ people.profile.nickname }}</strong>
            </div>
            <div>
                {{ people.profile.introduction }}
            </div>
        </div>
    </div>
    <!-- 여기까지 -->
    
    {% if user == people %}  
    <!-- 현재 로그인 사람과, user 가 같으면 , 회원정보수정페이지와 프로필수정페이지 링크 보여줘 -->
    <div>
        <a href="{% url 'accounts:profile_update' %}">프로필 정보 수정</a><br> 📌📌
        <a href="{% url 'accounts:update' %}">계정 정보 수정</a>
    </div>
    {% endif %}
    
    <div class="row">
        {% for post in people.post_set.all %}
        <div class="col-4">
            <img src="{{ post.image_set.first.file.url }}" class="img-fluid"/> <!--post 가 가지고 있는 첫번째 파일 url -->
        </div>
        {% endfor %}
    </div>
</div>

{% endblock %}
```



## 오늘의 할 일 2: 팔로우기능 (user: user = n:n)

#### 1. 새로운 user 모델 만들기

```python
# models.py
# AbstractUser  import   (완벽한 user 모델[살까지 다 붙여진거] 말고, 좀 빠진 abstractuser[骨] )
# models.Model < class AbstractBaseUser < class AbstractUser < class User (左向 : 骨)
# class User 는 커스터마이징 不可  ∴ AbstractUser 상속

from django.contrib.auth.models import AbstracUser
class User(AbstracUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings') 
    # 이렇게 하면 장고가 제공하는 USER 클래스가 들어가있음
    # 후에, 우리가 만든 User 로 바꿔주는 설정 해줘야됨 (밑에 override 과정)
    # 그래야 오류가 안 남
    # user.followings 랑 user.followrs 둘 다 가능하다. (무슨말이지?)
```

```python
# settings.py 가장 마지막 줄

# Auth User Model
AUTH_USER_MODEL = 'accounts.User'  # 앱名.User  (장고가 user 를 생성할 때, account 앱에서 정의한 user 를 사용하겠다라고 인식하도록)
```

* 내가 만든 User 로 User 를 갈아끼웠기 때문에, DB를 날려줘야함 
  (dbsqulite3 와 , accounts /migrate 폴더 내 0001 파일 삭제 )

* db 를 건들였으니, migrations 랑 migrate 하기

* 📌📌📌📌 여기까지 하고, 페이지에서 회원가입을 진행하면, 에러남

  `Error: Manager isn't available; 'auth.User' has been swapped for 'accounts.User' `

  `settings 에서 변경해주었다고 해도, 회원가입할 때, 바로 반영이 안 됨 ∴ 새로 override 작업 要`

  

#### 2. user 모델 override

```python
# forms.py, UserCreationform 을 import 
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
```

```python
# views.py

from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm 
📌# 우리가 만든 CustomUserCreationForm 넣기

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST) 📌 # CustomUserCreationForm 으로 변경
        if signup_form.is_valid():
            # 회원가입하면, 바로 로그인 시켜주도록 하기
            user = signup_form.save()
            Profile.objects.create(user=user)  # User의 Profile 생성
            auth_login(request,user)
            return redirect('posts:list')
        
    else: # get 방식 요청
        signup_form = CustomUserCreationForm() 📌 #CustomUserCreationForm 으로 변경
    return render(request, 'accounts/signup.html', {'signup_form': signup_form})
```



#### 3. 팔로우기능 함수, 링크, 페이지 만들기

```python
# views.py

def follow(request, user_id):
    people = get_object_or_404(get_user_model(), id=user_id)
    
    # 1. people 을 unfollow 하기
    # 이 사람을 follow 하는 사람들의 리스트 = people.followers
    if request.user in people.followers.all(): # 이미 팔로우 목록에 있으면
        people.followers.remove(request.user)   # action 은 팔로우취소
    
    # 2. people을 follow 하기
    else: # 팔로우 중이 아니면
        people.followers.add(request.user) # 리스트에 나를 추가 (add)
    return redirect('people', people.username)
```

```python
# urls.py
path('<int:user_id>/follow/', views.follow, name='follow'),
```

```html
<!-- people.html -->
<!-- 개인 페이지에, 팔로우버튼 만들기 -->

{% if user != people %}  <!-- 현재 사용자말고 타인의 페이지일 경우에만 follow 버튼 보여줘 -->
    {% if user in people.follower.all %}
    	<a href="{% url 'accounts:follow' people.id %}">팔로우취소</a>
    {% else %}
    	<a href="{% url 'accounts:follow' people.id %}">팔로우</a>
    {% endif %}
{% endif %}


<!-- follow 하는 사람 수 보여주기 -->
<div>
    <strong>Followers:</strong> {{ people.followers.count }}  
    <!--people을 팔로우 하고 있는 사람 수 -->
    <strong>Followings:</strong> {{ people.followings.count }} 
    <!-- 내가 팔로우 하고 있는 사람 수 -->
</div> 

```



#### 4. 내가 팔로우 한 사람의 글만 리스트페이지에 보이도록 하기

* 리스트 페이지는 posts 앱에서 하는 거니까, posts / views.py / def list 수정

  ```python
  @login_required  # 팔로우 관련이므로, 이제 리스트페이지도 로그인해야됨
  def list(request):
      #posts = Post.objects.order_by('-id').all() : 원래 썼던 문장
  
      # 1. 내가 follow 하고 있는 사람들의 리스트
      followings = request.user.followings.all()
      
      # 2. 이 사람들이 작성한 글들만 뽑아옴
      posts = Post.objects.filter(user__in=followings).order_by('-id')
      		# user 아이디가 followings 에 있는 사람들 글만 posts 에 넣음
      comment_form = CommentForm()
      return render(request, 'posts/list.html', {'posts':posts, 'comment_form':comment_form})
  ```

* 리스트 페이지에서 , 유저 옆에 사진보이기

  ```html
  <!--   _post.html -->
  
  {% if post.user.profile.image %}  <!-- user 가 사진이 있으면 -->
      <img src="{{ post.user.profile.image.url }}" width="25" alt="">
  {% endif %}
      <span>{{ post.user.username }}</span>
  ```

  * 그런데 위의 단계로 마치면, 현재 list 페이지에서 내가 쓴 글은 안 보임 (∵ 나는 나를 팔로잉하는 리스트에 x)
  * ∴ # 1. 부분을 수정해야한다

  ```python
  # views.py
  from itertools import chain
  # 1. 내가 follow 하고 있는 사람들의 리스트 >> 나를 추가
      followings = request.user.followings.all()
      # 1-1. followings 변수와 나를 묶
      followings = chain(followings, [request.user])
  ```



#### 5. 그냥 모든 글 페이지 보여주는 링크

```python
# views.py
def explore(request):
    posts = Post.objects.order_by('-id').all()
    comment_form = CommentForm()
    return render(request, 'posts/list.html', {'posts':posts, 'comment_form':comment_form})

# posts/urls.py
path('explore/', views.explore, name='explore'),
```

* navbar 에 explore 갈 수 있도록 추가

  ```html
  <!-- base.html -->
  <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
          
          📌📌📌 <!-- 아래 3줄 -->
        <li class="nav-item">
            <a class="nav-link" href="{% url 'posts:explore' %}">Explore</a>
        </li>
        
        
        {% if user.is_authenticated %}  <!--로그인 되어 있으면 -->
          <li class="nav-item">
            <a class="nav-link" href="{% url 'posts:create' %}">New Post</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">{{ user.username }}</a>     
              <!--user 는 장고가 전체 템플릿에서 로그인 되어 있으면 읽어올 수 있도록 해 놨음 -->
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'accounts:logout' %}">Logout</a>
          </li>
        {% else %}
          <li class="nav-item">
            <a class="nav-link" href="{% url 'accounts:login' %}">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'accounts:signup' %}">Sign up</a>
          </li>
        {% endif %}
      </ul>
    </div>
  ```

  