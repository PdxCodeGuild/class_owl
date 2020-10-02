let app = new Vue({
    el: '#app',
    data: {
        todos: [],
        todo: ''
    },
    methods: {
        addTodo: function(){
            let todo = {
                title: this.todo,
                editable: false,
                completed: false
            }
            this.todos.push(todo)
        },
        deleteTodo: function(i){
            this.todos.splice(i, 1)
        }
    }
})