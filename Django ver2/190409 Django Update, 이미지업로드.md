### update 페이지 만들기

```python
# views.py  (create 와 유사)

def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':  # 그냥 submit 버튼 눌렀을 때
        post_form = PostForm(request.POST, instance=post)  
        										# 수정페이지니 원래 있던 내용 보여주려고, instance
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
        
    else:  # get요청 = 주소창에 주소 입력했을 때
        post_form = PostForm(instance=post)
    return render(request, 'posts/create.html', {'post_form':post_form})
```

```python
# urls.py

urlpatterns = [
    path('<int:post_id>/update/', views.update, name='update'),]
```

```html
<!-- 리스트 페이지에 edit 버튼 만들기 -->
<!-- _post.html  -->

<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <p class="card-text">{{ post.content }}</p>
    <a href="{% url 'posts:update' post.id %}" class="btn btn-primary">Edit</a>  📌Edit 버튼
    <a href="{% url 'posts:delete' post.id %}" class="btn btn-danger">Delete</a>
  </div>
</div>
```



### 이미지 업로드 하기 (길다 길어....)

1. 이미지관련 python 라이브러리 설치

   ```bash
   # bash
   pip install pillow
   ```

2. 이미지넣기위한 작업

   ```python
   # 이미지를 넣을 수 있도록 models.py  수정
   from django.db import models
   
   class Post(models.Model):
       content = models.TextField()
       image = models.ImageField(blank=True)
   ```

   ```bash
   # DB 를 건들였으니 migrations 해야 됨 (bash)
   
   ./manage.py makemigrations
   ./manage.py migrate
   ```

   ```python
   # 이미지 폼을 받아올 수 있돋록 forms.py 수정
   from django import forms
   from .models import Post
   
   class PostForm(forms.ModelForm):
       class Meta:
           model = Post    # 어떠한 모델의 폼을 작성할 거니? Post 라는 모델의 폼을 만들거야
           fields = ['content','image',]   # models.py 에 작성된 Post 클래스의 content 와 이미지필드
   ```

   ```html
   # 새글 작성하는 html = create.html 에 이미지업로드 할 수 있도록 수정
   
   <!-- post 방식으로 보낼 때, 어떤 방식으로 보낼 지 정해주는 enctype 을 추가해서 적어줌 -->
   <!-- 기본값은 text 만 보내도록 설정되어 있어서, 이미지를 올릴 때는 enctype 를 적어줘야함 -->
   
   {% extends 'base.html' %}
   {% load bootstrap4 %}
   {% block container %}
   
   <h1>New Post</h1>
   <form action =""  method ="post" enctype="multipart/form-data"> 📌
       {% csrf_token %}
       {% bootstrap_form post_form %}
       {% buttons %}
           <button type="submit" class="btn btn-primary">Submit</button>
       {% endbuttons %}
   </form>
   {% endblock %}
   
   ```

   ```PYTHON
   # Views.py 수정(request 추가)
   def create(request):
       if request.method =='POST':
           post_form = PostForm(request.POST, request.FILES)  
           
           # 이미지는 단순 post 요청아니고, files 라서 추가 해줘야 하고, 
           # 꼭 post 먼저 쓰고, files 적어야 함
           # 원래는 `data=request.POST, files = request.FILES`  구문임
           
           if post_form.is_valid():  # 저장해도 되는 값이 들어왔으면
               post_form.save()  # 저장하고
               return redirect('posts:list')   # 리스트페이지를 보여줘
               
           
       else:  # get방식이면
           post_form = PostForm()
           
       return render(request, 'posts/create.html', {'post_form' : post_form})
   
   
   # 수정함수에서도 이미지 추가삭제 할 수 있도록 REQUEST 추가
   def update(request, post_id):
       post = get_object_or_404(Post, id=post_id)
       if request.method == 'POST':  # 그냥 submit 버튼 눌렀을 때
           post_form = PostForm(request.POST, request.FILES, instance=post)
           if post_form.is_valid():
               post_form.save()
               return redirect('posts:list')
           
       else:  # get요청 = 주소창에 주소 입력했을 때
           post_form = PostForm(instance=post)
       return render(request, 'posts/create.html', {'post_form':post_form})
   ```

   #### 업로드 한 파일을 저장할 위치를 저장해주기 

   #### (create 페이지에서 사진 업로드해서 새글작성하면 자동 生)

   ```python
   # settins.py   가장 마지막 줄에 추가 작성 (125line)
   # Media
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

   ```python
   # 전체 urls.py 수정,
   # 사용자가 업로드한 이미지의 주소를 만들어주기 위하여
   
   from django.contrib import admin
   from django.urls import path, include
   from django.conf.urls.static import static
   from django.conf import settings
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('posts/', include('posts.urls')),
   ]  
   
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
   # 여기서 MEDIA_ROOT = 위에서 만들어진 media 폴더
   ```

   ```html
   <!-- 위에서 만들어진 링크를 src 에 넣어주면 됨 -->
   <!-- _post.html -->
   
   <div class="card" style="width: 18rem;">
     <img src="{{ post.image.url }}" class="card-img-top" alt="{{ post.image }}">
     <div class="card-body">
       <p class="card-text">{{ post.content }}</p>
       <a href="{% url 'posts:update' post.id %}" class="btn btn-primary">Edit</a>
       <a href="{% url 'posts:delete' post.id %}" class="btn btn-danger">Delete</a>
     </div>
   </div>
   
   <!-- 만약 이미지가 없는 글에 대해서 오류를 발생시키고 싶지 않다면 if 문 추가 -->
   
   <div class="card" style="width: 18rem;">
     {% if post.image %} 📌
     <img src="{{ post.image.url }}" class="card-img-top" alt="{{ post.image }}">
     {% endif %} 📌
     <div class="card-body">
       <p class="card-text">{{ post.content }}</p>
       <a href="{% url 'posts:update' post.id %}" class="btn btn-primary">Edit</a>
       <a href="{% url 'posts:delete' post.id %}" class="btn btn-danger">Delete</a>
     </div>
   </div>
   ```




### 이미지 resizing 하기

1. resizing 관련 라이브러리 설치

   ```bash
   # bash
   pip install pilkit django-imagekit
   ```

2. settings.py 의 installed apps 에 `imagekit` 추가

   ```python
   INSTALLED_APPS = [
       'bootstrap4',
       'imagekit',
       'posts',
   ]
   ```

3. models.py 수정

   ```python
   # 앞에 버전은 업로드한 사진 원본 그대로 저장되는 것 (사이즈 너무 크면 이상...)
   # 얘는 이미지를 업로드할 때 resizing 된 사진이 저장
   
   from django.db import models
   from imagekit.models import ProcessedImageField
   from imagekit.processors import ResizeToFill 
   # processors 툴에 흑백변환같은 효과 有, 공식문서 찾아보고 쓰면 됨
   
   class Post(models.Model):
       content = models.TextField()
       #image = models.ImageField(blank=True)   ✅ 그냥 저장 되는 코드
       image = ProcessedImageField(             ✅ RESIZING 되어 저장되는 코드
           upload_to = 'posts/images', # 저장위치 (글을 삭제해도 사진은 남는다)
           processors=[ResizeToFill(600,600)], # 처리할 작업 목록, 
                                   		   # RESIZE 방법 몇 가지 있음 (TOFILL 이랑 ....)
           format = 'JPEG', # 저장 포맷
           options = {'quality':90}, # 옵션
           )
   ```

4. 모델 건들였으니, 다시 migrate

   ```bash
   # bash
   ./manage.py makemigrations
   ./manage.py migrate
   ```



### 올린 게시글에 따라 사진 분류해서 넣기

1. models.py 수정 (새로운 함수 만들)

   ```python
   from django.db import models
   from imagekit.models import ProcessedImageField
   from imagekit.processors import ResizeToFill
   
   # instance = 게시글? 
   def post_image_path(instance, filename):
       #return 'posts/{}/{}'.format(instance.content, filename)  : 아래 문장이랑 동일
       return f'posts/{instance.content}/{filename}'
       
       # instance.content 대신 instance.pk 하면 문제 생김
       # 아직 db에 들어가(저장되)기 전에, 이미지를 어디에 넣을지 정하는 단계라서, pk값이 아직 없다
       # 수정할 때는 pk 값이 있는 상태니까 정상처리되긴 하지만, 잘 쓰지 않는다
       
   class Post(models.Model):
       content = models.TextField()
       image = ProcessedImageField(
           #upload_to = 'posts/images',     # 저장위치 (모든 게시글의 사진이 하나의 폴더로 들어감)
           upload_to = post_image_path,     # 함수자체를 넘기는 것, 함수를 reference
           							  # 각 글마다 새로운 폴더를 만들어서, 이미지를 분류함
           processors=[ResizeToFill(600,600)],
           format = 'JPEG',
           options = {'quality':90},
           )
   ```

   