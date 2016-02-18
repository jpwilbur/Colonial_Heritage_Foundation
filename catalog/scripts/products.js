$(function () {
  $('.deletelink').click(function(){
    var pid = $(this).attr('data-pid');
    $.loadmodal({
          url: '/catalog/deleteproduct',
          id: 'deletemodal',
          title: 'WARNING',
          width: '700px',
          buttons: {'Delete': function() {
            window.location="/catalog/products.delete/" + pid;
          }},
        });
  });// click
}); // ready

$(function () {
  $('#createproductlink').click(function(){
    $.loadmodal({
          url: '/catalog/products.create',
          id: 'createproductmodal',
          title: 'Create New Product',
          width: '700px',
        });
  });// click
}); // ready

$(function () {
  $('.editproductlink').click(function(){
    var pid = $(this).attr('data-pid');
    var ptype = $(this).attr('data-ptype');
    $.loadmodal({
          url: '/catalog/products.edit/' + pid + '/' + ptype,
          id: 'editproductmodal',
          title: 'Edit Product',
          width: '700px',
        });
  });// click
}); // ready
