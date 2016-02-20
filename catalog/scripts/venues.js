$(function () {
  $('.deletelink').click(function(){
    var vid = $(this).attr('data-vid');
    $.loadmodal({
          url: '/catalog/deletevenue',
          id: 'deletemodal',
          title: 'WARNING',
          width: '700px',
          buttons: {'Delete': function() {
            window.location="/catalog/venues.delete/" + vid;
          }},
        });
  });// click
}); // ready

$(function () {
  $('#createvenuelink').click(function(){
    $.loadmodal({
          url: '/catalog/venues.create',
          id: 'createvenuemodal',
          title: 'Create New Venue',
          width: '700px',
        });
  });// click
}); // ready

$(function () {
  $('.editvenuelink').click(function(){
    var vid = $(this).attr('data-vid');
    $.loadmodal({
          url: '/catalog/venues.edit/' + vid,
          id: 'editvenuemodal',
          title: 'Edit Venue',
          width: '700px',
        });
  });// click
}); // ready
