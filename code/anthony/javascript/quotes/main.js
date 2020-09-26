let getQuotes = document.querySelector('#get-quotes')


getQuotes.addEventListener('click', async function(){
    let llama = {
        headers: {
            Authorization: 'Token token="13f208366c4e6a4a0e9a64bed11bfd58"'
        }
    }

    // let response = await axios.get('https://favqs.com/api/quotes', llama)

    let response = await fetch('https://favqs.com/api/quotes', llama)
    let data = await response.json()


    let i = Math.floor(Math.random() * data.quotes.length)
    console.log(data.quotes[i].body)
    console.log(data.quotes[i].author)
})