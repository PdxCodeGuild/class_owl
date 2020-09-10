let scoreboard = {
    wins: 0,
    loses: 0,
    ties: 0
}


function RPS(choice){
    let cpuChoices = ['rock', 'paper', 'scissors']
    let index = Math.round(Math.random() * 2)

    let cpu = cpuChoices[index]

    let result
    
    if (choice === cpu){
        result = '<h1>It is a tie!</h1>'
        scoreboard.ties++
    } else if ( choice === "rock" && cpu === "scissors" ) {
        result = '<h1> You win! </h1>'
        scoreboard.wins++
    } else if ( choice === "rock" && cpu === "paper" ) {
        result = '<h1> You lose! :( </h1>'
        scoreboard.loses++
    } else if ( choice === "paper" && cpu === "rock" ) {
        result = '<h1> You win! </h1>'
        scoreboard.wins++
    } else if ( choice === "paper" && cpu === "scissors" ) {
        result = '<h1> You lose! :( </h1>'
        scoreboard.loses++
    } else if ( choice === "scissors" && cpu === "paper" ) {
        result = '<h1> You win! </h1>'
        scoreboard.wins++
    } else if ( choice === "scissors" && cpu === "rock" ) {
        result = '<h1> You lose! :( </h1>'
        scoreboard.loses++
    }

    let print = document.getElementById('outcome')
    print.innerHTML = result
    
    table = `<table class="table">
                <tr>
                    <th>Wins</th>
                    <th>Loses</th>
                    <th>Ties</th>
                </tr>
                <tr>
                    <td>${scoreboard.wins}</td>
                    <td>${scoreboard.loses}</td>
                    <td>${scoreboard.ties}</td>
                </tr>
            </table>`

    let sb = document.getElementById('scoreboard')
    sb.innerHTML = table
}