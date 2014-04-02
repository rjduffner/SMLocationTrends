$(document).ready(function(){
    $("#validate-api-data" ).click(function() {
        apiValidateData()
    });
});

var apiValidateData = function() {
    $.post( "/auth/", { "api_key": "Hello", "access_token": "Now" }, function( data ) {
        console.log( data.hello ); // John
    }, "json");
}
