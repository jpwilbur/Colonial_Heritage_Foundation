$(function(){
    // bind form using ajaxForm
  $('#createproductform').ajaxForm({
    // target identifies the element(s) to update with the server response
    target: '#jquery-loadmodal-js-body',
    });
    $('#creationDate').closest('tr').addClass('hidden');
    $('#customizationNotes').closest('tr').addClass('hidden');
    $('#currentBulkPrice').closest('tr').addClass('hidden');
    $('#quantityAvailable').closest('tr').addClass('hidden');
    $('#currentRentalRate').closest('tr').addClass('hidden');
    $('#available').closest('tr').addClass('hidden');
});//ready

$(function () {
  $('#id_productType').change(function(){
    if ($(this).val() == "indproduct") {
      $('#creationDate').closest('tr').removeClass('hidden');
      $('#customizationNotes').closest('tr').removeClass('hidden');
      $('#currentBulkPrice').closest('tr').addClass('hidden');
      $('#quantityAvailable').closest('tr').addClass('hidden');
      $('#currentRentalRate').closest('tr').addClass('hidden');
      $('#available').closest('tr').addClass('hidden');
    } else if ($(this).val() == "bulkproduct") {
      $('#creationDate').closest('tr').addClass('hidden');
      $('#customizationNotes').closest('tr').addClass('hidden');
      $('#currentBulkPrice').closest('tr').removeClass('hidden');
      $('#quantityAvailable').closest('tr').removeClass('hidden');
      $('#currentRentalRate').closest('tr').addClass('hidden');
      $('#available').closest('tr').addClass('hidden');
    } else if ($(this).val() == "rentalproduct") {
      $('#creationDate').closest('tr').addClass('hidden');
      $('#customizationNotes').closest('tr').addClass('hidden');
      $('#currentBulkPrice').closest('tr').addClass('hidden');
      $('#quantityAvailable').closest('tr').addClass('hidden');
      $('#currentRentalRate').closest('tr').removeClass('hidden');
      $('#available').closest('tr').removeClass('hidden');
    } else if ($(this).val() == "") {
      $('#creationDate').closest('tr').addClass('hidden');
      $('#customizationNotes').closest('tr').addClass('hidden');
      $('#currentBulkPrice').closest('tr').addClass('hidden');
      $('#quantityAvailable').closest('tr').addClass('hidden');
      $('#currentRentalRate').closest('tr').addClass('hidden');
      $('#available').closest('tr').addClass('hidden');
    }
  });// click
}); // ready
