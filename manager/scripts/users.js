$(function () {
  $('.deletelink').click(function(){
    var pid = $(this).attr('data-pid');
    $.loadmodal({
          url: '/manager/deleteuser',
          id: 'deletemodal',
          title: 'WARNING',
          width: '700px',
          buttons: {'Delete': function() {
            window.location="/manager/users.delete/" + pid;
          }},
        });
  });// click
}); // ready

$(function () {
  $('#createuserlink').click(function(){
    $.loadmodal({
          url: '/manager/users.create',
          id: 'createusermodal',
          title: 'Create New User',
          width: '700px',
        });
  });// click
}); // ready

$(function () {
  $('.edituserlink').click(function(){
    var pid = $(this).attr('data-pid');
    $.loadmodal({
          url: '/manager/users.edit/' + pid,
          id: 'editusermodal',
          title: 'Edit User',
          width: '700px',          
        });
  });// click
}); // ready
