let app = new Vue({
    el: '#app',
    data: {
        clock: true,
        stopWatch: false,
        hours: 0,
        minutes: 0,
        seconds: 0,
        meridies: 'am',
        stopHour: 0,
        stopMinute: 0,
        stopSecond: 0,
        stopMili: 0,
        swInterval: null,
        lapTimes: [],
    },
    methods: {
        showClock: function(){
            this.clock = true
            this.stopWatch = false
        },
        showStopWatch: function(){
            this.clock = false
            this.stopWatch = true
        },
        keepTime: function(){
            let interval = setInterval(function(){
                let counter = app.hours
                // let d = new Date()
                // app.hours = d.getHours() % 12
                // app.minutes = d.getMinutes()
                // app.seconds = d.getSeconds()

                app.hours > 11 ? app.meridies = 'pm' : app.meridies = 'am'

                app.seconds++
                if(app.seconds >= 60){
                    app.seconds = 0
                    app.minutes++
                    if(app.minutes >= 60){
                        app.minutes = 0
                        app.hours++
                        app.hours > 23 ? app.hours = 0 : ''
                    }
                }
            },1000)
        },
        padStart: function(number){
            return number.toString().padStart(2, '0')
        },
        startStopWatch: function(){
            if(this.swInterval) return


            this.swInterval = setInterval(function() {
                app.stopMili += 100
                if(app.stopMili > 999){
                    app.stopMili = 0
                    app.stopSecond++
                }
                
            }, 100)
        },
        stopTimer: function(){
            clearInterval(this.swInterval)
            this.swInterval = null
        },
        lapStopWatch: function(){
            let time = {
                hours: this.stopHour,
                minutes: this.stopMinute,
                seconds: this.stopSecond,
                milliseconds: this.stopMili 
            }
            this.lapTimes.push(time)
        },
        resetStopWatch: function(){
            this.stopHour = 0
            this.stopMinute = 0
            this.stopSecond = 0
            this.stopMili = 0
            this.lapTimes = []
            clearInterval(this.swInterval)
            this.swInterval = null
        }
    },
    created(){
        let d = new Date()
        this.hours = d.getHours()
        this.minutes = d.getMinutes()
        this.seconds = d.getSeconds()
        this.keepTime()
    }
})