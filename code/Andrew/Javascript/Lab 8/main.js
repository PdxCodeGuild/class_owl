


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
        urlImg: null
    },
    methods:{
        getResp(){
            this.apiUrl= 'https://api.teleport.org/api/cities/'
            this.apiUrl += this.city?  `?search=${encodeURIComponent(this.city)}`: `?search=portland` 
            // console.log(this.apiUrl)

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
                
                    // console.log(prg.nicks)                    
                    // console.log(data)
                    prg.city = data._embedded["city:search-results"][0].matching_full_name
                    prg.linkTo = data._embedded["city:search-results"][0]._links["city:item"].href
                    
                    // console.log(prg.linkTo)
                    
                    let b = fetch(prg.linkTo)
                    .then(function(response){
                        return response.json()
                    })
                    .then(function(data){
                        console.log(data.location.latlon.latitude)
                        prg.lng = data.location.latlon.longitude
                        prg.lat = data.location.latlon.latitude
                        // console.log(data._links["city:urban_area"].href)
                        let c = fetch(data._links["city:urban_area"].href)
                        .then(function(response){
                            return response.json()
                        })
                        .then(function(data){
                            console.log(data)
                            
                            for (item in data){
                                prg.dataBody = data['mayor']
                                // console.log(item, data[item])
                            }
                            let tempImg = fetch(data._links["ua:images"].href)
                            .then(function(response){
                                return response.json()
                            })
                            .then(function(data){
                                console.log(data)
                                this.urlImg = data.photos[0].image.web
                                console.log(urlImg)
                            })
                        })
                        
                        
                    })


            })
            

        },

        updateThings(){
            this.city = ''
            this.dataBody =''
            this.lng=this.lat =''

        }


    }


})


// Vue.component('apiImg', {
//     data: function () {
//       return {
//         imgSrc: app.urlImg
//       }
//     },
//     template: '<img src="imgSrc">'
//   })

// let tester = new Vue({ el: '#imgtest' })

