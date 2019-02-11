##  오늘 作 `Form 폴더` : 

프로젝트명 articles, 앱명 form

클래스 만들 때, created_at 랑, updated_at  웬만하면  같이 적어주는 게 좋음

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# form/articles//urls.py

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('new/', views.create, name='create'),
]
```

```python
# views.py

from django.shortcuts import render

def create(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'form.html')
```

```html
<!--form.html-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>New Article</h1>
    
    <form method="post">
        {% csrf_token %}
        <input type="text" name="title" required/>     <!-- 속성값으로 required 추가해주면, 입력값이 없을 때, 입력하라고 뜸 -->
        <input type="text" name="content" required/>
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```

![](C:\Users\student\Desktop\메일\django\이이미지1.png)

* 입력받은 값을 저장할 수 있도록 `views.py` 수정

  ```python
  def create(request):
      if request.method == 'POST' :
          title = request.POST.get('title')
          content = request.POST.get('content')
          article = Article.objects.create(title=title, content=content)    # 이 줄은
          # article = Article(title=title, content=content)
          # article.save() 와 같음
          return redirect('articles:detail', article.pk)      # redirect 는 detail 로  → detail 새로 作
      else :
          return render(request, 'form.html')
    
  
  def  detail(request, article_id):
      article = Article.objects.get(pk=article_id)
      return render(request, 'detail.html', {'article': article})
  ```

* `urls.py`

  ```python
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
      path('new/', views.create, name='create'),
      path('<int:article_id>/', views.detail, name='detail'),
  ]
  ```

* `detail.html`

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <h1>Article Detail</h1>
      
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
  </body>
  </html>
  ```

  개발자 도구에서 변경가능

✅ `create.html` 에서 위에서 처럼 `input` 의 속성으로 `required` 를 주면,
        `F12` 개발자도구에서, 멋대로 수정 可 

   	 →→ Django 에서 자체적인 form 클래스를 가져와서 쓰자



## form 클래스

✅ `articles` 폴더 內 forms.py 만들기,    꼭 forms 여야 하는 건 아님. 그냥 관례적

```python
# forms.py     ( views.py 와 형태 유사)

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(label='제목')   # forms 의 CharField 는 max_length 가 필요 없다,    label=' ' 도 내가 원하는 것으로 적을 수 있음
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={
        'rows' : 5,
        'cols' : 50,
        'placeholder' : '내용을 입력하세요',
    }))                                                             # 이렇게 하면, html form 태그의 required 속성 저절로 (개발자도구에서 수정할 수 없다_)
                                                                     # forms 에는 textfield 없다 → widget 속성으로, textarea 로 변경
                                                                     # attrs 가 없으면 박스가 이상하게 생겨서, 예쁘게 바꿔주려고, attrs 어쩌고 저쩌고 썼음, 필수 X
```

```html
<!-- form.html 수정 -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>New Article</h1>
    
    <form method="post">
        {% csrf_token %}
                                                                                            <!-- <input type="text" name="title" required/> -->
                                                                                            <!-- <input type="text" name="content" required/> -->
        								    <!-- 지우고 밑에 form 넣어줌 -->
        {{ form }}  <!-- Articleform 의 인스턴스 -->
        
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```

* views.py 수정....뭔가 많았음 ㅜㅜㅜ

  ```python
  from django.shortcuts import render, redirect
  from .models import Article
  from .forms import ArticleForm  # form    import함
  
  # Create your views here.
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)    # POST 로 받아 들어온 데이터로,    form 의 title 과 content  를 미리 채워둔다
  
          if form.is_valid(): 			 # 미리 채워둔 data 가 유효하면(검증이 통과된 clean 한 데이터), True 반환 → if 문 可
              title = form.cleaned_data.get('title')  # clean 한 데이터에서 title 찾아서 title에 저장
              content = form.cleaned_data.get('content')
          
                                                                                                  # title = request.POST.get('title') : 얘네는 검증안된, 데이터였음
                                                                                                  # content = request.POST.get('content')
              
              article = Article.objects.create(title=title, content=content)                                                                          
              return redirect('articles:detail', article.pk)   # 🌹 입력을 잘 받았으면, 자기가 쓴 글 보여주는 상세페이지를 보여준다
              
      else:   # (POST 가 아니라 GET 방식이면, )
          form = ArticleForm()    # 사용자에게 빈 form 을 보여줘라
          
      return render(request, 'form.html', {'form':form})
          
          
  
  def detail(request, article_id):
      article = Article.objects.get(pk=article_id)
      return render(request, 'detail.html', {'article': article})
  ```

  

* models.py 와 연동된, form 만들기

  ```python
  # forms.py
  
  from django import forms
  from .models import Article   # Article 모델 import 해오기
  
  
  class ArticleModelForm(forms.ModelForm):    # 모델과 연관된 클래스
      class Meta:     # Meta 는 꼭 Meta 여야 함 ( ArticleModelForm 클래스(자기 품고 있는 클래스)의 정보가 담겨있는 클래스)
          model = Article  # Article 이라는 모델을 건들거임
          fields = ['title', 'content']    # article 의 필드들 써 줌, 저절로 해당 모델의  input 칸 生 인가?
  ```

  ```python
  # views.py 도 수정
  
  from django.shortcuts import render, redirect
  from .models import Article
  from .forms import ArticleModelForm  # import 하고
  
  # Create your views here.
  def create(request):
      if request.method == 'POST':
          form = ArticleModelForm(request.POST)   # AarticleModelForm 의 인스턴스
  
          if form.is_valid(): 
              title = form.cleaned_data.get('title')    ▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶ 부터
              content = form.cleaned_data.get('content')
              article = Article.objects.create(title=title, content=content)   ◀◀◀◀◀◀◀◀ 까지, 아래에서 축약
              return redirect('articles:detail', article.pk)
              
      else:
          form = ArticleModelForm()
          
      return render(request, 'form.html', {'form':form})
  
  
  
  # 한단계 더 수정  ( 짧아짐 👏👏👏👏)
  def create(request):
      if request.method == 'POST':
          form = ArticleModelForm(request.POST)
  
          if form.is_valid():
              article = form.save()   🆗 얘로
              return redirect('articles:detail', article.pk)
              
      else:
          form = ArticleModelForm()    # forms 의 ArticleForm 을 받아옴
          
      return render(request, 'form.html', {'form':form})
  ```

  

### Update

```python
# urls.py
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('new/', views.create, name='create'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/edit/', views.update, name='update'),
]
```

```python
# views.py
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article) # 이렇게 적으면, 수정페이지에, 원래 적혀있는 글 보여줌

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
            
    else:
        form = ArticleModelForm(instance=article)  # 여기서 article 은 def 밑에 쓴 article
        
    return render(request, 'form.html', {'form':form})
```



### form.html 수정

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>New Article</h1>
    
    {{ form.non_field_errors }}
    
    <form method="post">
        {% csrf_token %}
        <!-- {{ form }}  <!-- 데이터들이 하나로 뭉처져있어서 커스터마이징 하기가 힘들다 >> 쪼개자 -->
        
        <!-- 1. title -->
        <div>
            {{ form.title.errors }} <!-- error message (ul, li tag) -->
            {{ form.title.label_tag }} <!-- label tag -->
            {{ form.title }}  <!-- input tag -->
        </div>
        
        <!-- 2. content -->
        <div>
            {{ form.content.errors }}
            {{ form.title.label_tag }}
            {{ form.content }}
        </div>
        
        
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```





숙제

{{ form.as_p }} ? 

{{ form.as_table }}