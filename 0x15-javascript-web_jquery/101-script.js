$(document).ready(() => {
  $('DIV#add_item, DIV#remove_item, DIV#clear_list')
    .css('cursor', 'pointer');

  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    $('UL.my_list > li:last-child').remove();
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list > li').remove();
  });
});
