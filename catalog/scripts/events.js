$(function () {
  $('.deletelink').click(function(){
    var eid = $(this).attr('data-eid');
    $.loadmodal({
          url: '/catalog/deleteevent',
          id: 'deletemodal',
          title: 'WARNING',
          width: '700px',
          buttons: {'Delete': function() {
            window.location="/catalog/events.delete/" + eid;
          }},
        });
  });// click
}); // ready

$(function () {
  $('#createeventlink').click(function(){
    $.loadmodal({
          url: '/catalog/events.create',
          id: 'createeventmodal',
          title: 'Create New Event',
          width: '700px',
        });
  });// click
}); // ready

$(function () {
  $('.editeventlink').click(function(){
    var eid = $(this).attr('data-eid');
    $.loadmodal({
          url: '/catalog/events.edit/' + eid,
          id: 'editeventmodal',
          title: 'Edit Event',
          width: '700px',
        });
  });// click
}); // ready
