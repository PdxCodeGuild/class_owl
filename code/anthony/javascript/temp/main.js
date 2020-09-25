let getQuoteBtn = document.querySelector('#get-quote')
let quoteList = document.querySelector('#quote-list')

async function getQuotes() {

    let options = {
        headers: {
            Authorization: 'Token token="b1524d3cd339763f91e640aa3c593d89"'
        }
    }

    let response = await axios.get('https://favqs.com/api/quotes',options)
    console.log(response.data)
}

getQuoteBtn.addEventListener('click', async () => {
    // let response = await axios({
    //     method: 'get',
    //     url: 'https://favqs.com/api/quotes',
    //     headers: {
    //         Authorization: 'Token token="b1524d3cd339763f91e640aa3c593d89"'
    //     }
    // })
    // let data = response.data
    // let quotes = data.quotes
    // let output

    // quotes.forEach(element => {
    //     output += `<p>${element.body} -- ${element.author}</p>`
    // });

    // quoteList.innerHTML = output

    getQuotes()
})