/*Feet to Meters*/
function feetConverter(valNum) {
  valNum = parseFloat(valNum);
  document.getElementById("meters").innerHTML = (valNum) / 3.2808;
}
