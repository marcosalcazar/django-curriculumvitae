function go_to_contact(post){
    if (post==undefined){
        var method = 'GET';
    } else {
        var method = 'POST';
    }
    $.ajax('/contact/', {
        type: method,
        data: $("#submitform").serializeArray(),
    }).done(function(response) {
        $("#contact_container").html(response);
    })
}
$(document).ready(function(){
    go_to_contact();
});
