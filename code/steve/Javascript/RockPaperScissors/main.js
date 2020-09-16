

// scoreboard array
let scoreboard = {
    wins: 0,
    loses: 0,
    ties: 0
}


function RPS(choice){
    // cpu list
    let cpuChoices = ['rock', 'paper', 'scissors']
    // random choice on list index
    let index = Math.floor(Math.random() * 3)
    // store the cpu choice
    let cpu = cpuChoices[index]

    // we keep result undefined so that it can equal the end condition
    let result 
    

    //logic for win, lose and tie
    if (choice === cpu){
        result = '<h1>It is a Tie!</h1>'
        scoreboard.ties++
    } else if (choice === "rock" && cpu ==="scissors") {
        result = '<h1> You Win! </h1>'
        scoreboard.wins++
    } else if (choice === "rock" && cpu ==="paper") {
        result = '<h1> You Lose! </h1>'
        scoreboard.loses++
    } else if (choice === "paper" && cpu ==="scissors") {
        result = '<h1> You Lose! </h1>'
        scoreboard.loses++
    } else if (choice === "paper" && cpu ==="rock") {
        result = '<h1> You Win! </h1>'
        scoreboard.wins++
    } else if (choice === "scissors" && cpu ==="paper") {
        result = '<h1> You Win! </h1>'
        scoreboard.wins++
    } else if (choice === "scissors" && cpu ==="rock") {
        result = '<h1> You Lose! </h1>'
        scoreboard.loses++
    }

    


    let print = document.getElementById('outcome')
    print.innerHTML = result





    table = `<table>
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