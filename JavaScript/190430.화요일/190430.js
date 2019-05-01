// 반복 1 - while
let i = 0
while (i < 10) {
    console.log(i)
    i++
}

// 반복 2 - for
for (let j=0; j < 10; j++) {
    console.log(j)
}

// 반복 3 - for of
for (let number of [1,2,3,4,5]) {   // const로도 선언 가능
    console.log(number)
}

// Array (배열)
const numbers = [1,2,3,4]

console.log(numbers[0])
console.log(numbers[-1])

// Object (객체)
const me = {
    name: 'nwith',
    'phone number': '01012345678',
    appleProducts: {
        ipad: true,
        iphone: 'X'
    }
}

// JSON - JavaScript Object Notation (JS 객체 표기법)
// JSON.stringify()    // Object -> JSON String
// JSON.parse()    // JSON String -> Object


// 함수
// 방법 1 - 선언식
function add(num1, num2) {
    return num1 + num2
}
console.log('add: ' + add(1,2))

// 방법 2 - 표현식
const sub = function (num1, num2) {
    return num1 - num2
}
console.log('sub: '+ sub(5, 3))

typeof add // function
typeof sub // function

// Arrow Function - ES 6 들어서 새로 생긴 기능(핵심적이지만 일단 알아두는 정도로 생각)

// 기존 방법
// const mul = function (num1, num2) {
//     return num1 * num2
// }

// Arrow
const mul = (num1, num2) => {
    return num1 * num2
}

let square = (num) => { 
    return num ** 2 
}

// return문 단 한줄이면 {} & return 생략 가능. square는 위에 있기 때문에 let을 생략한 것일 뿐.
square = (num) => num ** 2

// () 안의 인자가 하나뿐이면 ()도 생략 가능. 인자가 0개 일때는 생략 불가능.
square = num => num ** 2
let noArgs = () => 'No args'

// Object를 return한다면? 괄호가 없으면 {}를 함수의 {}로 인식하기 때문에 ()가 필요! 
let returnObject = () => ({key:'value'})

// 함수의 기본 인자
const sayHello = (name='noName') => `hi ${name}` // hi noName 으로 출력됨.

sayHello('john')
sayHello()  // 기본 값을 주지 않았기 때문에 hi noName 으로 출력됨.

// 익명 함수(변수가 선언되지 않는 함수) : 호출 불가
function (num) { return num ** 3 }  // 세제곱
(num) => { return num ** 0.5 } // 제곱근

// 익명 함수 즉시 호출 : ()로 감싸면 하나의 함수가 돼버림.
(function (num) { return num ** 3})(3) // 3의 세제곱
// 가독성도 떨어지고 코드를 고의로 줄일 때 말곤 잘 안쓰임.