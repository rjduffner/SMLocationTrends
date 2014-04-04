$(document).ready(function(){
    $("#validate-api-data" ).click(function() {
        apiValidateData()
    });

    if ($.cookie('api_key') && $.cookie('access_token')) {
        $("#api-key-token-form").addClass('hide');
        $("#survey-id-form").removeClass('hide');
    }
});

var apiValidateData = function() {
    $.post( "/auth/",
            { "api_key": "Hello", "access_token": "Now" },
            function( data ) {
                $(".bd").html(data)
                console.log( data.hello ); // John
    }, "json");
}
