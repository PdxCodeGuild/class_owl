let app = new Vue({
    el: '#app',
    data: {
        hours: null,
        minutes: null,
        seconds: null,
    },
    methods: {
        keeptime: function(){
            let interval = setInterval (function(){
                let counter = app.hours
                // this is the fast easy way to get a new date every second
                // let d = new Date()
                // app.hours = d.getHours
                // app.minutes = d.getMinutes
                // app.seconds = d.getSeconds
                app.seconds++
                if(app.seconds >=60){
                    app.seconds = 0
                    app.minutes++
                    if(app.minutes >= 60){
                        app.minutes = 0
                        if(app.hours >= 24){
                            app.hours = 00
                        }
                    }
                }
            },1000)
        }
    },
    created(){
        let d = new Date()
        this.hours = d.getHours()
        this.minutes = d.getMinutes()
        this.seconds = d.getSeconds()
        this.keeptime()
    }
})