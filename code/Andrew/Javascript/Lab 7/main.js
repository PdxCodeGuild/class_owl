let quoteDiv = document.querySelector("#quote")
let getQuoteBtn = document.querySelector("#getQuote")
let authorDiv = document.querySelector("#author")
let adderValue = document.querySelector('#adderValue')


let quoteEl = document.createElement('div')

let headerObj = {
    headers: {
        Authorization: 'Token token="077565650e639d921b45668e52e53301"'
    }
}
let url = "https://favqs.com/api/quotes"



getQuoteBtn.addEventListener("click", function(){
    let filterText = adderValue.value? "&filter=" + adderValue.value + '&type=tag': ''
    let adder = "?page="+ Math.floor(Math.random()*26) + filterText
    console.log(adderValue.value)
    let x = fetch(url+adder, headerObj)
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data)
        let ind = Math.floor(Math.random()*25)
        quoteText = data.quotes[ind].body
        quoteAuthor = data.quotes[ind].author

        authorDiv.innerText = `-${quoteAuthor}`
        quoteDiv.innerText = `${quoteText}`
        
        // let quoteElBody = document.createElement('div')
        // quoteElBody.appendChild(quoteDiv)
        // quoteElBody.appendChild(authorDiv)

        // quoteEl.appendChild(quoteElBody)
        // return quoteEl
    })
    getQuoteBtn.blur()
    console.log(quoteEl)
})


getQuoteBtn.click()