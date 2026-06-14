let data = JSON.parse(localStorage.getItem("trs") || "[]");

let total = 0;

data.forEach(d=>{
let dispo = (d.produit - d.arret) / d.produit;
total += dispo;
});

let trs = (total / data.length) * 100;

document.getElementById("trs").innerHTML =
"TRS Global : " + trs.toFixed(2) + " %";
