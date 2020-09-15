let question = document.querySelector("#question")
let answer = document.querySelector("#answer")
let askButton = document.querySelector("#submit")


const ANSARR = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]


askButton.addEventListener('click', function() {

    let randInd = Math.floor(Math.random()*(ANSARR.length))

    let result = ANSARR[randInd]

    answer.style.color = "gray;"
    answer.innerText = result    
    answer.style = 'text-align: center; font-size: 2rem;'


})
