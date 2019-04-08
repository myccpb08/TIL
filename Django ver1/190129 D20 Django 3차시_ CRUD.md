html 에서 주소 쓸 때는 항상 슬래시로 시작하고 슬래시로 끝난다



* <span style="color:red">제목을 링크로</span> 만들기 (게시글의 제목을 누르면, 세부 내용 페이지로 넘어갈 수 있도록)

  ```html
  # index.html
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
      <ul>
      {% for post in posts %}  <!-- 포스트 반복문 내에서 각각의 포스트의 pk로 변수-->
          <li><a href="/posts/{{post.pk}}">{{ post.title }}</a></li>
      {% endfor %}
      </ul>
  </body>
  </html>
  ```

  ![](C:\Users\student\Desktop\메일\이미지\제목 없음5.png)



* #<span id="상세">제목 누르면, 내용 보여주는 <span style="color:red">상세 페이지로 </span>이동하기</span>

  ```python
  # urls.py
  urlpatterns = [
      path('', views.index),
      path('<int:post_id>/', views.detail),     📌 여기 : url 주소가   posts/숫자  이렇게 됨
  ]
  
  # <int:post_id> 에 변수名 post_id 는 detail(request,post_id 변수名) 과 同 
  
  # views.py
  def detail(request, post_id):
      post = Post.objects.get(pk=post_id)    # pk = post_id 인 걸 가져와서 post 로 저장
      return render(request, 'detail.html', {'post':post})  # detail.html 에서 post 가 필요하니까 템플릿변수로 傳
  ```

  ![](C:\Users\student\Desktop\메일\이미지\제목 없음6.png)

  ```html
  # detail.html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <h1>Post Detail</h1>
      <h2>Title : {{post.title}} </h2>    <!-- 위에서 변수로 넘겨받은 post 의 title --->
      <p>Content : {{post.content}} </p>   <!-- 위에서 변수로 넘겨받은 post 의 content --->
      <a href="/posts/">List</a>  <!-- 목록으로 돌아가는 페이지 -->
  </body>
  </html>
  ```

  

  * /posts/new 에서 title 과 content 를 입력하면  <span style="color:red">내가 쓴 글 보여주는 페이지로</span> 이동

    * get method 대신 <span style="color:blue"><b>post method 와  redirect</b></span> 보내기

      ```html
      # new.html 에서 작성
      
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      <body>   		         # url 을 create 로 보내니까, views.py 內 def create() 가 내가 쓴 글 페이지를 보여주도록 수정해야한다
          <form action="/posts/create/" method="post">  <!-- get 요청은 : ~~한 html 페이지를 보여줘 & 주소창에 내 요청이 다 보여짐-- 로그인 할 때 쓰면 안 됨>
                                                       <!-- post 요청은 : 이거 실어 보낼 테니까 저장하고 처리해 줘 & 주소창에 내 요청 안 보임-->
              {% csrf_token %}  <!--post 요청 보낼 때 꼭 필요한 거. 보안상の 목적 -->
              
              <input type="text" name="title"/>
              <input type="text" name="content"/>
              <input type="submit" value="제출"/>
          </form>    
      </body>
      </html>
      ```

      ```python
      # views.py
      # 📌📌📌📌📌📌 redirect 임포트 해줘야함
      from django.shortcuts import render, redirect
      
      def create(request):
          title = request.POST.get('title')    # POST method 썼으니까, 이제 중간자를 POST 로 바꿈
          content = request.POST.get('content')
          
          # DB INSERT
          post = Post(title=title, content=content)   # new 에서 입력받은 거 받아서 post 에 저장
          post.save()
          
          
          return redirect(f'/posts/{post.pk}')   # post 요청은 html 모여주는게 아니라 새로운 페이지로 결과를 돌려버림. 그러므로 주소 필요
      ```

      URLS.PY 파일을 보면 :

      ```PYTHON
      urlpatterns = [
          path('<int:post_id>/', views.detail),
      ] 
      # 이라서 결국 위의 CREATE 함수를 실행하면 
      ulrs 에서 detail 함수를 요청하게 된다
      ```

    

      * 추가 : 외부 페이지로 redirect 시키기 (....../posts/naver/검색어) 하면

        ```python
        # urls,py
        urlpatterns = [
            path('naver/<str:q>/', views.naver), ]        : 검색어가 q 로 넘어오고
        
        # views.py
        def naver(request, q):  # 외부 페이지로 redirect 시키기         : 그 q 가 함수의 q 로 넘어가서
            return redirect(f'https://search.naver.com/search.naver?query={q}')       : query 로 넘어가서 네이버 페이지 show
        ```



## 선택한 <span style="color:red">게시글 삭제</span>하고 리스트 보여주기

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/delete/', views.delete),   
]

# views.py

def delete(request, post_id):
    # 삭제하는 코드
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/posts/')
```

```html
# detail.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Post Detail</h1>
    <h2>Title : {{post.title}} </h2>
    <p>Content : {{post.content}} </p>
    <a href="/posts/">List</a>  <!-- 목록으로 돌아가는 페이지 -->
    <a href="/posts/{{post.pk}}/delete/">Delete</a>         <!--- DELETE 버튼 생성 ------>
</body>
</html>
```

..../posts/ 에서 게시글 하나 선택하기 >> delete 누르기 >> 삭제 된 리스트로 돌아옴 

![](C:\Users\student\Desktop\메일\이미지\제목 없음7.png)



![](C:\Users\student\Desktop\메일\이미지\제목 없음8.png)

![](C:\Users\student\Desktop\메일\이미지\제목 없음9.png)



# 게시글 수정

```html
# detail.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Post Detail</h1>
    <h2>Title : {{post.title}} </h2>
    <p>Content : {{post.content}} </p>
    <a href="/posts/">List</a>  <!-- 목록으로 돌아가는 버튼 -->
    <a href="/posts/{{post.pk}}/edit/">Edit</a>   <!-- 누르면 수정해주는 버튼 -->
    <a href="/posts/{{post.pk}}/delete/">Delete</a> <!-- 누르면 삭제해주는 버튼 -->
</body>
</html>

Edit 버튼 누르면 → /posts/{{post.pk}}/edit    url 로 연결
```

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:post_id>/', views.detail),
    path('<int:post_id>/edit/', views.edit),              # urls.py  에서  path 찾아서, 이제  views.py 에서 edit 함수 行
    path('<int:post_id>/update/', views.update),   
]

# views.py

def edit(request, post_id):
    post = Post.objects.get(pk=post_id)     # pk 로 post 가져옴
    return render(request, 'edit.html', {'post': post})   # edit.html 연결
```

```html
# edit.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Post Edit</h1>
    <form action="/posts/{{post.pk}}/update/" method="post">        # 변경한 입력 결과를 /posts/{{post.pk}}/update/  로 보낸다
        {% csrf_token %}
        <input type="text" name="title" value="{{post.title}}"/>
        <input type="text" name="content" value="{{post.content}}"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```

```python
# urls.py 에서  update 링크 찾는다

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:post_id>/', views.detail),
    path('<int:post_id>/edit/', views.edit),              
    path('<int:post_id>/update/', views.update),   # urls.py  에서  path 찾아서, 이제  views.py 에서 update 함수 行
]
```

```python
def update(request, post_id):
    # 수정하는 코드
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect(f'/posts/{post_id}/')
```



