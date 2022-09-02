const snowmanImg = document.querySelector("#snowman-img")
const guessBtn = document.querySelector("#guess-btn")
const userInterface = document.querySelector("#user-interface")
const lettersDiv = document.querySelector("#letters-div")
const alphabet = Array.from("abcdefghijklmnopqrstuvwxyz")
const guessWord = document.querySelector("#guess-word")
guessBtn.textContent = "You sure?"
let guesses = 0

function gameOver(word) {
    guesses = 0
    const buttons = document.querySelectorAll("button")
    for (let button of buttons) {
        button.disabled = true
    }
    const spans = document.querySelectorAll("span")
    for (i = 0; i < word.length; i++) {
        spans[i].textContent = word[i]
    }
    setTimeout(function() {
        playSnowman()
        const buttons = document.querySelectorAll("button")
        for (let button of buttons) {
            button.disabled = false
        }
        lettersDiv.innerHTML = ""
        userInterface.innerHTML = ""
        snowmanImg.src = "https://www.hanginghyena.com/static/branding/art/Snowman-1.jpg"
        guessWord.value = ""
    }, 5000)
}

function playSnowman() {
    const randomLength = (Math.floor(Math.random() * 7)) + 6
    fetch(`https://random-word-api.herokuapp.com/word?length=${randomLength}`).then(response => response.json()).then(data => displayWord(data[0]))
}

function displayWord(word) {
    guessBtn.addEventListener("click", function() {
        if (guessWord.value === word) {
            snowmanImg.src = `https://www.hanginghyena.com/static/branding/art/Snowman-WIN.jpg`
            gameOver(word)
        } else {
            guesses += 1
            if (guesses === 10) {
                gameOver(word)
                snowmanImg.src = `https://www.hanginghyena.com/static/branding/art/Snowman-END.jpg`
            } else {
                snowmanImg.src = `https://www.hanginghyena.com/static/branding/art/Snowman-${guesses+1}.jpg`
            }
        }
    })
    console.log(word)
    for (let i=0; i < word.length; i++) {
        const letter = document.createElement("span")
        letter.textContent = " "
        letter.className = "letter" 
        lettersDiv.append(letter)
    }
    alphabet.forEach (function(letter) {
        const letterBtn = document.createElement("button")
        letterBtn.textContent = letter // is string????
        userInterface.append(letterBtn)
        letterBtn.addEventListener("click", () => 
            displayLetter(letter, word, letterBtn))
    })
}

function displayLetter(letter, word, button) {
    button.disabled = true
    if (word.includes(letter)) {
        for (let i = 0; i < word.length; i ++) {
            if (word[i] === letter) {
                lettersDiv.childNodes[i].textContent = letter 
            }
        }
        if (lettersDiv.textContent === word) {
            snowmanImg.src = `https://www.hanginghyena.com/static/branding/art/Snowman-WIN.jpg`
            gameOver(word)
        }
    } else {
        guesses += 1
        if (guesses === 10) {
            gameOver(word)
            snowmanImg.src = `https://www.hanginghyena.com/static/branding/art/Snowman-END.jpg`
        } else {
            snowmanImg.src = `https://www.hanginghyena.com/static/branding/art/Snowman-${guesses+1}.jpg`
        }
    }
}

playSnowman()

// # Snowman

// Let's write a program to play a game of [Snowman](https://en.wikipedia.org/wiki/Snowman_(game))! Snowman is a word game where a secret word is chosen, then players have to guess letters until they get the word correct or they run out of chances and lose.


// We can use [Axios](../docs/13%20-%20APIs%20and%20Ajax.md#ajax-in-axios) to send a request to this random word API.

// ```
// https://random-word-api.herokuapp.com/word/?swear=0
// ```

// Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in the word, show the blanks with the letters filled in. If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. Allow the user 10 tries to guess the letters of the word. If the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

// We could either have an input field and button for making a guess, or have a button for every letter and disable it after guessing.

// For images, [this page](https://www.hanginghyena.com/snowman) has a series of images that can be linked to.