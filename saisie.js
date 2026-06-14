const postes = {
"Mécanique":["Découpage","Marquage","Emboutissage"],
"Soudage":["Soudage collerette","Soudage pied","Soudage corps"],
"Finition":["Peinture","Grenaillage","Test air"]
};

function loadPostes(){
let sec = document.getElementById("section").value;
let p = document.getElementById("poste");

p.innerHTML = "";

postes[sec].forEach(x=>{
let opt = document.createElement("option");
opt.textContent = x;
p.appendChild(opt);
});
}

function saveData(){

let data = {
nom: document.getElementById("nom").value,
section: document.getElementById("section").value,
poste: document.getElementById("poste").value,
produit: Number(document.getElementById("produit").value),
cycle: Number(document.getElementById("cycle").value),
arret: Number(document.getElementById("arret").value),
date: new Date().toLocaleString()
};

let old = JSON.parse(localStorage.getItem("trs") || "[]");
old.push(data);

localStorage.setItem("trs", JSON.stringify(old));

alert("Données enregistrées !");
}
