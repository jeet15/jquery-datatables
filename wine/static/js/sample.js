$(document).ready(function(){
    allUsers();
    

    $("#back").css("background", "#99CCFF");

    setTimeout(function () {
        $("#back").css("background", "yellow");
    }, 2000);


    $("#btn1").click(function(){
        alert("This is the link"+ $("#ht1").attr("href"))
    });

    $("#btn2").click(function(){
        alert("This is the value "+ $("#txt").val())
    });

    $("#a1").click(function(event){
        event.preventDefault();
        alert("This is the preventDefault")
    });
    /*
    $("#form").validate({
        rules:{
            name:{
                required:true
            },
            email:{
                required:true
            }
        },
        message:{
            name:"required field",
            email:"required field"
        }
    });

     form fetching using ajax */

    $("#add_user").click(function(event){
        event.preventDefault();
        $.ajax({
            type:'GET',
            url:$(this).attr('href'),
            success:function(response){
                $('#load_form').html(response.html);
                userBind();
            }
        });
    });

    function userBind(){
        /* form validation code */
        $("#user_form").validate({
          rules:{
            name:{
              required:true
            },
            email:{
            required:true
            }
          },
          message:{
            name :"*",
            email:"*"
            },
            submitHandler:function(form){
                $.ajax({
                    url:form.action,
                    type:'POST',
                    data:$(form).serialize(),
                    success:function(response){
                        if (0 == response.status) {
                            $("#form_error").text(response.message).show();
                        }
                        else{
                            $("#id_name").val('');
                            $("#id_email").val('');
                            allUsers();
                            alert(response.message);

                        }
                    },
                });
            }
        });    
    }

    function allUsers(){
        $.ajax({
            type:'GET',
            url:'/all-user/',
            success:function(response){
                $("#load_form").html(response.html);
                if (1 == response.status){
                    table();
                    
                }
                else{
                    alert(response.message);
                }
                
            }
        });
    }

    function table(){
        $("#mytable").dataTable({
            'aaData':[
                {'ajax':'data.json'}
            ],
                   

            'aoColumns' : [
                { 'sTitle' : 'S.No.', 'bSortable': false, "sWidth": "5%" },
                { 'sTitle' : 'Name' },
                { 'sTitle' : 'Email' },
                { 'sTitle' : 'Username', "sWidth": "10%"}
            ],
            'iDisplayLength' : 5,            
                   });

    }

    function editUserData(){
        $(".edit_user").click(function(e){
            e.preventDefault();
            var $this = $(this), userId = $this.data('user-id');
            $.ajax({
                type:'GET',
                url:'/edit-user/',
                data: {user_id: userId},
                cache:false,
                success:function(response){
                    $('#load_form').html(response.html);
                    userBind();
                }
            });
        }); 
    }

    function deleteUser(){
        $(".delete_user").click(function(e) {
            e.preventDefault();
            var $this = $(this), userId = $this.data('user-id');
            if (confirm('Are you sure, You want to delete this user?')){
                $.ajax({
                    url: '/delete-user/',
                    type: 'get',
                    data: {user_id: userId},
                    success: function(response) {
                        if (response.status == 1) {
                            alert(response.message);
                            allUsers();
                        }
                        else{
                            alert(response.message);
                        }
                    }
                });
            }
        });
    }

    function bindUserActions(){
        editUserData();
        deleteUser();
    }
});