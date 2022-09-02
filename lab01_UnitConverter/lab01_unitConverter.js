// Lab 1: JavaScript Redo

const unitConversions = {
    ft: "0.3048",
    mi: "1609.34",
    m: "1",      
    km: "1000",
    yd: "0.9144",
    in: "0.0254"  
}

//////////////// Version 1 ////////////////

// let inputNumber = Number(prompt("Enter meausurement \n\t> "))
// // console.log(inputNumber)
// let inputUnit = prompt("Enter input unit \n\t> ")
// // console.log(inputUnit)
// let outputUnit = prompt("Enter output unit \n\t> ")
// // console.log(outputUnit)
// let measurementInMeters = inputNumber * unitConversions[inputUnit]
// // console.log(measurementInMeters)
// let outputNumber = measurementInMeters / unitConversions[outputUnit]
// // console.log(outputNumber)
// alert(`${inputNumber} ${inputUnit} is ${outputNumber} ${outputUnit}`)


//////////////// Version 2 ////////////////

let inputNumber = document.querySelector('#inputNumber');
let inputUnit = document.querySelector('#inputUnit');
let outputUnit = document.querySelector('#outputUnit');
let run_bt = document.querySelector('#run_bt');
let output_div = document.querySelector('#output_div');
run_bt.onclick = function() {
    let inputNumberValue = Number(inputNumber.value);
    let inputUnitValue = inputUnit.value;
    let outputUnitValue = outputUnit.value
    let measurementInMeters = inputNumberValue * unitConversions[inputUnitValue]
    let convertedNumber = measurementInMeters / unitConversions[outputUnitValue]
    output_div.innerText = inputNumberValue + ' ' + inputUnitValue + ' is ' + convertedNumber + ' ' + outputUnitValue;
}