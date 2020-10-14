let app = new Vue({
    el: "#app",
    data:{
        firstName: '',
        lastName: '',
        description:'',
        subtitle:'',
        facebook:'',
        instagram:'',
        banner:''

        

    },
    methods:{
        getPlayer: async function(){
            let url = `https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p=${this.firstName}%20${this.lastName}`
           
           
            let response = await axios.get(url)
            console.log(response)  
        

            app.description = response.data.player[0].strDescriptionEN
            app.title = response.data.player[0].strPlayer
            app.subtitle = response.data.player[0].strTeam
            app.facebook = "https://" + response.data.player[0].strFacebook
            app.instagram = "https://www." + response.data.player[0].strInstagram
            app.banner= response.data.player[0].strBanner

            this.firstName = ''
            this.lastName = ''
        }

    }

})