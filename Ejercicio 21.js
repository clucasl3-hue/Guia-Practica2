function concatenarPalabras() {
  let palabras = ["Me", "gusta", "programar"];
  let texto = "";
  for (let i = 0; i < palabras.length; i++) {
    texto = texto + palabras[i] + " ";
  }
  console.log(texto);
}
