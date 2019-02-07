![](C:\Users\student\Desktop\메일\이미지\제목 없음13.png)

d/rwx/r-x/r-x    :  소유자/그룹/이도저도아닌

r: read 읽기

w: write 쓰기

x: execute 실행

/rwx/ 소유자는 읽기 쓰기 실행 전부 가능

/r-x/ 소유자는 아닌데 그룹원? 은 읽고 실행만

/r-x : 소유자도 아니고 그룹원도 아닌 사람이 할 수 있는?

x 붙어 있으면, 바로 실행가능한 파일

<hr>

오늘 내용 : 템플릿 정리
		    html 만들 때마다, 중복된 부분을 반복 입력하지 않고, 변경사항만 저장할 수 있도록
		    (항상 떠있는 네비바처럼, 항상 표시되는 것들은 묶어서 정리해두고 코드 중복해서 작성하지 않도록 하기)

`REST 인터페이스 위키에 검색해보기`

## 오늘의 作 : crud-rest  內 crud 內 tempaltes  內 base.html

1. ting.py 에 57번째 줄, templates 리스트 內 `DIRS` 에  만든 폴더 경로를 추가해준다

```python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')] } ]
```

```html
# base.html  만들어서 作

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1> 여기는 base.html! </h1>   <!-- 얘는 항상 보여주고 -->
    {% block container %}         <!-- 다른 html 파일에서, 묶음 처리한 내용 실행 , container 라는 이름은 마음대로 해도 됨-->
    {% endblock %}
</body>
</html>
```



2. 원래 있던 templates 폴더 내 index.html 수정하기

```html
<!-- 원래 index.html -->

{% load static %}
<!DOCTYPE html>    💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡 부터
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="{% static 'public.css' %}" type="text/css"/>
</head>
<body>   💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡  까지 삭제
    
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

```html
<!-- 변경 후 index.html-->

{% extends 'base.html' %}
{% load static %}
{% block container %}

    <img src="{% static '2.png' %}"/></img>
    <h1>Post Index</h1>
    <a href="{% url 'posts:new' %}">글쓰기</a>
    <ul>
    {% for post in posts %}
        <li><a href="{% url 'posts:detail' post.pk %}">{{ post.title }}</a></li>
    {% endfor %}
    </ul>

{% endblock %}
```

네비게이션 바가 항상 위에 있는 것 처럼 

이렇게 코드를 바꾸면,

base.html = 헤드로서, 어떤 페이지로 이동하든, 항상 위에 base.html 이 보인다

<hr>

# REST의 구성

* 자원(Resource) - URI
* 행위(Verb) - HTTP Method
* 표현(Representations)

### REST API 디자인 가이드

1. URI는 정보의 자원을 표현해야 한다.
2. 자원에 대한 행위는 HTTP Method(`GET, POST, PUT, DELETE`) 
   로 표현한다.



	### 예시 ( 끝날 때, 슬래시를 쓰지 않는게 보통이나, 장고에서는 써야 함)

```
GET /movies/show/1  (x)      : 1페이지를 보여달라는 동사 show 를 쓰지 않고
GET /movies/1           (o)      : 바로 1을 쓴다
```

```
GET /movies/create  (x)     : GET Method는 자원 생성에 부적합
POST /movies             (o)
```

```
GET /movies/2/update    (x)  :  GET 부적합
PUT /movies/2                 (o)  : 수정할 때는 put을 써라 (하지만 장고에서는 put 을 지원하지 않는다?)
```

``` 
GET /movies/2/edit      : 수정 페이지를 보여줌
POST /movies/2/edit     : 수정 작업을 行
```



```python
# urls.py 수정하자  rest 에 맞추어서
# 원래는

urlpatterns = [
    path('', views.index, name='list'),
    path('create/',views.create, name='create'),
    path('write/', views.new, name='new'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'), ]
```

```python
urlpatterns = [
    path('', views.index, name='list'),    # GET
    
    # path('create/',views.create, name='create'),   new 랑 합침
    path('write/', views.new, name='new'), #  GET(new) # POST(create)     : 수정  1️⃣
    
    path('<int:post_id>/', views.detail, name='detail'),  # GET
    
    path('<int:post_id>/delete/', views.delete, name='delete'), #GET(confirm), POST(delete)    : 수정  2️⃣
    
    path('<int:post_id>/edit/', views.edit, name='edit'), # GET(edit), POST(update)      : 수정 3️⃣
    #path('<int:post_id>/update/', views.update, name='update')  edit 으로 합침
 
]
```



### <span style="color:blue">수정 1 :</span> def new(request)  &  def create(reqeust) 合作 

```python
# views.py 수정   

def new(request):
    if request.method == 'POST':
        # create
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        post = Post(title=title, content=content, image=image)
        post.save()
        return redirect('posts:detail', post.pk)
        
    else:
        # new
        return render(request,'new.html')
```

```html
# new.html 수정 : form 의 액션 지워주기

{% extends 'base.html'%}
{%block container %}

    <form method="post" enctype="multipart/form-data">      : 액션이 없어지면, 자기 자신으로 다시 요청을 보낸다?                            
        {% csrf_token %} 
        <input type="text" name="title"/>
        <input type="text" name="content"/>
        <input type="file" name="image" accept="image/*"/>
        <input type="submit" value="제출"/>
    </form>
{% endblock %}


/posts/wrtie 로 get 요청이 가서 장고가 응답하여 html 파일을 보여줘서 글 쓸 수 있는 페이지가 보여짐
액션이 없으면, 자기 자신의 주소로 다시 post 요청을 보낸다  (/posts/write)
views.py 에서 if문の ==post 가 실행된다
```



<h3><span style="color:blue">수정 2 :</span>def delete </h3>

```python
def delete(request, post_id):
    if request.method == 'POST' :# 삭제하는 코드
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('posts:list')
    
    else:
        return render(request, 'delete.html')
```

```html
<!-- delete.html 만들기 -->

{% extends 'base.html'%}
{%block container %}
    <h1>정말 삭제하시겠습니까?</h1>
    <form method="post">
        {% csrf_token %}
        <input type="submit" value="삭제"/>
    </form>
{% endblock %}
```



## <span style="color:blue">수정 3 :</span> def edit(request)  &  def update(reqeust) 合作 

```python
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    if request.method == 'POST':
        #update
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:detail', post.pk)
    
    else:
        #edit
        return render(request, 'edit.html', {'post': post})
       
# 하고 edit.html 에서 action 지우기
```



