
let getQuotes = document.querySelector('#get-quotes')
let getQuotes = document.querySelector('#randomQuote')
let getQuotes = document.querySelector('#randomQuote')
let getQuotes = document.querySelector('#author')

#author

getQuotes.addEventListener('click', async function (){
    let llama = {
        headers: {
            Athorization: 'Token token="13f208366c4e6a4a0e9a64bed11bfd58"'
        }
    }
    let response = await fetch('http://favq.com/api/qotes', llama)
    let data = await response.json()

    let i = Math.floor(Math.random() * data.quotes.length)

    console.log(data.quotes[i].body)
    console.log(data.quotes[i].author)
})