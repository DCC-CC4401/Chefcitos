const form  = document.getElementById('form');
const nombreusuario = document.getElementById('Nombre');
const nombrespanError = document.getElementById('nombreError');
const apellidousuario = document.getElementById('Apellido');
const apellidospanError = document.getElementById('apellidoError');
const usernameusuario = document.getElementById("Username");
const usernamepanError = document.getElementById("usernameError");
const fechausuario = document.getElementById("Nacimiento");
const fechaspanError = document.getElementById("fechaError");
var usuarioregex = /([a-zA-Z ]){3,30}/;
var usernameregex = /([a-zA-Z0-9@.+_-]){3,150}/;

$(nombreusuario).change( function (){
    if (usuarioregex.test($(nombreusuario).val())){
        nombreusuario.classList.remove("invalid");
        nombrespanError.style.display = "none";
    } else {
        nombreError();
    }
})

$(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});

function nombreError() {
    nombreusuario.classList += " invalid";
    nombrespanError.style.display = "block";
};

$(apellidousuario).change( function (){
    if (usuarioregex.test($(apellidousuario).val())){
        apellidousuario.classList.remove("invalid");
        apellidospanError.style.display = "none";
    } else {
        apellidoError();
    }
})

function apellidoError() {
    apellidousuario.classList += " invalid";
    apellidospanError.style.display = "block";
};


$(usernameusuario).change( function (){
    if (usernameregex.test($(usernameusuario).val())){
        usernameusuario.classList.remove("invalid");
        usernamepanError.style.display = "none";
    } else {
        apodoError();
    }
})

function apodoError() {
    usernameusuario.classList += " invalid";
    usernamepanError.style.display = "block";
};

$(fechausuario).change( function (){
    if ($(fechausuario).val()){
        fechausuario.classList.remove("invalid");
        fechaspanError.style.display = "none";
    } else {
        fechaError();
    }
})

function fechaError() {
    fechausuario.classList += " invalid";
    fechaspanError.style.display = "block";
};


form.addEventListener('submit', function (event){
    var count = 0;
    if (nombreusuario.validity.valueMissing){
		nombreError();
		count++;
    }
    if (apellidousuario.validity.valueMissing){
		apellidoError();
		count++;
    }
    if (usernameusuario.validity.valueMissing){
		apodoError();
		count++;
    }
    if (!$(fechausuario).val()){
        fechaError();
        count++;
    }
	if (count>0){
		event.preventDefault();
	}
});