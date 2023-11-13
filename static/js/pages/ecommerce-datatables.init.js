$(document).ready(function() {
    $('#myDataTable').DataTable({
        paging: true,
        searching: true,
        ordering: true,
        info: true,
        responsive: true,
        pageLength: 8 
    });
});
