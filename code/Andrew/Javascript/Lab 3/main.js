let question = document.querySelector("#question")
let answer = document.querySelector("#answer")
let askButton = document.querySelector("#submit")
let asked = document.querySelector("#asked")


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

let ques = []
let counter = 0

question.focus()


const remover = function() {
    answer.innerTex = ""
}

askButton.addEventListener('click', function() {
    ques.push(question.value)
    let randInd = Math.floor(Math.random()*(ANSARR.length))
    
    let result = ANSARR[randInd]
    answer.style.color = "gray;"
    answer.innerText = result    
    answer.style = 'text-align: center; font-size: 2rem;'
    question.value = ""
    
    
    setTimeout(remover, 1500)
    if (counter <=5){
        let liChild = document.createElement('li')
        liChild.classList.add('removed')
        let textEl = document.createTextNode(`${ques[counter]}`)
            liChild.appendChild(textEl)
            asked.appendChild(liChild)
            counter += 1
        
    }
    else{
        let listChildren = document.getElementsByClassName("removed")
        let copyList =[...listChildren]

        for (x of copyList){
            x.remove()
            
        }
        let liChild = document.createElement('li')
        liChild.classList.add('removed')
        let textEl = document.createTextNode(`${ques[counter]}`)
        liChild.appendChild(textEl)
        asked.appendChild(liChild)
        ques = []
        counter = 0 
          
    }


    
    }
    
)





