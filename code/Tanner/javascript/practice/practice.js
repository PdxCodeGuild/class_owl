// for (var x =0; x<10; ++x) {}
// alert(x, console.log("hi there"))

// let a = 5;
// let b = 10.4;
// let c = "Hello";
// let d = true;
// let e = null;
// let f = undefined;

// console.log(f)


// INPUTS*********************************************
// // let name = prompt("name");
// // alert("hello " + name + "! How are you?");

// let name_input = document.querySelector("#name_input");
// let name_value = name_input.value;
// alert(name_value);

//OUTPUTS****************************************************

// alert("hello");

// console.log("hi")

// document.write('<span>yo<span/>');

// STRINGS*************************************************************

// let s = 'hello dude'
// let t = "hola bro"


// console.log(s.startsWith('h'))

// LINE CONTINUATION*************************************************

// let s = 'this is really long\
// String, so long that we had to\
// make lines';

// TEMPLATE LITERALS(fstring) backtick*******************************************

// function getFullName(title, fname, lname, degree) {
//     return `${title} ${fname} ${lname} ${degree}`
// }

// console.log(getFullName('lawyer', 'tyler', 'john', 'associates'));

// function showWork(num1, num2) {
//     return `${num1} + ${num2} = ${num1 + num2}`
// }

// console.log(showWork(3,4));

// CONDITIONALS***************************************************

// let temperature = 78; // if , else if, else
// if (temperature < 60) {
//     alert('cold');
// } else if (temperature < 80) {
//     alert('warm');
// } else {
//     alert('hot')
// }

// // ARRAYS *********************************************************

// // let nums = [2,1,3,4];

// // //
// // nums[0] = 'dogs'

// // console.log(nums)

// // WHILE LOOPS *******************************************************

// // let i = 11;
// // while (i<10) {
// //     console.log(i);
// //     i++;
// // }

// // let invalidInput = true;
// // while (invalidInput) {
// //     answer = prompt('pick a number one to ten: ');
// //     if (answer >= 1 && answer <=10) {
// //         invalidInput = false;
// //     }
// // }

// // FOR LOOPS*******************************************

// // let fruits = ['apples', 'bananas', 'pear']; array
// // fruits.push('cherry'); adding to the arrray
// // for (let i = 0; i<fruits.length; i++) { FOR LOOPS have 3 parts initialization, condition, increment
// //     console.log(fruits[i]);
// // }

// // KEY/VALUE *******************

//     let library_user = {
//         first_name: 'Jane',
//         last_name: 'Smith',
//         age: 20,
//         books: [{
//             title: 'a wrinkle in time',
//             author: 'madeleine',
//             published: 1964
//         },{
//             title: 'the giving tree',
//             author: 'shel',
//             published: 1964
//         }]
//     };

//     console.log(library_user.first_name);
//     // console.log(library_user[first_name]);
//     console.log(library_user.books[1].title);
//     // console.log(library_user[books][0][title]);


// MODULES *****************************************************

// let calculations = {
//     add: function(a,b) {
//         return a + b;
//     },
//     subtract: function(a,b) {
//         return a - b;
//     },
//     multiply: function(a,b) {
//         return a * b;
//     },
//     divide: function(a,b) {
//         return a / b;
//     }
// }

// console.log(calculations.multiply(10,5))

