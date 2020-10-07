let app = new Vue({
    el: '#app',
    data: {
        
        numbers: ""
    },
    methods:{
        
        nums(a){
            let button = document.querySelector("#button")
            this.numbers += a 
            
           
            console.log(numbers)
        }
    },
})