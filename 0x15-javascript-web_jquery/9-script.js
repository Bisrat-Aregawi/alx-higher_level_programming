$(document).ready(() => {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    dataType: 'json'
  })
    .done(json => {
      $('DIV#hello').text(`${json.hello}`);
    });
});
