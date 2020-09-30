let app = new Vue({
    el: '#app',
    data:{
        toList: [],
        i: "",
        isFin: false
    },
    methods:{
        addItem: function(){
            
           let input = document.querySelector(".input")
           input = input.value 
           this.toList.push({
               i: this.i,  
               isFin: false
           })
           this.i = '' 
        },
        del: function(i){
            this.toList.splice(i, 1)
        },
        done: function(x){
            
            this.toList[x].isFin = !this.toList[x].isFin 

        },
        
    },
})


// v-bind:class="{color: T/F}"