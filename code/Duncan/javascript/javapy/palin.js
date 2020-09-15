let word = document.getElementById("word")
let answer = document.getElementById("answer")
let clicky = document.getElementById("clicky")


clicky.addEventListener("click", event => {
    let wordA = word.value.split("");
    console.log("hi")
    // wordA.push(word.value)
    console.log(wordA)
    wordB = wordA.slice().reverse()
    console.log(wordB)
    if (wordA.toString() === wordB.toString()){
        answer.innerText = "That is infact a palindrome"
        console.log("clack")
    }

    else if (wordA.toString() !== wordB.toString()){
        answer.innerText = "That is not a Palindrome. Dork"
        console.log("cluck")
    }



})