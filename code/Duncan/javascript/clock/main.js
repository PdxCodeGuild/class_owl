let clock = document.querySelector("#clock")
let watch = new timer()






// function myclock(){
    let today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();

    m = add0(m);
    s = add0(s);

    clock.innerText = h + ":" + m + ":" + s ;

    let time = setTimeout(startTime, 500);

// }

function add0(i){
    if (i < 10) {i = "0" + i};
    return i;
}

function timer(){
    let time = 0;
    var interval; 
    var offset;

    function update() {
        time += delta();
        let formattedTime = timeForm(time);
    }
    function delta() {
        let now = Date.now()
        let timePassed = now - offset;
        offset = now;
        return timePassed
    }
    function timeForm(timeInMilliseconds) {
        let time = new Date(timeInMilliseconds);
        let minutes = time.getMinutes();
        let seconds = time.getSeconds();
        let milliseconds = time.getMilliseconds();

        minutes = add0(minutes)
        seconds = add0(seconds)

        return minutes + ":" + seconds + "." + milliseconds;
    }



    this.isOn = false;

    this.start = function() {
        if (!this.isOn) {
            interval = setInterval(update, 10);
            offset = Date.now();
            this.isOn = true;
        }
    };
    this.stop = function() {
        if(this.isOn) {
            clearInterval(interval);
            interval = null;
            this.isOn = false;
        }
    };
    this.reset = function() {};

}

