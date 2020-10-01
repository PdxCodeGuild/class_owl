let quoteBtn = document.getElementById('get-quotes')
let quoteDiv = document.getElementById('quotes')
let filter = document.getElementById('filter')
let nextBtn = document.getElementById('next-page')
let backBtn = document.getElementById('back-page')
let pageNumber = 1


nextBtn.addEventListener('click', function(){
    pageNumber++
})

backBtn.addEventListener('click', function(){
    if (pageNumber > 1){
        pageNumber--
    }
})

quoteBtn.addEventListener('click', async function(){
    const api_key = '13f208366c4e6a4a0e9a64bed11bfd58'
    let filterText = filter.value
    const base_url = 'https://favqs.com/api/quotes/?filter=${filterText}&page=${pageNumber}'

    let owl = {
        headers: {
            Authorization: 'Token token=${api_key}'
        }
    }

    let response = await axios.get(base_url, owl)
    let data = response.data
    let quotes = data.quotes
    let quotesList = ''
    for (let quote of quotes){
        quotesList += '<q class="quote">${quote.body} <span>${quote.author}</span></q>'
    }

    quoteDiv.innerHTML = quotesList
})