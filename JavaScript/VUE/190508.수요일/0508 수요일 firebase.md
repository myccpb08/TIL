###  새로고침해도 유지되는 ToDo 만들기 (nosql, firebase)



어제 todo 복사해서 사용 (todo_firebase.html)  `<https://firebase.google.com/>`

M(firebase.google.com)

V(html 파일)



> >  firebase 사이트, 로그인하고, 콘솔로 이동 >> 프로젝트추가
> >
> > 프로젝트ID = 후에 domain 됨  ( `vue-todo-0821`)
> >
> > 프로젝트 실행
> >
> > 개발 tab - Database - 아래 쪽, `realtime database` - 데이터베이스 만들기 - 테스트 모드로 시작 - 사용설정
> >
> > `https://vue-todo-0821.firebaseio.com/`



firebase 를 html 파일에서 쓰기 위해서는 `script` 를 `head` 에 추가해야 한다

`<https://firebase.google.com/docs/web/setup/?hl=ko>` 들어가서 복사

```html
<script src="https://www.gstatic.com/firebasejs/5.9.1/firebase.js"></script>

<!-- VueFire -->
<script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
<script>
  // Initialize Firebase
  // TODO: Replace with your project's customized code snippet
  var config = {
        apiKey: "AIzaSyD0ChKVrxAo5miPq-SjMZbozsC1wi0hylU",
        authDomain: "vue-todo-0821.firebaseapp.com",
        databaseURL: "https://vue-todo-0821.firebaseio.com",
        projectId: "vue-todo-0821",
    };
  firebase.initializeApp(config);
</script>
```



#### 1. todo 리스트 유지시키기 (체크박스는 유지 x)

1. 원래 있던 todos 주석처리

   ```html
   // todos: [
                   //     {
                   //         id : 1,
                   //         content : '점심 메뉴 고민하기',
                   //         completed: true,
                   //     },
                   //     {   
                   //         id : 2,
                   //         content:  '사다리 타기',
                   //         completed: false,
                   //     },
                   //     {
                   //         id : 3,
                   //         content :  '약속의 2시. 낮잠자기',
                   //         completed: false,
                   //     },
                   //     {
                   //         id : 4,
                   //         content: '야자하기',
                   //         completed : false,
                   //     }   
                   // ]
   ```

   

2. `<script>` 에 `const database` 추가

   ```html
   <script>
           const database = firebase.database() // firebase db 기능 쓸 수 있게 함
   </script>
   ```

   

3. methods 와 같은 레벨에 firebase 만들기

   ```html
   <script>
   firebase: {
               todos : database.ref('messages'),  
   // database : firebase db 전체,  차곡차곡 데이터 쌓으려면 database.ref('임의변수명')
           },
   </script>
   ```



4. db 변경해서 addTodo 의 todos 에 push 하는 거 사용x → 수정

   ```html
   <script>
       addTodo : function() {
           this.$firebaseRefs.todos.push({   ⏮⏮⏮⏮⏮⏮
               id: Date.now(),
               content : this.newTodo,
               completed : false,   // 값을 넣고
           })
           this.newTodo = ''  // 넣은 후에는 input 창 깨끗하게
       },
   </script>
   ```



5. 이렇게하고 페이지 열어보면, 이제 데이터를 새로 넣고, 새로고침 해도 sleep 계속 有

   ![](C:\Users\student\Desktop\KYR\JavaScript\이미지\03.png)





#### 2. 체크박스도 유지시키기

1. methods 에 `updateTodo` 만들기

   ```html
   <script>
       methods : {
           /*..... 중략 .....*/
           
           updateTodo : function(todo){ // 우리가 작성한 todo
               /* todo = {'content:'hi', completed:true}
                ...todo =  'content':'hi', completed:true
                spread operator : 복사본 만들기 위하여, 원본을 건들지 않기 위하여 */
               const newTodo = { ...todo }
               delete newTodo['.key']  
   /* newTodo 에 있는 키(firebase 에서 각각의 object 를 구분하기 위해 사용하는 키) 를 지움  
     ∵ 굳이 db 에 업데이트 할 필요 없어서 지움  */
               
               this.$firebaseRefs.todos.child(todo['.key']).set(newTodo)
               /* set : 그냥 update 로 생각하면 됨. completed 만 f >t 로 바뀌더라도, completed 만 바꾸는 게 아니라, content 랑 completed 이 세트를 통째로 갈아 끼워야함 */ 
           },
       },
   </script>
   ```

   

