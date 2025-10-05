function contarImpares() {
  let numeros = [2, 5, 7, 8, 10];
  let contar = 0;
  for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] % 2 != 0) {
      contar = contar + 1;
    }
  }
  alert("Cantidad de impares: " + contar);
}
