let quoteBtn = document.getElementById('get-quotes')
let quoteDiv = document.getElementById('quotes')
let filter = document.getElementById('filter')
let nextBtn = document.getElementById('next-page')
let backBtn = document.getElementById('back-page')
let pageNumber = 1

nextBtn.addEventListener('click', function(){
    pageNumber += 1
    getQuotes()
})

backBtn.addEventListener('click', function(){
    if (pageNumber > 1){
    pageNumber -= 1
    getQuotes()
    }
})

quoteBtn.addEventListener('click', async function(){
    getQuotes()
    
})

async function getQuotes(){
    const api_key = 'b0932a3293d219f164528766c4fc6379'
    let filterText = filter.value
    const base_url = `https://favqs.com/api/quotes/`
    let url
    
    if (filterText) {
        url = base_url+=`?filter=${filterText}`
    } else{
        url = base_url
    }

    url += `&page=${pageNumber}`
    let owl = {
        headers: {
            Authorization: `Token token=${api_key}`
        }
    }
    let response = await axios.get(base_url, owl)
    let data = response.data

    let quotes = data.quotes

    let quotesList = ''

    for (let quote of quotes){
        quotesList += `<q class='quote'>${quote.body}</q> <span>-${quote.author}</span><br>`
    }
    quoteDiv.innerHTML = quotesList
}