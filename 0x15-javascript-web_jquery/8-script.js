$(document).ready(() => {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    type: 'GET',
    dataType: 'json'
  })
    .done((json) => {
      json.results.forEach(elem => {
        $('UL#list_movies').append(`<li>${elem.title}</li>`);
      });
    });
});
