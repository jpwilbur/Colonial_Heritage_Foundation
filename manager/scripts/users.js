$(function () {
  var pid = $(this).attr('data-pid');
  $('#deletelink').click(function(){
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

// '/manager/users.delete/'+ str(pid),
