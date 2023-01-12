function Hidepreloader(){
    setTimeout(() => {
        document.getElementById("preloader").style.display = "none";
        document.getElementById("normnav").style.display = "flex";
        document.getElementById("anime").style.display = "block";
        document.getElementById("dbody").style.display = "block";
    }, 1000);

}

function Shownav(){
    if(document.getElementById("smallnav").style.display == "none"){
        document.getElementById("smallnav").style.display = "flex";
        setTimeout(() => {
            document.getElementById("smallnav").style.opacity = "1";
        }, 200);
    }
    else{
        document.getElementById("smallnav").style.opacity = "0";
        setTimeout(() => {
            document.getElementById("smallnav").style.display = "none";
        }, 1000);
        
    }
}

function Anime(){
    const hei = Number(window.innerHeight);
    let pos = Number(document.documentElement.scrollTop);
    const deno = 7250 - hei;
    let perc = (100*pos)/deno;
    document.getElementById("anime").style.width = perc + "%";
}

setInterval(() => {
    Anime();
}, 500);