let getQuotes = document.querySelector('#get-quotes')

getQuotes.addEventListener('click', async function()){
    let requesthats = {
        headers: {
            Authorization: 'Token token="774d5ebb558a0113d53204d5eca5553c"'
        }
    }
    let response = await axios.get('https://favqs.com/api/qotes', requesthats)

    console.log(response.data)
}