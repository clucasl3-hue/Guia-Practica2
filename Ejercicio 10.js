function dividirOracion(oracion) {
  const palabras = oracion.split(" ");
  for (let i = 0; i < palabras.length; i++) {
    console.log("• " + palabras[i]);
  }
}
const texto = "Me gusta aprender programación";
dividirOracion(texto);
