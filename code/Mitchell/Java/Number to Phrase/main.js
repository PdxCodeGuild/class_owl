let phrase = {
    1: "teen",
    2: 'twenty ',
    3: 'thirty ',
    4: 'forty ',
    5: 'fifty ',
    6: 'sixty ',
    7: 'seventy ',
    8: 'eighty ',
    9: 'ninety ',
}
let ones_digit_phrase = {
    1: "one",
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

let teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
}

let hundred_digit_phrase = {
    1: 'one hundred',
    2: 'two hundred ',
    3: 'three hundred ',
    4: 'four hundred ',
    5: 'five hundred ',
    6: 'six hundred ',
    7: 'seven hundred ',
    8: 'eight hundred ',
    9: 'nine hundred ',
}

let input = document.querySelector('#input')
let button = document.querySelector('#button')

function result () {
    let digit = input.value

    if ( (digit >= 1) & (digit <= 9) ) {
        alert(ones_digit_phrase[digit]);
    } else if ( (digit >= 10) & (digit <= 15) ) {
        alert(teens[digit]);                                                                                  
    } else if ( (digit >= 100) & (digit <= 999) ) {
        hundred_digit = Math.floor(digit / 100 % 10);
        tens_digit = (digit % 10) % 10;
        ones_digit = (digit % 10);

        function digitreturnhundred() {
            hundred_half = hundred_digit_phrase[hundred_digit]
            first_half = phrase[tens_digit]
            second_half = ones_digit_phrase[ones_digit]
            console.log(hundred_digit)
            alert('Your number is written as ' + hundred_half + first_half + second_half)
        }
        digitreturnhundred()
    } else {
        tens_digit = (digit % 10)
        ones_digit = (digit % 10)
    }
        function digitreturn() {
            first_half = phrase[tens_digit]
            second_half = ones_digit_phrase[ones_digit]
            alert( 'Your number is written as ' + first_half + second_half)
        }
}


button.addEventListener('click', result);