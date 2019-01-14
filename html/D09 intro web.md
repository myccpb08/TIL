www : world wide web

웹 :  요청(client가 브라우저에서 보냄) 과 응답(Server)

서버컴퓨터 : 요청된 걸 처리하는 컴퓨터 

요청의 종류

- <span style="color:blue"> 줘라(get) </span> --- 요청받은거 서버가 client 에게 줌

- <span style="color:blue"> 보내다(post) </span>  --- 서버가 저장을 하거나, 다른 곳으로 보내거나





  우리는 서버컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.


#### static web : 정말 단순한 웹서비스

* 모든 人에게 동일한 화면 show

크롬 주소창에서

`/dir1/dir2/../WantThis.file`  ▶ 파일이 브라우저에서 열림 (원하는 파일 크롬으로 드래그해도 ok)

`남의 컴퓨터 주소/dir/dir2/../WantThis.file`  ▶ 남 컴퓨터가 허락하면, 남 컴퓨터 파일도 보여줌

ex) `google.com/dir/dir2/../WantThis.file` 

​	( 숫자로 된 남의 컴퓨터 주소 = 경북대학교의 도로명 주소 

​	  google.com = 경북대학교)  ▶ 도로명 주소만 써놓으면 다른 사람들이 알기 힘드니까, 건물명 써주는 것



#### Dynamic Web ( Web Application program ) : web app

- 요청하는 사람마다 다른 화면을 보여줌

- 주소 예시`http(s)://hphk/lectures/1`

- ##### <span style="color:blue"> URL </span>(Uniform Resouce Locator) : 네트워크 상에서 자원이 어디 있는지 알려주는 고유 규약

  - 웹 사이트 주소 뿐만 아니라 컴퓨터 네트워크 상의 자원을 모두 나타낼 수 있다



### <span style="color:red"> HTML (Hyper Text Markup Language) </span>

* hyper text 는 순서대로 읽지 않아도 되는 text = 비선형적 text

* markup : bold, 문단, 색, 글씨 크기 등등 tag 를 통해 역할 나눠서 text 구분 하는 것

  ```html
  <!DOCTYPE html>     # doctype 선언부 : 사용하는 문서의 종류를 선언하는 부분. 보통 html 을 사용한다.
  <html lang="en">    # 여기부터 끝까지 : html 요소로 head + body 구성
  					en : 이 웹페이지가 영어로 작성되어 있음을 알려줌
  <head> 			   # head : 문서제목, 문자코드(인코딩) 와 같이 해당 문서 정보를 담고 有. 브라우저에 show (x)
      					   css 선언 혹은 외부 로딩 파일 지정 들을 작성
      					   크롬탭에 표시되는 거
      <meta charset="UTF-8">  # meta tag 는 카톡공유 누르면 미리보기 되는 부분에 해당
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      
  </body>
  </html>
  ```

* 주석은 `ctrl+/` 또는 `<!-- 내용 -->`

* #### body 內 tag 와 dom tree

  * html 의 element 는 태그와 내용(contents) 로 구성되어 있다.

    `    <h1>= 시작태그` 웹문서 `</h1>= 종료태그`  : 태그는 대소문자를 구별하지 않으나, <span style="color:red">소문자로 작성</span>해야 함. 


  ​												          요소間 중첩 可 = tag 內 다른 tag 삽입 가능

  ​	+) 닫는 태그가 없는 것도 有 : 이미지태그 = `<img src="url"/>` 

  * 태그에는 속성이 지정될 수 있다 : id, class, style 속성은태그와 상관없이 모두 사용 可

    `<a herf="https://"google.com"/>  : `  a 태그는 button 이니까 google 로 이동하는 버튼 生 / 쌍따옴표 권장

    * herf = 속성명 / google.com = 속성값



 * Dom 트리 : 부모와 자식, 형제관계 표시  : 그냥 html 죽 쓴 거 모양인듯...
 * <span style="color:blue">시맨틱 태그 </span> : 컨텐츠의 <span style="color:blue">의미를 설명</span>하는 태그로서, html5 에 새롭게 추가된 시맨틱 태그가 有
    * header : 헤더 ( 문서 전체나 섹션의 헤더)
    * nav: 내비게이션 ( 상단의 로그인 버튼같은...)
    * aside : 사이드에 위치한 공간으로, 메인 콘텐츠와 관련성이 적은 콘텐츠에 사용( 날씨, 인기급상승 검색어 등등)
    * section : 문서의 일반적인 구분으로 컨텐츠의 그룹을 표현하며, 일반적으로 h1~h6
    * article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역(포럼/신문 등의 글 또는 기사)
    * footer : 푸터(문서 전체나 섹션의 푸터)



