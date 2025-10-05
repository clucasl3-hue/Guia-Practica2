//Invertir numeros en un arreglo 16
let numeros = [123, 450]
let numerosInvertidos = [];
for (let i = 0; i < numeros.length; i++) {
let num = numeros[i];
let invertido = Number(String(num).split("").reverse().join(""));
numerosInvertidos.push(invertido);
}
console.log(numerosInvertidos);
