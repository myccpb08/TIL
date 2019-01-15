## CSS (html로 뼈대 잡고, css로 꾸미기)

```html
<!-- 1. Inline stye(인라인 스타일) : css 문자이긴 한데, 인라인 스타일에선 선택자 필요 없음 -->
    <ul style="list-style-type:circle;">
        <li>HTML</li>
        <li>CSS</li>
    </ul>
```



#### 기본 css 구조

```html
<!-- style 내부는 css 코드로 -->
<!-- 2. Embedding style(style tag 사용하기 : 우리가 배우면서 가장 빈도 多) -->
<style>
        /* css */
        /* h1 : 선택자 */
        /* color : 속성(property */
        /* aquamarine : 값(value) */
        /*  {   }   : 선언 블록 */
        /* color: aquamarine;  : 선언문 */
        /* {.......} : 선언블록 + 선언문 = 규칙 */
        /* 규칙 묶음 : 스타일 시트 */
        h1 { 
            color: aquamarine; 
        }
    </style>
```



###  외부 css 파일 가져와서 스타일로

```html
<!-- 3. Link style (css 파일 link) : 실제로 가장 빈도 多 -->
<link rel="stylesheet" href="style.css">
```



### 색 바꾸는 방법들 (01.basic selector 파일)

```html
    <style>
        /* 전체 선택자는 '*' 로 시작 */
        * {
            color: red; 
        }
        
        /* 태그 선택자는 해당 태그로 시작하는 것 */
        h1 {
            color: rosybrown;
        }
        
        /* 클래스 선택자는 .클래스명으로 시작 */
        .blue {
            color: blue;
        }
        .pink {
            color: hotpink;
        }
        
        /* 아이디 선택자는 #클래스명으로 시작 */
        #green {
            color: green;
        }
    
    </style>

</head>

<body>
    <p>red, 전체 선택자</p>
    
    <h1>rosybrown, 태그 선택자</h1>
    
    <h2 class="blue">blue, .클래스 선택자</h2>
    
    <h3 id="green">green, #아이디 선택자</h3>
    
    <!-- ★★★ ID > CLASS > TAG > 전체 -->
    <h1 class="blue">클래스선택자(승) vs 태그선택자</h1>
    <h1 id="green">아이디선택자(승) vs 클래스선택자</h1>
    <h1 id="green" class="blue">아이디선택자(승) vs 클래스선택자 vs 태그선택자</h1>

	<!-- 개별적으로 색 넣기 : span -->
    <p>나는 <span class="blue">파랑색</span>이고 싶고, 여기는 <span class="pink">핑크색</span>이고 싶을 때</p>


</body>
</html>
```



### color 선택 방법들(02_unit.html 파일)

```html
<style>
    /* 색 넣는 방법 */
        /* 1. color name */
        h1 {color:red;}

        /* 2. color code */
        h2 {color: #0000ff}

        /* 3. rgb(빨,초,파) */
        h3 {color: rgb(0,250,0)}

        /* 4. rgba(빨,초,파,투명도) 알파값은 0~1*/
        p {color: rgba(255,0,0,0.3)}

    
    </style>
```



```html
<style>
/* 단위 길이(font-size) */
    html { font-size: 10px;} : 폰트사이즈는 상속되는 거라, div 의 폰트사이즈만 10px 가 아니라 문서전체 사이즈 감소
    
    
    
    
</style>

<body>
    <div>저는 10px입니다</div>
</body>
```





### ㅂ박스만들기

```html
<style>
        /* 박스에 가로 & 세로 & 여백 지정 */
        .box {width:100px ; height: 100px; padding: 25px; margin:25px ;} # 상하좌우 모두 여백
    
    	상하좌우 따로 주려면
    
    	.box {width:100px ; height: 100px; 
            	padding-top: 25px; padding-right: 25px ; padding-bottom: 25px;padding-left: 25px;
           		margin:25px ;}   # margine 도 따로 가능
```





lorem ipsum