* 태그 실습 ( b   strong   i    em	    mark	    del      ins     sub     sup    p    br    pre     hr     or    ul    li )

  ```html
  <!DOCTYPE html>     
  <!-- doctype 선언부 : 사용하는 문서의 종류를 선언하는 부분. 보통 html 을 사용한다. -->
  <html lang="ko">
  <!-- head 는 브라우저에 나타나지 않는다 -->
  <!-- 미리보기에 해당하는 것 : meta tag -->
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Hi,HTML!</title>
      <!-- style 내부는 css 코드로 -->
      <style>h1 { color: aquamarine; }</style>
  </head>
  <!-- body 는 실제 user 가 브라우저에서 보게 되는 내용 -->
  <body>
     <h1>Hi, h1!</h1>
     <h2>Hi, h2!</h2>
     <h3>Hi, h3!</h3>
     <h4>Hi, h4!</h4>
     <h5>Hi, h5!</h5>
     <h6>Hi, h6!</h6>
  <!-- <b> = Bold 이고, <strong> 도 굵은 글씨인데, semantic 태그임. strong 사용 권장 -->
      <b>This is b.(non semantic)</b>
      <STRONG>This is strong.(semantic)</STRONG>
  
      <!-- italic 과 em(semantic 이고, empasize 약자) -->
      <i>This is italic</i>
      <em>This is em.(semantic)</em>
  
      <!-- 중첩으로 쓰기 -->
      <b><em>굵고 기울이기</em></b>
  
      <!--highlighted 형광펜 -->
      <h2>This is <mark>Mark</mark>.</h2>
  
      <!-- del 취소선 / ins 밑줄 -->
      <h2>This is <del>del</del>.</h2>
      <h2>This is <ins>ins</ins>.</h2>
  
      <!-- sub 아래첨자 / sup 윗첨자 -->
      <h2>This is <sub>sub</sub>.</h2>
      <h2>This is <sup>sup</sup>.</h2>
  
      <!-- p = paragraph, br=띄어쓰기 -->
      <p>This is p tag. This is p tag. This is p tag. <br>
         This is p tag. This is p tag. </p>
  
      <!-- pre 쓰면 br 안 써도 입력하는 그대로 출력됨. 들여쓰기까지 그대로 -->
      <pre>
          from flask import flask
          app = Flask(__name__)
  
          @app.route('/')
      </pre>
  
      <!-- hr : 수평선 하나 그어줌. 닫는 태그 無 -->
      <hr>
  
      <!-- q : 인용 quotation 따옴표 붙여줌   blockquote -->
      <p>
          Junwoo said, <q>Hello world!</q>
      </p>
      <blockquote>
          Hello world!
      </blockquote>
  
  
      <!-- ol = ordered list 이나 ul = unordered list 을 쓰고 li = list -->
      <ol>
          <li>first</li>
          <li>second</li>
          <li>third</li>
      </ol>
      <ul>
          <li>first</li>
          <li>second</li>
          <li>third</li>
      </ul>
  </body>
  </html>
  ```



# 

##### 웹 developer 설치 (크롬웹스토어) >> information >> view document outline

### HTTP(s) (Hyper Text Transfer Protocol (secure))

