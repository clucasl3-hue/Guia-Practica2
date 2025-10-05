const entrada = "Programador";
let salida = "";
for (let i = 0; i < entrada.length; i++) {
  const caracter = entrada[i];
  if (caracter === "o") {
    salida += "#";
  } else {
    salida += caracter;
  }
}
console.log(salida); // Programador 
