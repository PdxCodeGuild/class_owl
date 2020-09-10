let header = document.getElementById("header")
let firstNum = document.getElementById("firstNum")
let secondNum = document.getElementById("secondNum")
let thirdNum = document.getElementById("thirdNum")
let fourthNum = document.getElementById("fourthNum")
let fithNum = document.getElementById("fithNum")
let output = document.getElementById("output")

let nums = []

firstNum.addEventListener("input", function(){
    let num1 = nums.push(firstNum.value)
    console.log(nums[0])
})

secondNum.addEventListener("input", function(){
    let num2 = nums.push(secondNum.value)
    console.log(nums)
})

thirdNum.addEventListener("input", function(){
    let num3 = nums.push(thirdNum.value)
    console.log(nums)
})

fourthNum.addEventListener("input", function(){
    let num4 = nums.push(fourthNum.value)
    console.log(nums)
})

fithNum.addEventListener("input", function(){
    let num5 = nums.push(fithNum.value)
    console.log(nums)
})

output.addEventListener("click", function(){
    

})



var array = [1, 2, 3, 4, 5];
    
    // Getting sum of numbers
    var sum = array.reduce(function(a, b){
        return a + b;
    }, 0);
    
    console.log(sum); // Prints: 15