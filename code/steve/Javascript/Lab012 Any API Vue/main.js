let app = new Vue({
    el: '#app',
    data: {
        
        getChar: '',
        bio: '',
        hero: []

    },
    methods: {
        getHero: async function(){
            const api_key = '10218561275765916'

         
            let url = `https://gateway.marvel.com/v1/public/characters?name=${this.getChar}&ts=1&apikey=46a047d390231cbf4256827b02acf4fb&hash=7251119a520273af31b1720bc26a784f`

            
            let config = {
                url: 'https://gateway.marvel.com/v1/public/characters',
                method: 'get',
                params: {
                    name: this.getChar,
                    ts: 1,
                    apikey: '46a047d390231cbf4256827b02acf4fb',
                    hash: '7251119a520273af31b1720bc26a784f',
                }
            }
            let response = await axios.request(config)
            console.log(response)
            
            let copyrt = response.data.copyright
            let charId = response.data.data.results[0].id
            let description = response.data.data.results[0].description
            let img = response.data.data.results[0].thumbnail.path + '.' + response.data.data.results[0].thumbnail.extension
            this.hero.push({ 
                cid: charId,
                cardText: description,
                picture: img
            })
            
        }
        
        
        
}}
)