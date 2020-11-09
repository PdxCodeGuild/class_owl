let app = new Vue({
    el: '#app',
    data:{
        baseURL: 'https://favqs.com/api/qotes',
        headers: {
            Authorization: 'Token token="774d5ebb558a0113d53204d5eca5553c"'
        },

    },
    methods: {
        getQuote: function(raceURL){
            GET /api/quotes/:quote_id
            })
        }
    },
    created(){
        axios.get(this.baseURL + '/api/')
        .then(function(response){
            return response.data
            console.log(response.data)
        })
        .then(function(data){
            this.endpoints = data
            print(this.endpoints)
        })
    }

})