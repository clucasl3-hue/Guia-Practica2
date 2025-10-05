function compararFrases(frase1, frase2) {
  if (frase1.length > frase2.length) {
    console.log("La frase '" + frase1 + "' tiene más caracteres.");
  } else if (frase2.length > frase1.length) {
    console.log("La frase '" + frase2 + "' tiene más caracteres.");
  } else {
    console.log("Ambas frases tienen la misma cantidad de caracteres.");
  }
}
const fraseA = "Me gusta el fútbol";
const fraseB = "Prefiero el baloncesto";
compararFrases(fraseA, fraseB);
