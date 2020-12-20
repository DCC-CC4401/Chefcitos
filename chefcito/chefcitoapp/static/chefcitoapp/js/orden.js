function alphabetically() {
    document.getElementById("alphabet").className = document.getElementById("alphabet").className.replace( /(?:^|\s)d-none(?!\S)/g , '' );
    if (!document.getElementById("default").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("default").className += " d-none";
    }
    if (!document.getElementById("downalphabet").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("downalphabet").className += " d-none";
    }
    if (!document.getElementById("date").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("date").className += " d-none";
    }
    if (!document.getElementById("downdate").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("downdate").className += " d-none";
    }
}
function date() {
    document.getElementById("date").className = document.getElementById("date").className.replace( /(?:^|\s)d-none(?!\S)/g , '' );
    if (!document.getElementById("default").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("default").className += " d-none";
    }
    if (!document.getElementById("downalphabet").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("downalphabet").className += " d-none";
    }
    if (!document.getElementById("alphabet").className.match(/(?:^|s)d-none(?!\S)/)){
        document.getElementById("alphabet").className += " d-none";
    }
    if (!document.getElementById("downdate").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("downdate").className += " d-none";
    }
}
function dalphabetically() {
    document.getElementById("downalphabet").className = document.getElementById("downalphabet").className.replace( /(?:^|\s)d-none(?!\S)/g , '' );
    if (!document.getElementById("default").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("default").className += " d-none";
    }
    if (!document.getElementById("date").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("date").className += " d-none";
    }
    if (!document.getElementById("alphabet").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("alphabet").className += " d-none";
    }
    if (!document.getElementById("downdate").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("downdate").className += " d-none";
    }
}
function ddate() {
    document.getElementById("downdate").className = document.getElementById("downdate").className.replace( /(?:^|\s)d-none(?!\S)/g , '' );
    if (!document.getElementById("default").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("default").className += " d-none";
    }
    if (!document.getElementById("date").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("date").className += " d-none";
    }
    if (!document.getElementById("alphabet").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("alphabet").className += " d-none";
    }
    if (!document.getElementById("downalphabet").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("downalphabet").className += " d-none";
    }
}
function ddefault() {
    document.getElementById("default").className = document.getElementById("default").className.replace( /(?:^|\s)d-none(?!\S)/g , '' );
    if (!document.getElementById("downdate").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("downdate").className += " d-none";
    }
    if (!document.getElementById("date").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("date").className += " d-none";
    }
    if (!document.getElementById("alphabet").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("alphabet").className += " d-none";
    }
    if (!document.getElementById("downalphabet").className.match(/(?:^|\s)d-none(?!\S)/)){
        document.getElementById("downalphabet").className += " d-none";
    }
}



$('.dropdown.keep-open').on({
    "shown.bs.dropdown": function() { this.closable = false; },
    "click":             function() { this.closable = true; },
    "hide.bs.dropdown":  function() { return this.closable; }
});


function add_ingrediente_function() {
    let valor = parseInt(document.getElementById('id_form-TOTAL_FORMS').value) + 1;
    document.getElementById('id_form-TOTAL_FORMS').value=String(valor);

    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    let ingrediente_form=document.getElementsByClassName('ingrediente_container')[0].innerHTML.replace(formRegex, `form-${valor-1}-`);
    document.getElementById('anadir_ingrediente_form').innerHTML+=ingrediente_form;

}
