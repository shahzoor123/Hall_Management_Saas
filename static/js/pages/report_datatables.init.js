$(document).ready(function () {
    $("#datatable").DataTable({
      paging: true, // Disable pagination
    });
  
    $("#datatable-buttons")
      .DataTable({
        lengthChange: !1,
        buttons: ["copy", "excel", "pdf", "colvis"],
        paging: true, // Disable pagination
      })
      .buttons()
      .container()
      .appendTo("#datatable-buttons_wrapper .col-md-6:eq(0)");
  
    $(".dataTables_length select").addClass("form-select form-select-sm");
  });
  