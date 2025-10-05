let palabra1 = prompt("Ingresa la primera palabra:");
let palabra2 = prompt("Ingresa la segunda palabra:");

if (palabra1.length > palabra2.length) {
  console.log(`La palabra '${palabra1}' tiene más letras.`);
} else if (palabra2.length > palabra1.length) {
  console.log(`La palabra '${palabra2}' tiene más letras.`);
} else {
  console.log(`Ambas palabras tienen la misma cantidad de letras.`);
}
