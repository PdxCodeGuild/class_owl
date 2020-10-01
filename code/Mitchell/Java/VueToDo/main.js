let app = new Vue({
    el: '#app',
    data: {
        message: '',
        TuDoList: [],
        
    },
    methods: {
        addtask: function() {
            let todo = this.message
            this.TuDoList.push({
                task: todo,
                completed: false
            })

        },
        deleteTask: function(i) {
            this.TuDoList.splice(i, 1)

        },
    }
})