2. 체크박스를 만질 때마다, 값을 바꿀 거니까, 체크박스 수정 

   ` <input type="checkbox" v-model="todo.completed" v-on:change="updateTodo(todo)"> `

   

#### 3. 완료된 거 일괄 삭제버튼 수정

##### `clearCompleted` 수정 :  완료한 거 삭제하기

```html
<!-- 전 -->
<script>
     //  핵심은 '.filter' 의 사용! ( 완료된 일을 지우고 싶으면, 완료되지 않은 일을 남기는 것으로 접근하기)
            clearCompleted: function(){
                const notCompletedTodos = this.todos.filter((todo)=>{
                    return !todo.completed
                })  // notCompletedTodos = [{...}, {...}] 완료되지 않은 애들만 담긴 새로운 배열 만들어짐 
                 this.todos = notCompletedTodos  // 새로 만들어진 애들로 todos 를 교체 
            },
</script>
```

```html
<!-- 후 -->
<script>
    clearCompleted: function(){
        const CompletedTodos = this.todos.filter((todo)=>{ ⏮⏮
            return todo.completed  ⏮⏮
        }) 
        CompletedTodos.forEach((todo)=>{   ⏮⏮⏮⏮
            this.$firebaseRefs.todos.child(todo['.key']).remove()   ⏮⏮⏮
        })
    },
</script>
```



### 채팅앱 만들기 (chat폴더/public폴더/-index.html)

#### index.html

firebase 에서 새로운 프로젝트 만들기

##### 	1. 3종세트 import

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.9.1/firebase.js"></script>
<script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
<script>
    // Initialize Firebase
    // TODO: Replace with your project's customized code snippet
    var config = {
        apiKey: "AIzaSyDgH5qPXaMyhccWJYm_JhqVtwBAFkqT6lI",
        authDomain: "vue-chat-0821.firebaseapp.com",
        databaseURL: "https://vue-chat-0821.firebaseio.com",
        projectId: "vue-chat-0821",
    };
    firebase.initializeApp(config);
</script>
```



##### 	2. body 부분 작성

```html
<body>
    <div id="app">
        <ul>
            <li v-for="message in messages">
                {{ message.content }}
            </li>
        </ul>
        <input type="text" v-model="newMessage" v-on:keyup.enter="addMessage">
        <button v-on:click="addMessage">></button>
    </div>

    <script>
        const app = new Vue({
            el: '#app',
            data: {
                messages: [],
                newMessage:'',
            },
            methods: {
                addMessage: function(){  // addMessage 라는 함수는
                    this.messages.push({  // data-messages 리스트에 새로운 데이터를 넣는 함수다
                        content: this.newMessage
                    })
                    this.newMessage='' // input 창 비우기 위한 코드
                }
            }
        })
    </script>

</body>
```



##### 	3. firebase 이용하려고 body 부분 수정

```html
<body>
    <div id="app">
        <ul>
            <li v-for="message in messages" v-bind:key="message['.key']"> ⏮⏮
                {{ message.content }}
            </li>
        </ul>
        <input type="text" v-model.trim="newMessage" v-on:keyup.enter="addMessage"> ⏮⏮
        <!-- trim 역할 .  쓸데없는 공백 없애줌 >>  빈칸으로 enter 치면 메시지 입력x, -->
        <button v-on:click="addMessage">></button>
    </div>

    <script>
        const database = firebase.database()  ⏮⏮

        const app = new Vue({
            el: '#app',
            data: {
                newMessage:'', ⏮⏮
            },
            firebase : { ⏮⏮
                messages : database.ref('messages')
            },
            methods: {
                addMessage: function(){
                    this.$firebaseRefs.messages.push({ ⏮⏮
                        content: this.newMessage
                    })
                    this.newMessage='' // input 창 비우기 위한 코드
                }
            }
        })
    </script>

