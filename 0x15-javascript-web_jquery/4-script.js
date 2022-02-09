$(document).ready(() => {
  $('header').css('cursor', 'pointer');
  $('header').click(function () {
    if ($(this).hasClass('green')) {
      $(this).removeClass('green');
      $(this).addClass('red');
    } else {
      $(this).removeClass('red');
      $(this).addClass('green');
    }
  });
});
