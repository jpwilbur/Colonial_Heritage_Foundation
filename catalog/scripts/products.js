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

$(document).ready(function(){

	$(document).on('click', '#updateQty', function (event) {
		var btn = $(this);
		var btnId = $( this ).attr('data-di') ;
		var urlSend = "/catalog/ajax/"+btnId+"/";
		$(".quantityAvailable"+btnId).load(urlSend);
		$.ajax({
			type : "GET",
			url : urlSend,
			success : function(data) {
					$(".quantityAvailable"+btnId).html(data[0]);
			},
		});
		console.log(urlSend);
		return false;
	});

});
