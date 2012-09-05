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
        $("div#form").html(response);
    })
}
$(document).ready(function(){
    go_to_contact();
    $("#contact #form").css({display: "none"}); // Opera Fix
    $("#contact span").click(function(){
        $('#contact span').stop().css({height: "27px", background: "none"});
        $('#contact').stop().animate({
            width: "220px"
        }, 300,function() {
            $('#form').stop().css({
                visibility: "visible",
                display: "none"}
            ).slideDown(300);
        });
    });
});
