 $(function () {
    var productType = $('#editProductTable').attr('data-ptype');
    console.log(productType);
    // var table = $('#editproductform').children()[0];
    $(function () {
      if ($('#editProductTable').attr('data-ptype') == "indproduct") {
        $('#creationDate').closest('tr').removeClass('hidden');
        $('#customizationNotes').closest('tr').removeClass('hidden');
        $('#currentBulkPrice').closest('tr').addClass('hidden');
        $('#quantityAvailable').closest('tr').addClass('hidden');
        $('#currentRentalRate').closest('tr').addClass('hidden');
        $('#available').closest('tr').addClass('hidden');
      } else if ($('#editProductTable').attr('data-ptype') == "bulkproduct") {
        $('#creationDate').closest('tr').addClass('hidden');
        $('#customizationNotes').closest('tr').addClass('hidden');
        $('#currentBulkPrice').closest('tr').removeClass('hidden');
        $('#quantityAvailable').closest('tr').removeClass('hidden');
        $('#currentRentalRate').closest('tr').addClass('hidden');
        $('#available').closest('tr').addClass('hidden');
      } else if ($('#editProductTable').attr('data-ptype') == "rentalproduct") {
        $('#creationDate').closest('tr').addClass('hidden');
        $('#customizationNotes').closest('tr').addClass('hidden');
        $('#currentBulkPrice').closest('tr').addClass('hidden');
        $('#quantityAvailable').closest('tr').addClass('hidden');
        $('#currentRentalRate').closest('tr').removeClass('hidden');
        $('#available').closest('tr').removeClass('hidden');
      }
      else {
        console.log('it didnt work')
      }
    });
 }); // ready
