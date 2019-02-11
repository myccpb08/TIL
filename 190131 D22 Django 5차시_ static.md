# 오늘의 <b>作</b> : crud-files 內

Static <-> Dynamic

정적인 파일 관리 ; 서버가 이미지, 음악 등등 정적인 파일을 갖고 있다가, 요청받으면 보여줘

꾸준하게 사용자에게 제공되어야 하는 파일들이라, 한 쪽에 모아놓도록 함(static 폴더 내에서 관리)

1. posts<span style="color:blue">(앱) 안</span>에 `static 폴더` 生 (<span style="color:blue">폴더명 무조건 static</span> ) ( tempaltes 랑 같은 레벨)

2. static 폴더 內 `style.css` 生 (만약 이 css 파일을 index.html 에서 쓴다고 하면)

   ```html
   # index.html
   
   📌{% load static %}  <!--파이썬의 import 와 유사 -->
   
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
       <link rel="stylesheet" href="{% static 'style.css' %}" type="text/css"/> 🔆🔆🔆 여기 여기 문법
   </head>
       
   <body>
       <img src="{% static '2.png' %}"/></img>     🔆🔆🔆 이미지 넣을 땐, static 폴더 內 사진 넣고 이렇게 경로 써주면 됨
       <h1>Post Index</h1>
       <a href="{% url 'posts:new' %}">글쓰기</a>
       <ul>
       {% for post in posts %}
           <li><a href="{% url 'posts:detail' post.pk %}">{{ post.title }}</a></li>
       {% endfor %}
       </ul>
   </body>
   </html>
   ```

   

   ✅ 만약에 static 內 test 라는 폴더 안에 css 가 들어가있으면  <span style="color:orange"><b>href</b></span> 부분을`{% static 'test/style.css' %}`

   ✅ <span style="color:blue">임의의 경로</span>에 static 폴더 성질을 가진 폴더를 만들고 싶으면( <span style="color:blue">앱 폴더 밖</span>, <span style="color:blue">폴더名 자유</span>)  <u>settings.py 제일 마지막 줄</u>에 下 작성

   ​	ex) crud 폴더 내에 `assets` 폴더 內 `public.css` 를 넣었다고 가정

   ```python
   # windows : \
   # Linux : /
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'crud', 'assets'),
       ] # BASE_DIR : 가장 윗 줄에 정의되어 있음        프로젝트 폴더の 최상단을 뜻함       이 경우,  crud-files 폴더      =      즉,  프로젝트의 루트 폴더
         # crud : 루트 폴더 안에 'crud' 폴더 뜻함
         # assets : 'crud' 안에 'assets' 폴더 뜻함
         # 이 경로들을 합쳐주는 join >> 하나의 path 가 生  (경로들도 일종의 문자열이니까)
         # os.path = '/' 뜻함. 리눅스니까
         # assets 는 다른 폴더명 써도 可
         # 이렇게 해 두면, assets 폴더 안에 있는 css 도 가져올 수 있음
   ```

   이렇게 하고 

   ```html
   # index.html
   
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
       <link rel="stylesheet" href="{% static 'public.css' %}" type="text/css"/>  🔆🔆🔆 여기 여기 문법. 별도의 폴더명 안 써주고 그냥 이렇게 쓰면 됨
   </head>
   <body>
       <img src="{% static '2.png' %}"/></img>
       <h1>Post Index</h1>
       <a href="{% url 'posts:new' %}">글쓰기</a>
       <ul>
       {% for post in posts %}
           <li><a href="{% url 'posts:detail' post.pk %}">{{ post.title }}</a></li>
       {% endfor %}
       </ul>
   </body>
   </html>
   ```







## 👀 글쓰기 할 때, 텍스트 말고 <span style="color:red">이미지도 올려보자</span>

1. 글쓰기 폼에, 이미지파일을 load 할 박스를 추가해 줘야 한다 = `new.html` 로 go

   * imag 업로드를 하기 위한, input 박스를 <b>加</b>

     ```html
     # new.html
     
     <body>
         <!--method : get, post -->
         <!-- enctype : multipart/form-data (binary 전송 가능) -->
         <!--         : application/x-www-form-urlencoded (기본 값) 즉, enctype 안 적었을 때 -->
         <form action="{% url 'posts:create' %}" method="post" enctype="multipart/form-data"> 📌📌 여기
             {% csrf_token %}
          
             <input type="text" name="title"/>
             <input type="text" name="content"/>
             <input type="file" name="image" accept="image/*"/>   📌📌📌📌여기
             <input type="submit" value="제출"/>
         </form>    
     </body>
     ```

     * 이미지를 넣을 박스에 image 관련 확장자만 받아라   <span style="color:orange">accept</span>=<span style="color:green">"image/*"</span>     * 은 확장자 의미

     * 이미지를 post 요청 할 때는 추가 속성이 필요하다,  method="post" 뒤에 <span style="color:orange">enctype(인코딩타입)</span> 

     * 기본 post 는 텍스트형태로 압축하여 넘겨주는데  <span style="color:green">multipart</span> 추가해주면, binary 형태도 보낼 수 있게 된다 (이미지도 전송할 수 있게 됨)

       

