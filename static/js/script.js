

let startX;
let startY;

let endX;
let endY;
let ran = false;



const left = document.getElementById('left')
const right = document.getElementById('right')
const track = document.getElementById('track')


function send(){
let width=track.clientWidth;
fetch("/cords", {
		method:"POST",
		headers :{"Content-Type":"application/json"},
		body:JSON.stringify({cordinates : width})
	})
}

window.onload = send;

track.addEventListener("touchstart",e => {
	e.preventDefault();
	startX = e.targetTouches[0].clientX
	startY = e.targetTouches[0].clientY
	// console.log("start",e.targetTouches[0].clientX,e.targetTouches[0].clientY);
})
track.addEventListener("touchmove",e => {
	e.preventDefault();

	endX = startX - e.changedTouches[0].clientX;
	endY = startY - e.changedTouches[0].clientY;
	startX = e.changedTouches[0].clientX;
	startY = e.changedTouches[0].clientY;

	data = "move,"+endX+","+endY+"\n"

	fetch("/cords", {
		method:"POST",
		headers :{"Content-Type":"application/json"},
		body:JSON.stringify({cordinates : data})
	})

	// console.log("(",endX, ",", endY, ")")
	// console.log("move",e.changedTouches[0].clientX,e.changedTouches[0].clientY);
})
track.addEventListener("touchend",e => {
	e.preventDefault();
	endX = startX - e.changedTouches[0].clientX;
	endY = startY - e.changedTouches[0].clientY;
	startX = e.changedTouches[0].clientX;
	startY = e.changedTouches[0].clientY;
	// console.log("(",endX, ",", endY, ")")
	// console.log("released",e.changedTouches[0].clientX,e.changedTouches[0].clientY);
})




left.addEventListener("touchstart",e => {
	e.preventDefault();
	// console.log("left click");
	data = "left,"+endX+","+endY+"\n"

	fetch("/cords", {
		method:"POST",
		headers :{"Content-Type":"application/json"},
		body:JSON.stringify({cordinates : data})
	})
})
left.addEventListener("touchend",e => {
	e.preventDefault();
})




right.addEventListener("touchstart",e => {
	e.preventDefault();
	data = "right,"+endX+","+endY+"\n"
	fetch("/cords", {
		method:"POST",
		headers :{"Content-Type":"application/json"},
		body:JSON.stringify({cordinates : data})
	})


	// console.log("right click");
})
right.addEventListener("touchend",e => {
	e.preventDefault();
	
})