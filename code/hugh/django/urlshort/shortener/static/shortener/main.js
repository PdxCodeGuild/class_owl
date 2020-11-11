let app = new Vue({
    el: '#app',
    delimiters: ['[[',']]'],
    data:{
        message: 'Hello World 🐱‍💻',
        longURL: ''
        },
    methods:{
        getURLS: async function(){
            data = await axios.get("get_urls/")
            console.log(data)
        },
        postURLS: async function(){

            let token = document.getElementsByName("csrfmiddlewaretoken")[0]

            let config = {
                method: 'POST',
                url: 'post_urls/',
                data: {
                    URL: app.longURL
                },
                headers: {
                    'X-CSRFToken': token.value
                }
            }

            let response = await axios(config)
            console.log(response)
        }
    }
})

