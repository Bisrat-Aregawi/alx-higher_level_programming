$(document).ready(() => {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    type: 'GET',
    dataType: 'json'
  }).done(function (json) {
    console.log(json.name);
    $('DIV#character').text(json.name);
  });
});
