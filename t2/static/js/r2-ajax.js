$(document).ready(function() {

$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/r2/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});

$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/r2/suggest_category/', {suggestion: query}, function(data){
         $('#cats').html(data);
        });
    });

$('#AddPage').click(function(){
        var page_item;
        page_item = $(this).val();
        //$.get('/r2/suggest_category/', {suggestion: page_item}, function(data){
         //$('#cats').html(data);
         $('#AddPage').hide();
       //});
    });  
    
    
    
    
});