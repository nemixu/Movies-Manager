$(document).ready(function () {
	flashed_messages();
});


function flashed_messages() {
	let messages = parseInt($("#messages p").length);
	if (messages) {
		$("#alerts").slideDown(1500);
		setTimeout(() => {
			$("#alerts").slideUp(1500);
		}, 7000);
	}
}
console.log('hello')