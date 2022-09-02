const temp = document.querySelector("#temperature");
const feelsLike = document.querySelector("#feels-like")
const humidity = document.querySelector("#humidity");
const sunrise = document.querySelector("#sunrise");
const sunset = document.querySelector("#sunset");
const icon = document.querySelector("#icon");
const weatherDescription = document.querySelector("#weather-description");


navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.latitude);
    let lat = position.coords.latitude;
    console.log(position.coords.longitude);
    let lon = position.coords.longitude;

    fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&exclude=hourly,daily,minutely&appid=${apiKey}&units=imperial`).then(response => response.json()).then((data) => {
        temp.innerHTML = data.current.temp.toFixed() + "&deg;F";
        humidity.textContent = data.current.humidity + "%";
        feelsLike.innerHTML = "Feels like: " + data.current.feels_like + "&deg;F"
        let sunriseTimeStamp = new Date(data.current.sunrise * 1000);
        sunrise.textContent = String(sunriseTimeStamp.getHours()).padStart(2, "0") + ":" + String(sunriseTimeStamp.getMinutes()).padStart(2, "0");
        // sunrise.textContent = `Sunrise: ${sunriseTimeStamp.get} AM`;
        let sunsetTimeStamp = new Date(data.current.sunset * 1000);
        sunset.textContent = String(sunsetTimeStamp.getHours()).padStart(2, "0") + ":" + String(sunsetTimeStamp.getMinutes()).padStart(2, "0");
        weatherDescription.textContent = data.current.weather[0].description;
        icon.classList.add(`owf-${data.current.weather[0].id}`);

    });
});


// .then(function(response){return response.json()})
// is the same as .then(response => response.json())

