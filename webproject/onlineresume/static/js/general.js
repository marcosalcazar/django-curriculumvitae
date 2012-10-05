function go_to_contact_ajax(method){
    $.ajax('/contact/', {
        type: method,
        data: $("#submitform").serializeArray(),
    }).done(function(response) {
        $("#contact_container").html(response);
    })
}
function go_to_contact(post){
    if (post==undefined){
        var method = 'GET';
        go_to_contact_ajax(method);
    } else {
        var method = 'POST';
        $("#submitform").fadeOut('fast', function(){
            $("#submitloading").fadeIn('fast', function(){
                go_to_contact_ajax(method);
            });
        })
    }
}
$(document).ready(function(){
    go_to_contact();
});
