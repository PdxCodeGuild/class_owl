let app = new Vue({
    el: '#app',
    data: {
        message: '',
        toDoList: [],
    },
    methods: {
        addToDo: function () {
            let todo=this.message
            this.toDoList.push({
                task:todo,
                completed:false
            })
        },
        deletetask: function(i) {
            this.toDoList.splice(i,1)
        },
        completetask: function(i) {
            this.toDoList
        }
    }
})