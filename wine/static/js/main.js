$(document).ready(function(){
  alert("hello welcome")
    $("#driver").click(function(event){
        $.ajax({
            type:'GET',
            url:'/get-list/',
            success:function(response){
              console.log(response);
              if (1 == response.status) {
                  $('#load_data').html(response.html);
              }
            }
        });
    });

    function allCars(){
        $.ajax({
            type:'GET',
            url:'/get-list/',
            success:function(response){
              console.log(response);
              if (1 == response.status) {
                  $('#load_data').html(response.html);
              }
            }
        });

    }

    $("#add_car").click(function(event){
      event.preventDefault();
      $.ajax({
        type:'GET',
        url:$(this).attr('href'),
        success:function(response){
          console.log(response);
          $('#load_data').html(response.html);
          $("#cars").validate({
            rules:{
              name:{
                  required:true
                },
              image:{
                  required:true
                }
            },
              message:{
                name :"required field",
                image:"required field"
      }
    });          
        }
      });
    });



});
