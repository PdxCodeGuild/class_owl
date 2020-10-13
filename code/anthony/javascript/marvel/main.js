let app = new Vue({
    el: "#app",
    data: {
        getChar: '',
        result: ''
    }, 
    methods: {
        getHero: async function() {
            let url = `https://gateway.marvel.com/v1/public/characters?name=${this.getChar}&ts=1&apikey=46a047d390231cbf4256827b02acf4fb&hash=7251119a520273af31b1720bc26a784f`
        
            let config = {
                url: 'https://gateway.marvel.com/v1/public/characters',
                method: 'get',
                params: {
                    name: this.getChar,
                    ts: 1,
                    apikey: '46a047d390231cbf4256827b02acf4fb',
                    hash: '7251119a520273af31b1720bc26a784f',
                    limit: 100,
                    offset: 0,
                }
            }

            let response = await axios.request(config)
            console.log(response.data)
        }
    }
})
