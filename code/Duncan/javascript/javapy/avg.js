let header = document.getElementById("header")
let firstNum = document.getElementById("firstNum")
let secondNum = document.getElementById("secondNum")
let thirdNum = document.getElementById("thirdNum")
let fourthNum = document.getElementById("fourthNum")
let fithNum = document.getElementById("fithNum")
let output = document.getElementById("output")
let calc = document.getElementById("calc")
let body = document.getElementById("body")


let nums = []

firstNum.addEventListener("input", function(){
    nums.push(parseInt(firstNum.value));
    console.log(nums[0])
})

secondNum.addEventListener("input", function(){
    nums.push(parseInt(secondNum.value))
    console.log(nums)
})

thirdNum.addEventListener("input", function(){
    nums.push(parseInt(thirdNum.value))
    console.log(nums)
})

fourthNum.addEventListener("input", function(){
    nums.push(parseInt(fourthNum.value))
    console.log(nums)
})

fithNum.addEventListener("input", function(){
    nums.push(parseInt(fithNum.value))
    console.log(nums)
})

calc.addEventListener("click", function(){
    var avg = nums.reduce((a, b) => a + b, );
    
    output.innerText = `Your Average is ${avg}`
    console.log(` the avg is : ${avg}. `)
})

// couldnt get this to work

// fithNum.addEventListener("keyup",(function(event){
//     if (event.keycode === 13) {
//         console.log();
//         calc.click();
//     };

//     // let click = function() {
//     //     var avg = nums.reduce((a, b) => a + b, );
    
//     //     output.innerText = `Your Average is ${avg}`
//     //     console.log(` the avg is : ${avg}. `) 
//     // }
// }))










// var array = [1, 2, 3, 4, 5];
    
//     // Getting sum of numbers
//     var sum = array.reduce(function(a, b){
//         return a + b;
//     }, 0);
    
//     console.log(sum); // Prints: 15