let deck = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

let cardOne = document.querySelector('#cardOne')
let cardTwo = document.querySelector('#cardTwo')
let button = document.querySelector('#button')



function advice () {
    let one = deck[cardOne.value]
    let two = deck[cardTwo.value]

    if ((deck[one] + deck[two]) < 17) {
        alert('take a hit')
    } else if ((deck[one] + deck[two]) > 17) {
        alert('stay strong')
    }
        
}

button.addEventListener('click', advice); 