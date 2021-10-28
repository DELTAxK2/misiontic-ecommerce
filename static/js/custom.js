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

function cbxAnalyze(id){
    var componentes = $('.selected');
    id_sel = 'chxSeleccion_' + id;
    if (componentes.length > 0) {
        for (var i = 0; i < componentes.length; i++) {
            var id_des = componentes[i].id
            if (id_des != id_sel) {
                 $('#'+id_des).prop('checked', false);
            } else {
                let valor = id_sel.split("_");
                $('#data_sel').val(valor[1]);
                $('#row_sel').val(i);
            }
        }
    }
}

function getPostComponentes(form_name){
     let form = $('#'+form_name)[0]
     var data = new  FormData()
     for (var i = 0; i < form.length; i++) {
         id = form[i].id;
         if(id != 'csrf_token') {
             value = $('#'+id).val()
             data.append(id, value)
         }
     }
     return data
}

function cleanComponentes(form_name){
     let form = $('#'+form_name)[0]
     for (var i = 0; i < form.length; i++) {
         id = form[i].id;
         if(id != 'csrf_token') {
             $('#'+id).val('');
         }
     }
}

function search(){
    let vista = $('#hdnView').val();
    let view = '../'+vista+'/get';
    let id = $('#data_sel').val();
	$.ajax({
        url: view,
        type: 'get',
        data: {id: id},
        success: function(response){
            var json = JSON.stringify(response['output']);
            var data = JSON.parse(json);
            if (!response.error) {
                console.log(data);
                let formulario = 'form_'+vista;
                switch(vista){
                    case 'usuarios':
                        $('#id').val(data[0]);
                        $('#tipo_id').val(data[1]);
                        $('#identificacion').val(data[2]);
                        $('#nombre1').val(data[3]);
                        $('#nombre2').val(data[4]);
                        $('#apellido1').val(data[5]);
                        $('#apellido2').val(data[6]);
                        $('#email').val(data[7]);
                        $('#telefono').val(data[8]);
                        $('#celular').val(data[9]);
                        $('#direccion').val(data[10]);
                        $('#id_rol').val(data[11]);
                        break;
                    case 'compras':
                        break;
                    case 'ventas':
                        break;
                    case 'proveedores':
                        break;
                    case 'productos':
                        break;
                }
            } else {
                alert(data);
            }
		}
    });
}
function save(){
    let vista = $('#hdnView').val();
    let view = '../'+vista+'/save';
    let form_name = 'form_'+vista;
    let formData = this.getPostComponentes(form_name);
     $.ajax({
         url: view,
         type: 'POST',
         dataType: 'json',
         data:formData,
         cache:false,
         processData: false,
         contentType: false,
         beforeSend: function() {
         }
     })
     .done(function(respuesta) {
        var json = JSON.stringify(respuesta['output']);
        var data = JSON.parse(json);
        if (!respuesta.error) {
            alert(data);
            cleanComponentes(form_name)
        }else{
            alert(data);
        }
     })
     .fail(function(resp) {
         alert('error del sistema, contacte al administrador');
     })
     .always(function() {
         console.log("complete");
     });
}
function update(){
    let vista = $('#hdnView').val();
    let view = '../'+vista+'/update';
    let form_name = 'form_'+vista;
    let formData = this.getPostComponentes(form_name);
     $.ajax({
         url: view,
         type: 'PUT',
         dataType: 'json',
         data:formData,
         cache:false,
         processData: false,
         contentType: false,
         beforeSend: function() {
         }
     })
     .done(function(respuesta) {
        var json = JSON.stringify(respuesta['output']);
        var data = JSON.parse(json);
        if (!respuesta.error) {
            alert(data);
            cleanComponentes(form_name)
        }else{
            alert(data);
        }
     })
     .fail(function(resp) {
         alert('error del sistema, contacte al administrador');
     })
     .always(function() {
         console.log("complete");
     });
}
function inactive(){
    let vista = $('#hdnView').val();
    let view = '../'+vista+'/save';
    let form_name = 'form_'+vista;
    let formData = this.getPostComponentes(form_name);
     $.ajax({
         url: view,
         type: 'DELETE',
         dataType: 'json',
         data:formData,
         cache:false,
         processData: false,
         contentType: false,
         beforeSend: function() {
         }
     })
     .done(function(respuesta) {
        var json = JSON.stringify(respuesta['output']);
        var data = JSON.parse(json);
        if (!respuesta.error) {
            alert(data);
            cleanComponentes(form_name)
        }else{
            alert(data);
        }
     })
     .fail(function(resp) {
         alert('error del sistema, contacte al administrador');
     })
     .always(function() {
         console.log("complete");
     });
}