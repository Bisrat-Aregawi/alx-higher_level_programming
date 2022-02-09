$(document).ready(() => {
  $('DIV#update_header').css('cursor', 'pointer');
  $('DIV#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
