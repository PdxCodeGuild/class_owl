let app = new Vue({
    el: '#app',
    data: {
        quotes: '',
        pageNumber: 1,
        filter: ''
    },
    methods: {
        nextPage(){
            this.pageNumber++
            this.getQuotes()
        },
        previousPage(){
            if(this.pageNumber > 1){
                this.pageNumber--
                this.getQuotes()
            }
        },
        async getQuotes(){
            const api_key = '13f208366c4e6a4a0e9a64bed11bfd58'
            let url = 'https://favqs.com/api/quotes/'

            if(this.filter){
                url += `?filter=${this.filter}&page=${this.pageNumber}`
            } else{
                url += `?page=${this.pageNumber}`
            }

            let owl = {
                headers: {
                    Authorization: `Token token=${api_key}`
                }
            }
            let response = await axios.get(url, owl)
            this.quotes = response.data.quotes
        }
    }
})