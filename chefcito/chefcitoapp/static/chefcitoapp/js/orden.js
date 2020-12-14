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
    if (!document.getElementById("alphabet").className.match(/(?:^|\s)d-none(?!\S)/)){
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