2. class 에 image 자리가 있어야 들어가니까 class 수정해야한다 = `models.py` 로 go >> migrations 하기

   ```python
   from django.db import models
   
   class Post(models.Model):
       title = models.CharField(max_length=100)
       content = models.TextField()
       image = models.ImageField(blank=True) # 이 칼럼에는 빈칸이어도 된다
       created_at = models.DateTimeField(auto_now_add=True) # 언제 生되었는지에 대한 정보: 하나의 데이터가 생성될 때(딱 한 번) 현재 시간을 넣어
       updated_at = models.DateTimeField(auto_now=True) # 언제 업데이트 되었는지에 대한 정보 : 변경이 될 때 마다, 현재 시각 
       # 이 두 줄은 맨 밑에 추가정보로 有
       
       def __str__(self):
           return self.title
   ```

   * <span style="color:green">ImageField</span>는 그냥 사용할 수 無 : bash 에서 `pip install Pillow` 해야 함  (Python image library)
   * 파일 사용하고 싶으면 FileField()



3. 받은 이미지를 Post 라는 클래스에 추가 저장해주는 작업을 해야 한다 = `views.py` 內 `def create` 로 go

   ```python
   from django.shortcuts import render, redirect
   from .models import Post, Comment
       
   def create(request):
       title = request.POST.get('title')
       content = request.POST.get('content')
       image = request.FILES.get('image')  # 파일이라서 POST 아니고 📌📌📌FILES 
       post = Post(title=title, content=content, image=image)   # 이미지 자리 만들어주기
       post.save()
       return redirect('posts:detail', post.pk)
   ```



4. 가져온 이미지를  detail 화면에서 보여주기 위해서는 `detail.html` 수정

   ```html
   <body>
       <h1>Post Detail</h1>
       <img src="{{ post.image.url }}"></img>     ✅ 그냥 post.image 하면 안 되고, url 까지 적어야 함
   ......
   </body>
   ```

   

5. 그런데 사진은 `setting.py` にも 추가 설정이 필요하다. (사용자가 올린 image 파일을 어디에 저장하고, 가져올 거야?)

   : 사진 올리면 `media` 폴더 <b>生</b> 되고, 그 안에 이미지가 <b>入</b>

   ```python
   # Media Files
   MEDIA_URL = '/media/' # 임의의 값 사용 가능
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # media 라는 폴더명은 자유 / 사용자가 업로드한 이미지 파일을 어느 파일에 올릴 거니? = media 파일 가져올 때, 이 폴더 뒤져라
   ```

   

6. 프로젝트의 `urls.py` 수정도 필요하다. 이미지 파일 읽어오려고

   ```python
   # import 2줄
   
   from django.conf.urls.static import static
   from django.conf import settings  # settings.py 파일 가져오기
   
   # 맨 밑에 추가
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

   

   <hr>

## 이미지가 화면에 보여지기 전에, <span style="color:blue">사이즈나 해상도 조절</span>하기

: 위 방식에서 끝내면, 원본 사진으로 올라가는데, 사이즈가 중구난방이니까, 사전처리가 필요



1. `djago-imagekit` 이라는 모듈 필요 : bash 에 설치하기

   `pip install pilkit` 打

   `pip install django-imagekit pilkit` 打



2. `setting.py` 로 가서  installed_app 에 imagekit 추가

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'imagekit', 📌 이거
       'posts.apps.PostsConfig',
   ]
   ```

   

3. `models.py` 수정

   * import 2가지

     ```python
     from django.db import models
     from imagekit.models import ProcessedImageField   # 원래 models.ImageField 를 대체할 아이
     from imagekit.processors import ResizeToFill # 이미지가 업로드되는 과정에서 어떤 조작과정을 거칠지
     ```

   * image 칼럼부분 수정

     ```python
     class Post(models.Model):
         title = models.CharField(max_length=100)
         content = models.TextField()
         
         # image 칼럽 수정
         
         image = ProcessedImageField(
                 upload_to = 'posts/images',      # 어디에 업로드 될 것인지 = 저장위치   
                 processors = [ResizeToFill(300,300)],  # 업로드 되면 무슨 처리과정을 거칠지. 가로 세로 300으로 바꿔/  이 값들 단순 변경은 migrations 안 해도 됨
                 format='JPEG', # 저장 포맷 (확장자)
                 options={'quality':90}, # 저장 포맷 관련 옵션 : jpeg 는 압축스타일이라 얼마나 퀄리티로 압축할지
             )
             
         created_at = models.DateTimeField(auto_now_add=True)
         updated_at = models.DateTimeField(auto_now=True)
         
         def __str__(self):
             return self.title
     ```

      * ResizeToFill : 300, 300 맞추고 넘치는 부분 잘라냄 (600*400 이면,  300**300 설정했을 때, 

        ​											    짧은 길이를 300에 맞추고, 가로의 넘치는 부분은 잘라냄)

      * ResizeToFit : 300, 300 맞추고 남는 부분은 빈 공간으로 둠



4. models.py 바궜으니까 migations 해





<hr>

✅ DB 초기화 하는 법  : 

​	① `migrations/__pycache__` 폴더 內 `000#` 붙은 파일들 모두 삭제

​	② `db.sqlite3` 파일 삭제

​	③ `superuser 계정` 새로 生