</body>
```



##### 	4. 빈칸으로 엔터치면 메시지로 안 넘어가도록 수정

```html
<script>
    const database = firebase.database()

    const app = new Vue({
        el: '#app',
        data: {
            newMessage:'',
        },
        firebase : {
            messages : database.ref('messages')
        },
        methods: {
            addMessage: function(){
                if (this.newMessage) {  ⏮⏮⏮⏮⏮
                    this.$firebaseRefs.messages.push({
                        content: this.newMessage
                    })
                    this.newMessage='' // input 창 비우기 위한 코드
                }
            }
        }
    })
</script>
```



##### 	5. 로그인 기능 이용해서, 회원가입기능 붙이기	

​	`<https://console.firebase.google.com/project/vue-chat-0821/authentication/providers>` 

> >  우측상단 - 문서로 이동
> >
> > `<https://firebase.google.com/docs/auth/web/firebaseui?authuser=0>`

​	

1. 헤드에 추가

```html
<head>
    <script src="https://cdn.firebase.com/libs/firebaseui/3.5.2/firebaseui.js"></script>
    <link type="text/css" rel="stylesheet" 			href="https://cdn.firebase.com/libs/firebaseui/3.5.2/firebaseui.css" />
</head>
```



2. script 변수추가

   ```html
   <script>
       const database = firebase.database()
       const auth = firebase.auth()  ⏮⏮   // 로그인 하는 모든 기능 구현되어 있음
       const ui = new firebaseui.auth.AuthUI(auth)  ⏮⏮ 
   </script>
   ```

   

3. 위 페이지에서 `로그인 방법 설정 - 이메일 주소 및 비밀번호`, `로그인` 코드 부분 복사하여 methods 추가

   ```html
   <script>
       methods: {
           addMessage: function () {
               if (this.newMessage) {
                   this.$firebaseRefs.messages.push({
                       content: this.newMessage
                   })
                   this.newMessage = '' // input 창 비우기 위한 코드
               }
           }, // addMessage 끝
   
               initUi: function () {
                   ui.start('#firebaseui-auth-container', {
                       signInOptions: [
                           firebase.auth.EmailAuthProvider.PROVIDER_ID],  // email 로 로그인 옵션
                       callbacks: {
                           signInSuccessWithAuthResult: function (authResult, redirectUrl) {  // 로그인이 성공했으면 뒤에 무슨 실행을 할지
                               // User successfully signed in.
                               // Return type determines whether we continue the redirect automatically
                               // or whether we leave that to developer to handle.
                               return true;
                           },
                           // Other config options...
                       },
                   });
               }
       }
   </script>
   ```



4. button 밑에 새로운 div 만들기

   ```html
   <body>
       <button v-on:click="addMessage">></button>
       <div id="firebaseui-auth-container"></div>
   </body>
   ```

   

5. methods 랑 같은 레벨에 mounted 작성

   ```html
   <script>
    mounted : function(){   // mount 가 된 이후 실행될 함수
       this.initUi()        
    	}
   </script>
   ```

   

6. 채팅창과, 로그인창 div 분리

   ```html
   <body>
       <div id="app">
           <div>  <!-- 채팅창 div-->
               <ul>
                   <li v-for="message in messages" v-bind:key="message['.key']">
                       {{ message.content }}
                   </li>
               </ul>
               <input type="text" v-model.trim="newMessage" v-on:keyup.enter="addMessage">
               <!-- trim 역할 .  쓸데없는 공백 없애줌 >>  빈칸으로 enter 치면 메시지 입력x, -->
               <button v-on:click="addMessage">></button>
           </div>
   
           <div>  <!-- 로그인창 div-->
               <div id="firebaseui-auth-container"></div>
           </div>
   
       </div>
   </body>
   ```

   

7. data 에 추가

   ```html
   <script>
    data: {
                   newMessage: '',
                   currentUser:{
                       uid:'',
                       email:'',
                       name:'',
                   }
               },
   
   </script>
   ```



8. 로그인 되어 있으면 채팅창 보여주도록 if 문 걸어줌

   ```html
   <!-- 채팅창 div-->
   
   <div v-if="currentUser.uid">  ⏮⏮
       <ul>
           <li v-for="message in messages" v-bind:key="message['.key']">
               {{ message.content }}
           </li>
       </ul>
       
       <input type="text" v-model.trim="newMessage" v-on:keyup.enter="addMessage">
       <button v-on:click="addMessage">></button>
   </div>
   ```

   

