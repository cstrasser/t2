$(document).ready(function() {

      
    $("p").hover( function() {
     $(this).css('color', 'red');},
     function() {  $(this).css('color', 'blue'); });

    $("#about-btn").click( function(event){
    msgstr =$("#msg").html()
    msgstr = msgstr + "o"
        $("#msg").html(msgstr)       
    });
    
});