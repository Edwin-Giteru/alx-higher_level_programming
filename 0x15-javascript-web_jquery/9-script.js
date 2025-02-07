$(document).ready(() => {
	$.ajax({
		type: 'GET',
		url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
		success: (data) => {
			$("#hello").text(data.hello);
		}
	});
});
