// JavaScript Document
var display = "";

function calcInput(inp) {
	display = document.getElementById("display");
	display value += inp;
	//alert(display);
}
function calculate() {
	display = document.getElementById("display");
	display.value = eval(display.value);
}
function clearDisplay() {
	//alert("Clear")
	display = document.getElementById("display");
	display.value = "";
}