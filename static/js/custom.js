function iniciarSesion(){
    var user = $('#user').val()
    var password = $('#password').val()
	$.ajax({
        url: "login",
        type: 'get',
        data: {user: user, password: password},
        success: function(response){
            var json = JSON.stringify(response['output']);
            var data = JSON.parse(json);
            if (!response.error) {
                var origin   = window.location.origin
                window.open(origin+'/home',"_self");
            } else {
                alert(data);
            }
            console.log(data)
		}
    });
}

function cerrarSesion(){
	$.ajax({
        url: "../../destroy_session",
        type: 'get',
        success: function(response){
            alert('¡Usted ha abandonado su sesión!');
             window.open(origin+'/',"_self");
		}
    });
}
