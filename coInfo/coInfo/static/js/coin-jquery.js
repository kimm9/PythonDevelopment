$(document).ready(function() {

console.log("hey jquery")


$('#likes').click(function(){ var catid;
    catid = $(this).attr("data-catid");
    $.get('/coin/like/', {category_id: catid}, function(data){
            $('#like_count').html(data);
                $('#likes').hide();
    }); 
  });


});