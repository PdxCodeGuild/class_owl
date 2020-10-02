// Part 1
let url = 'https://favqs.com//api/quotes'
let getQuote = document.querySelector('#getQuote')
let randomQuote = document.querySelector('#randomQuote')
let author = document.querySelector('#author')

// event listener on click everything below happens
getQuote.addEventListener('click', async function(){
    // define the api key
    let aKey = {
        headers: {
            Authorization: 'Token token="b0932a3293d219f164528766c4fc6379"'
        }
    }
    // fetching the data from API
    let response = await fetch(url, aKey)
    let data = await response.json()
        // randomizing the quote and showing the quote body
        let i = Math.floor(Math.random() * data.quotes.length)
            randomQuote.innerText = data.quotes[i].body
            author.innerText = data.quotes[i].author
})



// Part 2


// defining variables
let getPage = document.querySelector('#getPage')
let PageQuote = document.querySelector('#PageQuote')
// defining the parameter variables
let page = document.querySelector('#page')
let filter = document.querySelector('#filter')




// on clik everything below happens
getPage.addEventListener('click', async function(){
    let page = document.querySelector('#page')
    let filter = document.querySelector('#filter')
    // encodeURIComponent function removes all spaces from the data stream (replaced with %20)
    let filterOne = encodeURIComponent(filter.value)

    // url variable defined with parameters 
    let urlOne = `https://favqs.com/api/quotes?page=${page.value}"+page_id+"&filter=${filterOne}`
    let bKey = {
        headers: {
            Authorization: 'Token token="b0932a3293d219f164528766c4fc6379"'
        }
    }

    // grabbing the data
    let response = await fetch(urlOne, bKey)
    let data = await response.json()
    
    // defining a blank string variable
    let quotePage = ''
    // loop to build the quote list string
    for(let quote of data.quotes){ 
        // quotePage is the the list string, put in as <p> tags
        quotePage += `<p>${quote.body} - ${quote.author}</p> <br></br>`      
    }
    
    // displaying the <p> tags as HTML
    pageQuote.innerHTML = quotePage
    
})