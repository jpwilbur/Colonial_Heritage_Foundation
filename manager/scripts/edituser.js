$(function(){
    // bind form using ajaxForm
  $('#edituserform').ajaxForm({
    // target identifies the element(s) to update with the server response
    target: '#jquery-loadmodal-js-body',
    });
});//ready

$(function () {
  $('#changepasswordlink').click(function(){
    var pid = $(this).attr('data-pid');
    $.loadmodal({
          url: '/manager/users.changepassword/' + pid,
          id: 'changepasswordmodal',
          title: 'Change User Password',
          width: '700px',
        });
  });// click
}); // ready
