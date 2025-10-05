//Numeros perfectos en un arreglo 13
let numeros = [6, 10, 28];
let numerosperfectos = [];
for (let i = 0; i < numeros.length; i++) {
    let num = numeros[i];
    let sumaDivisores = 0;
    for (let c = 1; c < num; c++) {
if (num % c === 0) {
    sumaDivisores += c; 
}
    }
    if (sumaDivisores === num) {
        numerosperfectos.push(num);
}
}
console.log("Numeros perfectos: " + numerosperfectos.join(", "));

