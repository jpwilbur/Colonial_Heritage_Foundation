$(function(){
    // bind form using ajaxForm
  $('#editvenueform').ajaxForm({
    // target identifies the element(s) to update with the server response
    target: '#jquery-loadmodal-js-body',
    });
});//ready

$(function () {
  $('.deletearealink').click(function(){
    var aid = $(this).attr('data-aid');
    $.loadmodal({
          url: '/catalog/deletearea',
          id: 'deletemodal',
          title: 'WARNING',
          width: '700px',
          buttons: {'Delete': function() {
            window.location="/catalog/venues.deletearea/" + aid;
          }},
        });
  });// click
}); // ready

$(function () {
  $('#createarealink').click(function(){
    $('editvenuemodal').modal('hide');
    var vid = $(this).attr('data-vid');
    $.loadmodal({
          url: '/catalog/venues.createarea/' + vid,
          id: 'createareamodal',
          title: 'Create New Area',
          width: '700px',
        });
  });// click
}); // ready

$(function () {
  $('.editarealink').click(function(){
    var aid = $(this).attr('data-aid');
    $.loadmodal({
          url: '/catalog/venues.editarea/' + aid,
          id: 'editareamodal',
          title: 'Edit Area',
          width: '700px',
        });
  });// click
}); // ready
