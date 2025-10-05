let nombreCompleto = prompt("Ingresa tu nombre completo:");
let partes = nombreCompleto.split(" ");
let iniciales = "";

for (let i = 0; i < partes.length; i++) {
  iniciales += partes[i][0].toUpperCase() + ".";
}

console.log(`Iniciales: ${iniciales}`);
