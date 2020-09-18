let picker = document.querySelector("#sitePicker")
// picker.setAttribute("src", "https://wikipedia.com")

const WEBSITES = ['https://www.dictionary.com', 'https://www.wikipedia.com', 'https://www.thesaurus.com', "https://portlhologram.com/"]
let counter = 5
let randInd = Math.floor(Math.random() * WEBSITES.length)
let timeLeft = document.querySelector("#timeLeft")
let stopButton = document.querySelector("#stopButton")
let changeButton = document.querySelector("#changeButton")

changeButton.addEventListener("click", function(){
    // console.log(this)
    webPicker(counter)
    
})





const webPicker = function(counter) {
    // console.log(randInd)
    
    var test = window.setInterval(timer, 1000)
    // window.location = WEBSITES[randInd]

    stopButton.addEventListener("click", function(){
        clearInterval(test)
        timeLeft.innerText = 'Stopped!'
    
    })


}


const timer = function(){
    if (counter >= 0){
        timeLeft.innerText = `Time Left: ${counter} seconds 
        URL: ${picker.getAttribute("src")}`
        // console.log(randInd)
        timeLeft.style = "font-weight: 900; font-size: 1.5rem;"

        counter -= 1
        
        
    }
    else{
        picker.setAttribute("src", WEBSITES[Math.floor(Math.random() * WEBSITES.length)])
        
        // window.location = WEBSITES[randInd]
        
        counter = 5
    }
    
    
}
