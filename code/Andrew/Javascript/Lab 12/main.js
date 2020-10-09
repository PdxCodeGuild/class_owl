


let prg = new Vue({

    el: "#prg",
    data:{
        apiUrl: 'https://api.teleport.org/api/cities/',
        city: '',
        linkTo:'',
        nicks: [],
        
        dataBody: "",
        mayor:'',
        lng:'',
        lat:'',
        urlImg: null,
        scores: '',
        scoresObj: [],
        dumpsterFire: true
    },
    methods:{
        getResp: function(){
            this.apiUrl= 'https://api.teleport.org/api/cities/'
            this.apiUrl += this.city?  `?search=${encodeURIComponent(this.city)}`: `?search=portland` 

            let a = fetch(this.apiUrl)
            .then(function(response){
                return response.json()
            })
            .catch(function(opps){
                console.log('does this work?')
            })
            .then(function(data){
                
                if(data.count ===0){
                    
                        return prg.city = 'No Such City Found!'

                    }
                    prg.nicks = data._embedded["city:search-results"][0].matching_alternate_names
                
                    
                    prg.city = data._embedded["city:search-results"][0].matching_full_name
                    prg.linkTo = data._embedded["city:search-results"][0]._links["city:item"].href
                    
                    
                    
                    let b = fetch(prg.linkTo)
                    .then(function(response){
                        return response.json()
                    })
                    .then(function(data){
                        
                        prg.lng = data.location.latlon.longitude
                        prg.lat = data.location.latlon.latitude
                        // console.log(data._links["city:urban_area"].href)
                        let c = fetch(data._links["city:urban_area"].href)
                        .then(function(response){
                            return response.json()
                        })
                        .then(function(data){
                            prg.scores = data._links["ua:scores"].href
                            
                            for (item in data){
                                prg.dataBody = data['mayor']
                            }
                            let tempImg = fetch(data._links["ua:images"].href)
                            .then(function(response){
                                return response.json()
                            })
                            .then(function(data){
                                
                                prg.urlImg = data.photos[0].image.web
                                let scrs = fetch(prg.scores)
                                .then(function(response){
                                    return response.json()
                                })
                                .then(function(data){
                                    
                                    prg.scoresObj = data

                                })
                            })
                        })
                        
                        
                    })


            })
            
            
            

        },

        updateThings: function(){
            this.city = ''
            this.dataBody =''
            this.lng=this.lat =''
            this.apiUrl= ''
            this.linkTo=''
            this.nicks= []
            this.urlImg= null
            this.scores= ''
            this.scoresObj= []
        },

        rounder: function(num){
            return Number.parseFloat(num).toFixed(2)
        }
        

    },
    created() {
        setTimeout(function(){
            prg.dumpsterFire = false
        }, 5000)
        
    },


})