9. 로그인 에러 해결 (로그인 성공하면 어떻게 할지, methods 수정 )

   ```html
   <script>
       initUi: function () {
           ui.start('#firebaseui-auth-container', {
               signInOptions: [
                   firebase.auth.EmailAuthProvider.PROVIDER_ID],  // email 로 로그인 옵션
               callbacks: {
                   signInSuccessWithAuthResult: (authResult, redirectUrl)=> {  // 로그인이 성공했으면 뒤에 무슨 실행을 할지
                       // 로그인성공하면 authResult 에 성공정보가 담겨 있음
                       this.currentUser.uid = authResult.user.uid     //  authResult.user에 user 의 uid , email 등등 다 담겨있음
                       this.currentUser.email = authResult.user.email
                       this.currentUser.name = authResult.user.displayName
                
                       return false; 
   // true 이면 다른페이지로 redirect 시키므로, vue 는 싱글페이지니까 redirect 안 하도록 false ( 그냥 로그인 창 숨겨줌)
                   },
               },
           });
       }
   
   </script>
   ```

   

10. 새로고침하면 로그인풀림 ( ∵ 새로고침하면 mount 가 실행됨 → initUi 실행)  문제 해결하기

    ```html
    <script>
        mounted: function () {   // mount 가 된 이후 실행될 함수
            auth.onAuthStateChanged((user) => {
                if (user) {  // user 정보가 일치하면 로그인 창 안 보여줘도 돼
                    this.currentUser.uid = user.uid
                    this.currentUser.email = user.email
                    this.currentUser.name = user.displayName
                } else {  // user 정보가 안 들었다면 로그인창 보여줘
                    this.initUi()
                }
            })
        }
    </script>
    ```

    

11. 로그아웃만들기(methods 內 작성)

    ```html
    <script>
        logout: function(){
            // 1. currentUser 초기화
            this.currentUser = {
                uid:'',
                email:'',
                name:'',
            },
                // 2. firebase auth한테 로그아웃 알리기
                auth.signOut().then(()=>{
    
            }).catch((error)=>{
    
            })
        },
    
    
    </script>
    ```

    

12. 채팅창 div 위에 로그아웃버튼만들기

    ```html
    <body>
    
        <div v-if="currentUser.uid">
            <div>
                <span>Hi, {{ currentUser.name }}</span>
                <button @click="logout">로그아웃</button>
            </div>
            <!-- 채팅창 div-->
            <ul>
                <li v-for="message in messages" v-bind:key="message['.key']">
                    {{ message.content }}
                </li>
            </ul>
            <input type="text" v-model.trim="newMessage" v-on:keyup.enter="addMessage">
            <!-- trim 역할 .  쓸데없는 공백 없애줌 >>  빈칸으로 enter 치면 메시지 입력x, -->
            <button v-on:click="addMessage">></button>
        </div>
    
        <div>
            <!-- 로그인창 div-->
            <div id="firebaseui-auth-container"></div>
        </div>
    
        </div>
    </body>
    ```



13. 채팅창에 이름 보이기

    ```html
    <li v-for="message in messages" v-bind:key="message['.key']">
        <b>{{ message.username }}</b>{{ message.content }}
    </li>
    ```

    

    ```html
    <script>
        addMessage: function () {
            if (this.newMessage) {
                this.$firebaseRefs.messages.push({
                    username: this.currentUser.name,
                    content: this.newMessage
                })
                this.newMessage = '' // input 창 비우기 위한 코드
            }
        },
    </script>
    ```

    


### npm? (posting 서비스를 통해 웹 상에 공유시키도록 한다)

* cmd로 chat 폴더까지 이동
* `npm install -g firebase-tools`
* `firebase login`
* `firebase init`

public, ` Configure as a single-page app (rewrite all urls to /index.html)? Yes`



*database.urles.json 수정

```json
{
  "rules": {
    "messages" : {
      ".read" : "auth != null",
      ".write": "auth != null"
    }
  }
}
// 로그인 사용자가 null 이 아닐 때만 읽고 쓰도록
```



cmd에 `firebase deploy` 입력

`https://vue-chat-0821.firebaseapp.com`