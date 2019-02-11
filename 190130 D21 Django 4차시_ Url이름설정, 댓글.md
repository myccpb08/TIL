어제까지는 링크를 손으로 하나하나 흐름에 따라, 맞춰줬는데

이러면 불편함이 有 (실수로 / 를 뺀다거나, 오타가 난다거나) ▶ Django 는 각각의 url 에 이름을 붙여서 한꺼번에 변경 가능하도록 기능을 제공한다



1) urls.py 가 어디 소속인지 명시해야 한다

```python
# urls.py 에

from django.urls import path
from . import views

app_name = 'posts'  # 이 urls.py 주인은 posts 다
```

2) 각 url 의 <b>名</b> 을 <b>立</b>

```python
urlpatterns = [
    path('', views.index, name='list'),     			# name = ' '   으로 각 url の 名 을 정해준다
    path('create/',views.create, name='create'),
    path('new/', views.new, name='new'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),  
]
```

3) views.py 에서 링크들을 立한 名으로 變

```python
def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts:list') 📌📌📌📌 여기   ('설정한 app_name: 링크 name')


#어제까지 했던 모양은
→ return redirect('/posts/')

-----------------------------------------------------------------------------------------

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    post = Post(title=title, content=content)  
    post.save()				              📌📌📌📌 여기
    return redirect('posts:detail', post.pk)  # path('<int:post_id>/', views.detail, name='detail'),    인데
						         # detail 이란 url 은 변수가 필요하니까   콤마찍고 변수 넣어줌
    
    
#어제까지 했던 모양은
→ def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    post = Post(title=title, content=content)
    post.save()
    return redirect(f'/posts/{post.pk}') 

```



4) html 에도 링크 變

```html
# index. html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Post Index</h1>
    <a href="{% url 'posts:new' %}">글쓰기</a>    🔆🔆🔆🔆 <!--   이 부분 변경, 진자문법  --->
    <ul>
    {% for post in posts %}
        <li><a href="{% url 'posts:detail' post.pk %}">{{ post.title }}</a></li> 🔆🔆🔆🔆 <!--   이 부분 변경, 진자문법, 콤마 ❌ 띄어쓰기로 구분  --->
    {% endfor %}                             <!-- ↑ 변수 필요한 거 콤마 안 쓰고 띄어쓰기로 구분-->
    </ul>
</body>
</html>


--------------------------------------
# 이전 꺼 모양은

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Post Index</h1>   
    <a href="/posts/new/">글쓰기</a>          📌📌📌📌 여기
    <ul>
    {% for post in posts %}
        <li><a href="/posts/{{post.pk}}">{{ post.title }}</a></li>      📌📌📌📌 여기
    {% endfor %}
    </ul>
</body>
</html>
```



## <b>댓글기능 구현하기</b>

<포스트: <span style="color:red">댓글</span> =  1:<span style="color:red">N</span>>

* <span style="color:red"><b>on_delete</b></span> 옵션 : post 가 사라졌을 때 <u>(내가 댓글 단 글이 사라졌을 때)</u> 댓글 어떻게 처리할 거야?

  * <span style="color:blue">CASCADE</span> : 부모가 삭제되면(댓글단 글이 사라지면), 자기 자신도 삭제(댓글도 삭제)
    		     ex)보통글

  * PROTECT : 자식이 존재하면(댓글이 달려 있으면), 부모 삭제 불가능(글 삭제 불가능)
                         ex)지식인?

  * SET_NULL : 부모가 삭제되면, 자식의 부모 정보를 NULL로 변경
                        ex)내가 쓴 댓글목록에서는 댓글이 보이지만, 글누르면 x

    ```python
    # models.py
    
    class Comment(models.Model):
        # 어떤 게시글에 대한 댓글인가 = 게시글 정보
        # 댓글 쓸/쓴 글 = post ( 외부 테이블 foreignkey 로부터 id 를 가져와서 게시글 지정_)
        post = models.ForeignKey(Post,on_delete=models.CASCADE)  # 외부키 = foreignkey (=다른 테이블의 키 값을 가져와서 쓸 거야)
                                                                 				     # 무슨 외부 테이블 쓸거야? Post
        content = models.TextField()
        
        
        ⭕⭕⭕⭕ views.py 맨 위에 Comment 임포트 시켜야함
    ```

    

<下 terminal 에서 打>

장고에서 파이선 쉘 실행 : `python manage.py shell`

models 에서 작성한 클래스 사용하려고 import : `from posts.models import Post, Comment`   = `from 앱名.models import 클래스名`

클래스에 가장 마지막으로 저장한 데이터 불러와서 post 라는 변수에 넣음 `post = Post.objects.last()` = `변수名 = 클래스名.objects.last()`

