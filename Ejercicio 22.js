function cuboElementos() {
  let numeros = [2, 3, 4];
  for (let i = 0; i < numeros.length; i++) {
    let cubo = numeros[i] * numeros[i] * numeros[i];
    console.log("Cubo de " + numeros[i] + " = " + cubo);
  }
}
