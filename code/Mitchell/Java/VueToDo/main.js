let prg = new Vue({

    el: "#app",
    data: {
        total: 0
    },
    methods: {
        addTask: function(){
                let toDo = this.tasks
                if( this.userInput.length >0 && this.userInput.length <=50){
                    toDo.push(
                        {userInput: [this.userInput, true]}
                        )
                        console.log(toDo)
                        this.userInput =''
                    }
                else if( this.userInput.length >50) {
                    alert('Keep it short')
                    this.userInput = this.userInput.slice(0,52)
                }
        },
        remove: function(i){
            this.tasks.splice(i,1)
        },
        removeItem: function(i){
            this.completedTask.splice(i,1)
        },
        taskDone: function(i){
            let a = this.tasks.splice(i,1)
            console.log()
            this.completedTask.push(a[0]['userInput'][0])        
        },
        omit: function(){
            this.userInput = ''
            this.tasks =  []
            this.completedTask = []
        },      
    },
})