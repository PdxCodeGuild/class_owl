let app = new Vue({
    el: '#app',
    data: {
      quotes: '',
      pageNumber: 1,
      filter: ''  
    },
    methods:{
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
            const api_key = 'b0932a3293d219f164528766c4fc6379'
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
