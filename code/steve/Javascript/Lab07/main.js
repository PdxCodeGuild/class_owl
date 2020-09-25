

let url = 'https://favqs.com//api/quotes'
let getQuote = document.querySelector('#getQuote')
let randomQuote = document.querySelector('#randomQuote')
let author = document.querySelector('#author')

getQuote.addEventListener('click', async function(){
    
    let aKey = {
        headers: {
            Authorization: 'Token token="b0932a3293d219f164528766c4fc6379"'
        }
    }
    let response = await fetch(url, aKey)
    let data = await response.json()
            
        let i = Math.floor(Math.random() * data.quotes.length)
            randomQuote.innerText = data.quotes[i].body
            author.innerText = data.quotes[i].author
})


let getPage = document.querySelector('#getPage')
let PageQuote = document.querySelector('#PageQuote')

let page = document.querySelector('#page')
let filter = document.querySelector('#filter')





getPage.addEventListener('click', async function(){
    let page = document.querySelector('#page')
    let filter = document.querySelector('#filter')
    let filterOne = encodeURIComponent(filter.value)

    let urlOne = `https://favqs.com/api/quotes?page=${page.value}"+page_id+"&filter=${filterOne}`
    let bKey = {
        headers: {
            Authorization: 'Token token="b0932a3293d219f164528766c4fc6379"'
        }
    }
    let response = await fetch(urlOne, bKey)
    let data = await response.json()
    console.log(data.quotes)

    let blah = ''
    for(let quote of data.quotes){ 
        blah += `<p>${quote.body} - ${quote.author}</p>`      
    }
    

    pageQuote.innerHTML = blah
    
})