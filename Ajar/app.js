var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
var x = 250;
var y = 250;

function drawUserCell() {
  context.fillStyle = "cyan";
  context.beginPath();
  context.arc(x, y, 70, 0, 2*3.14159);
  context.fill();
}
drawUserCell();

function mouseMoved(mouse) {
  x = mouse.clientX;
  y = mouse.clientY;
}
