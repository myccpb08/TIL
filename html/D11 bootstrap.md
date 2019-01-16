> 트위터 회사에서 만든 css 프레임워크

> CDN = Content Delivery(Distribution) Network : 

콘텐츠(css,js,image,text 등) 을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템



> https://getbootstrap.com/docs/4.2/content/reboot/ : 브라우저가 기본으로 가지고 있는 css 제거하기 위한 bootstrap 의 reboot 기능덕분에 모든 브라우저에서 같은 모양으로 화면이 보여지게됨



https://getbootstrap.com/docs/4.2/getting-started/introduction/ 에서 css 랑 js 링크 추가해 줘야 함



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- link bootstrap -->
>>>> <link rel="stylesheet"   href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
</head>
<body>
    <h1>Get Bootstrap</h1>
    <a href="https://getbootstrap.com" target="_blank">Go to Bttostrap</a>






>>>><script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>
</html>
```







1-1. spacing (클래스명으로 아래 문자들을 넣으면 됨)

> .m-0  = margin : 0!  뜻함
>
> .mg-0 = margin-right
>
> .py-0 = padding-top 과 padding-bottom 이 0 (padding y축)   (패딩은 클릭되고, 마진은 클릭 ㄴㄴ)
>
> .mt-1 = margin-top: 0.25rem (브라우저 기본 rem은 16px)      mt-5까지 있고 (0.25→0.5 →1→ 1.5→ 3 순서)
>
> (margin 은 음수값이 가능해서 -5 까지 가능  ex) my-n5  (negative5)
>
> .mx-auto
>
> ```html
> <h1 class="py-3 bg-primary">Get Bootstrap</h1>
> <a class="pl-3 ml-3" href="https://getbootstrap.com" target="_blank">Go to Bttostrap</a>
> ```
>
>



1-2. color

> .bg-색깔명   ex) 클래스명에 .bg-primary  백그라운드 색 primary 로 바뀜
>
> .text-색깔명
>
> ```html
> <h2 class="text-success">Nice to meet you</h2>
> ```
>
>



1-3. border

```html
<a class="pl-3 ml-3 border" href="https://getbootstrap.com" target="_blank">Go to Bttostrap</a>
```

> > 보더에 테두리 색 넣고 싶으면 .border border-success
> >
> > ```html
> >  <a class="pl-3 ml-3 border border-success" href="https://getbootstrap.com" target="_blank">Go to Bttostrap</a>
> > ```

> > 보더 테두리 둥글게 하고 싶으면 rounded(각 모서리 부채꼴)   or   rounded-cicle(타원)   or  rounded-pill (양끝 반원)
> >
> > ```html
> > <a class="pl-3 ml-3 border border-success rounded" href="https://getbootstrap.com" target="_blank">Go to Bttostrap</a>         ↑ 여기 바꾸면 됨
> > ```



1-4. Display

* d-none : 화면에서 그냥 사라짐

  ```html
  <h2 class="d none text-success alert-warning">Nice to meet you</h2>
  ```

* d-sm-none : 화면이 커지면 사라짐  (sm 자리를 md lg xl 로 바꿀 수 ㅇㅇ) getbootstrap.com/docs/4.2/layout/grid

  ```html
  <h2 class="d none text-success alert-warning">Nice to meet you</h2>
  ```

* d-inline 

* d-inline-block 

* d-block



1-5. Position

* position-fixed fixed-bottom(아래에 붙이기 , top 으로 바구기 가능)



1-6 Text

* font-weight-bold

* text-center (가운데 정렬)

* font-italic

  ```html
  <p class="text-center">Lorem</p>
  <p class="font-weight-bold">Lorem</p>
  <p class="font-italic">Lorem </p>
  ```





컴포넌트는 공식문서로 확인 (앞으로도 많이 활용할 것이고, 직접 들어가서 코드를 찾아야하기 때문!)



bootstrapcreative.com

아래 쪽에

bootstrap4 cheat sheat







```html
 <div class="container">.......내용.. </div>   # 양쪽에 여백을 줘서 콘텐츠에 시선이 가도록 
"container-fluid" 쓰면 여백 작은 거    # 컨테이너도 반응형
```





## 2. grid system (12줄 구성)

빈칸만들기 offset

```html
<div class="col-4 border border-primary">
                One of three columns
</div>
<!-- offset -->
<div class="offset-4 col-4 border border-primary">
      One of three columns
</div>
<div class="col-4 border border-primary">
     One of three columns
</div>
```



자동완성으로 class 2개 동시에 만들기

```html
div.container>div.row
```

```html
<div class="col-4 col-sm-3 border border-success">1</div> 화면이 특정이상 커지면 1칸이 3열 차지로 바뀜
```

```html
<div class="col-4 col-sm-3 col-md-2 border border-success">3</div> md일땐 2칸으로
```



## 3. bootstrap 의 component  (https://getbootstrap.com/docs/4.2/components/alerts/)

> button
>
> ```html
> <button type="button" class="btn btn-primary">Primary</button>   btn-primary : 배경색
> 															btn-outline-primary: 하면 배경색x
> ```
>
> ```html
> <button type="button" class="btn btn-primary btn-lg btn-block">Primary</button>
> lg = large
> b> block = 한 줄 다 차지하는 크기의 버튼
> ```
>
> ```html
> <!-- button group -->
> <div class="btn-group btn-group-lg btn-group-vertical" role="group" aria-label="Basic example"></div> vertical 은 세로로 버튼 배열
> ```
>
>

