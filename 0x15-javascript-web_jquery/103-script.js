$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/?lang=${lang}`,
      type: 'GET',
      dataType: 'json'
    })
      .done((json) => {
        $('DIV#hello').text(`${json.hello}`);
      });
  });
  $('INPUT#language_code').keypress((e) => {
    if (e.which === 13) {
      const lang = $('INPUT#language_code').val();
      $.ajax({
        url: `https://www.fourtonfish.com/hellosalut/?lang=${lang}`,
        type: 'GET',
        dataType: 'json'
      })
        .done((json) => {
          $('DIV#hello').text(`${json.hello}`);
        });
    }
  });
});
