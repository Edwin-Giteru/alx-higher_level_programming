$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').val();
    parameters = {
      lang: code
    };
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/' + '?' + $.param(parameters),
      success: (data) => {
        $('#hello').append('<p>' + data.hello + '</p>');
      }
    });
  });
});
