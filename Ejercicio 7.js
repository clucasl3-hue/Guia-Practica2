const palabra = "radar";
let mensaje = "La palabra '" + palabra + "' es un palíndromo.";
let contador = 0;
for (let posicion = 0; posicion < palabra.length / 2; posicion++) {
  let letraInicial = palabra[posicion];
  let letraFinal = palabra[palabra.length - 1 - posicion];
  if (letraInicial !== letraFinal) {
    contador = contador + 1;
  }
}
if (contador > 0) {
  mensaje = "La palabra '" + palabra + "' no es un palíndromo.";
}
console.log(mensaje);
