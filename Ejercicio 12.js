//Suma de divisores en un arreglo 12
let numeros = [6, 12];
for (let i = 0; i < numeros.length; i++) {
    let num = numeros[i];
    let sumaDivisores = 0;
    for (let c = 1; c <= num; c++) {
        if (num % c === 0) {
            sumaDivisores += c;
            console.log("Sumando divisor de " + num + " = " + sumaDivisores);
        }
        }
        }
