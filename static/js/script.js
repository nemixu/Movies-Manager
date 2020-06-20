$(document).ready(function () {
	flashed_messages();
});


function flashed_messages() {
	let messages = parseInt($("#messages p").length);
	if (messages) {
		$("#alerts").slideDown(650);
		setTimeout(() => {
			$("#alerts").slideUp(650);
		}, 5000);
	}
}
