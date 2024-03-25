function pages(event){
    var idButonApasat = event.target.id;
    if(idButonApasat == "button_back") document.location.assign("meniu.html");
    else if(idButonApasat == "button_logout") document.location.assign("login.html");
}


function highScores(game){
    document.location.assign("highScores.html");
}