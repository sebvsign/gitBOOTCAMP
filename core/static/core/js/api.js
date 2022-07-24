$(document).ready(
    function(){
        $.get("http://127.0.0.1:8000/api/sucursal/",
        function(data){
            $.each(data,function(i,item){
                $("#tabla").append("<tr><td>"+item.region+
                "</td><td>"+item.comuna+
                "</td><td>"+item.direccion+
                "</td><td><img src="+item.imagen+"</td></tr>");
            });
        });
    });