

function init(){
    'use strict'
    if (document && document.getElementById){
        const footerEnd = document.getElementById('footer');
        footerEnd.innerHTML = "Copyright &copy " + new Date().getFullYear();
    }
}
init()

function autoRefresh() {
        window.location = window.location.href;
    }
//setInterval('autoRefresh()', 5000);
