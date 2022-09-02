
const loginForm = document.querySelector("#login-form")
const username = document.querySelector("#username")
const password = document.querySelector("#password")
const csrfToken = Cookies.get("csrftoken")

loginForm.addEventListener("submit", function(event) {
    event.preventDefault()
    const data = {
        username: username.value,
        password: password.value
    }
    fetch("", {
        method: "POST", 
        body: JSON.stringify(data),
        headers: {
            'X-CSRFToken': csrfToken
        }
    }).then(response => response.json())
    .then(data => {
        if(data.message !== "Ok"){
            console.error(data.message)
        } else {
            window.location = "../"
        }
    })    
})
