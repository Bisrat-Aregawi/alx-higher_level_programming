$(document).ready(() => {
  $('DIV#add_item').css('cursor', 'pointer');
  $('DIV#add_item').click(function () {
    const list_element = $('<li></li>').text('Item');
    $('UL.my_list').append(list_element);
  });
});
