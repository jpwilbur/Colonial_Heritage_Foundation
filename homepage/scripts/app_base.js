$(function () {
  $('#loginlink').click(function(){
    $.loadmodal({
          url: '/Account/login',
          id: 'loginmodal',
          title: 'Login to Colonial Heritage Foundation',
          width: '700px',
        });
  });// click
}); // ready
