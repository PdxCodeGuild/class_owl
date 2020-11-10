let app = new Vue({
    el: "#app",
    delimiters: ['xxx','xxx'],
    data: {
        message: 'Hello World 😇🤬🥋',
        longURL: '',
        redirects: [],
    },
    methods: {
        getURLS: async function(){
            data = await axios.get("get_urls/")
            app.redirects = data.data.urls
        },
        postURLS: async function(){
            let token = document.getElementsByName('csrfmiddlewaretoken')[0]
            
            let config = {
                method: "POST",
                url: 'post_urls/',
                headers: {
                    'X-CSRFToken': token.value
                },
                data: {
                    URL: app.longURL
                },
                headers: {
                    'X-CSRFToken': token.value
                }
            }
            await axios(config)
            app.longURL = ''
            app.getURLS()

        }    
    },
    created: function(){
        this.getURLS()
    }
})