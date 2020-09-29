


let prg = new Vue({

    el: "#prg",
    data:{
        apiUrl: 'https://api.teleport.org/api/cities/',
        city: '',
        linkTo:'',
        dataBody: ""


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
            .then(function(data){
                // console.log(data)
                // console.log(data._embedded["city:search-results"][0].matching_full_name)
                prg.city = data._embedded["city:search-results"][0].matching_full_name
                prg.linkTo = data._embedded["city:search-results"][0]._links["city:item"].href
                
                // console.log(prg.linkTo)
                
                let b = fetch(prg.linkTo)
                .then(function(response){
                    return response.json()
                })
                .then(function(data){
                    console.log(data.location.latlon.latitude)
                    // console.log(data._links["city:urban_area"].href)
                    let c = fetch(data._links["city:urban_area"].href)
                    .then(function(response){
                        return response.json()
                    })
                    .then(function(data){
                        // console.log(data)

                        for (item in data){
                            prg.dataBody = data['mayor']
                            // console.log(item, data[item])
                        }

                    })
                
                
                })


            })
            

        },

        updateThings(){
            this.city = ''
            this.dataBody =''


        }


    }


})




