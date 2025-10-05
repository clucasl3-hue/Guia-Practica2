function contarCaracter(texto, caracter) {
  let contador = 0;
  for (let i = 0; i < texto.length; i++) {
    if (texto[i] === caracter) {
      contador++;
    }
  }
  console.log("La letra '" + caracter + "' aparece " + contador + " veces.");
}
const texto = "Examen de programación";
const letra = "m";
contarCaracter(texto, letra);