댓글 추가하기 `c = Comment(post=post, content='댓글입니다') `  : 📌위에서 불러온 post 라는 글에 댓글 달기

댓글 추가한 거 저장 `c.save()`

댓글 다 불러오는 것 `Comment.objects.all()`   = `클래스名.objects.all()`    

해당 글에 달린 댓글 불러 오기 `post.comment_set.all()`   = `post.클래스名_ set.all()`    <span style="color:red">✔</span> admin 에서 할 때는 all 로 끝

pk가 1인 댓글 가져와서 c에 저장 `c = Comment.objects.get(pk=1)`

c가 달린 글의 제목 가져오기 `c.post`  치면  <<Post:제목>> 반환

c.post.title : 해당 글의 제목 반환

c.post.content : 해당 글의 내용 반환

`post.comment_set.first().content` : 해당 글에 달린 첫번째 댓글의 내용을 보여줌

쉘 종료는 `ctrl+d`

------ 장고 쉘은 쓰기 어려우니까 admin 으로 만지도록 하자 👍-----



```python
# admin.py

from django.contrib import admin
from .models import Post, Comment✅

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content',)


admin.site.register(Post, PostAdmin) 
admin.site.register(Comment)✅
```

댓글은 글 하단에 작성하는 거니까, detail 페이지로

## <span style="color:blue">댓글 작성</span>

```html
# detail.html

<body>
    <h1>Post Detail</h1>
    <h2>Title : {{post.title}} </h2>
    <p>Content : {{post.content}} </p>
    <a href="{% url 'posts:list' %}">List</a>
    <a href="{% url 'posts:edit' post.pk %}">Edit</a>
    <a href="{% url 'posts:delete' post.pk %}">Delete</a>
    
    <hr>
    
    <form action="{% url 'posts:comments_create' post.pk %}" method="post">       <!-- form 에 댓글 내용 담아서 실어 보냄 -->
        {% csrf_token %}
        댓글 : <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
```



```python
# urls.py

urlpatterns = [
    path('', views.index, name='list'),
    path('create/',views.create, name='create'),
    path('write/', views.new, name='new'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/comment/create/', views.comments_create, name='comments_create')📌이거
]
```





```python
# views.py

# 댓글 만드는 역할
def comments_create(request, post_id):
    # 댓글을 달 게시물 가져오기
    post = Post.objects.get(pk=post_id)
    
    # detail form 칸에 담겨서 날아온 댓글 내용
    content = request.POST.get('content')
    
    # 댓글 생성 및 저장
    comment = Comment(post=post, content=content)
    comment.save()
    
    # 댓글 쓴 글의 디테일 페이지로 가기
    return redirect('posts:detail', post.pk)
```



## <span style="color:blue">댓글 목록 보여주기</span>

```html
# detail.html
<form action="{% url 'posts:comments_create' post.pk %}" method="post">
        {% csrf_token %}
        댓글 : <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>

    <ul>
        {% for comment in post.comment_set.all %}   <!-- 파이썬 쉘이랑 다름 괄호 없어! -->
        <li> {{ comment.content }} </li>
        {% endfor %}
    </ul>
```

![](C:\Users\student\Desktop\메일\이미지\제목 없음11.png)

## <span style="color:blue">댓글 삭제하기</span>

```html
# detail.html

<form action="{% url 'posts:comments_create' post.pk %}" method="post">
        {% csrf_token %}
        댓글 : <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>
    
    <ul>
        {% for comment in post.comment_set.all %}   <!-- 파이썬 쉘이랑 다름 괄호 없어! -->
        <li> {{ comment.content }} - <a href="{% url 'posts:comments_delete' post.pk comment.pk %}">삭제</a></li>
        {% endfor %}
    </ul>
```

![](C:\Users\student\Desktop\메일\이미지\제목 없음10.png)

```python
# urls.py

urlpatterns = [
    path('', views.index, name='list'),
    path('create/',views.create, name='create'),
    path('write/', views.new, name='new'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete') 📌
]
```

```python
# views.py

def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    
    # 삭제한 후, 댓글 썼던 글의 디테일 페이지 보여주기
    return redirect('posts:detail', post_id)
```



1. Project 이름

   * 소문자, 숫자 `_` 만 가능

     

2. APP 이름

   * 복수형 명사 권장

   * 숫자로 시작 금지

   * 소문자, 숫자 `_` 만

   * ex) `posts`, `students`

     

3. Model 이름

   * 대문자로 시작
   * **단수형** 명사 권장
   * 숫자 사용 금지
   * ex) `class Post`, `class Comment`

4. Model Column 이름
   * 소문자, 숫자 `_` 만 가능 (대문자 금지)

5. URL

* `path('posts/', include('posts.url')),`
  * 여기서 posts/ 에 들어가는 주소, **복수형** 명사



