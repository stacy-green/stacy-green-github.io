// const btn1 = document.querySelector(".rock")
// const btn2 = document.querySelector(".paper")
// const btn3 = document.querySelector(".scissors")

// btn1.addEventListener("click", someFunction)
// btn2.addEventListener("click", someFunction)
// btn3.addEventListener("click", someFunction)

// console.log(btn1, btn2, btn3)
// console.log(buttons)

// for (button of buttons) {
//     button.addEventListener("click", function () {
//         console.log(btn.className);
//     })
// };


// Option 2
const buttons = document.querySelectorAll(".btn");

buttons.forEach(function(button) {
    button.addEventListener("click", function() {
        rps(button.classList[1]);
    })
});

function rps(player) {
    const choices = ["rock", "paper", "scissors"];
    const opponent = choices[Math.floor(Math.random() * 3)];
    const wins = ["rockscissors", "paperrock", "scissorspaper"];

    console.log(player, opponent);
        
    let p = document.createElement("p");
    p.classList.add("result");
    if(player === opponent) {
            p.innerText = (`You chose ${player}. Opponent chose ${opponent}. You tie.`);
            p.classList.add("tie");
    } else if (wins.includes(player+opponent)) {
        p.innerText = (`You chose ${player}. Opponent chose ${opponent}. You win!`);
        p.classList.add("win");
    } else {
        p.innerText = (`You chose ${player}. Opponent chose ${opponent}. You lose...`);
        p.classList.add("lose");
    };
    document.querySelector("#gamelog").prepend(p)
};

