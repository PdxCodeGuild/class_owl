let quoteDiv = document.querySelector("#quote")
let getQuoteBtn = document.querySelector("#getQuote")
let authorDiv = document.querySelector("#author")

let quoteEl = document.createElement('div')



getQuoteBtn.addEventListener("click", function(){
    let x = fetch("https://favqs.com/api/qotd")
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        // console.log(data)
        quoteText = data.quote.body
        quoteAuthor = data.quote.author

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