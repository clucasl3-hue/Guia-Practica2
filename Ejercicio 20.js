function buscarValor() {
  let numeros = [4, 8, 15, 23];
  let buscar = parseInt(prompt("Ingresa el número que deseas buscar:"));
  let encontrado = false;
  for (let i = 0; i < numeros.length; i++) {
     n=numeros[i]
    if (n == buscar) {
      encontrado = true;
      valoren=n;
    }
  }
  if (encontrado) {
    console.log("El valor "+valoren+" sí existe en el arreglo.");
  } 
}
