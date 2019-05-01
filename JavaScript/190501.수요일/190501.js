// Array Helper Methods

// case 1. 
// ES5
// var colors = ['red', 'blue', 'green']

// for ( var i=0; i <colors.length; i++) {
//     console.log(colors[i]);
//}   // 결과값 : red blue green 출력

// ES6+ 에 새로 생긴 기능 : forEach, 반환값은 없고 반복문만 돌려줌. forOf 와 유사
const colors =  ['red', 'blue', 'green']

colors.forEach(function(color) {  // 익명함수 = callback function, 함수자체가 parameter 로 넘어가
    console.log(color)
})

//CASE 2.
// ES5
// var numbers = [1,2,3]
// var doubleNumbers = []

// for (var i=0; i<numbers.length; i++) {
//     doubleNumbers.push(numbers[i]*2)
// }
// console.log(doubleNumbers) // 결과값 : [2,4,6] 출력

// ES6+ 에 새로 생긴 기능 : map
const numbers = [1,2,3]
const doubleNumbers = numbers.map(function(number){
    return number*2  // number 로 받아서 어떤 함수로 처리 할 지 return 뒤에 씀, ∴ return 값 필수 / 기존 배열은 그대로 보관하고, 새로운 배열에 할당
})

console.log(doubleNumbers) // 결과값 : [2,4,6] 출력


// CASE 3
// ES6+ - filter
const products = [
    {name : 'cucumber', type: 'vegetable'},
    {name : 'banana', type: 'fruit'},
    {name : 'carrot', type: 'vegetable'},
    {name : 'apple', type: 'fruit'}
]

const fruitProducts = products.filter(function(product){
    return product.type === 'fruit' // true 인지 false 인지 반환
}) // 해당조건이 true 이면 products 에서 그 item 자체를 가져와서, fruitProducts 에 넣음

console.log(fruitProducts)  // 결과값 : [ { name: 'banana', type: 'fruit' }, { name: 'apple', type: 'fruit' } ]

// case4
// es6+ - find
const users = [
    {name : 'nwith'},
    {name : 'admin'},
    {name : 'zzuli'},
]

const foundUser = users.find(function(user){
    return user.name === 'admin'  // 조건에 맞는 거 찾으면 바로 반복 종료
})

console.log(foundUser)

// case5
// es6+ - every & some
const computers = [
    {'name': 'macbook', ram:16},
    {'name': 'gram', ram:8},
    {'name': 'serues9', ram:32},
]

const everyComputersAvailable = computers.every(function(computer){
    return computer.ram > 16 // 모든 값이 16 초과여야, true 반환
})

const someComputersAvailable = computers.some(function(computer){
    return computer.ram>16 // 하나라도 16넘으면 true 반환
})

console.log(everyComputersAvailable) // 결과 : false
console.log(someComputersAvailable) // 결과: true