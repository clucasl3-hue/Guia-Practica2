//Numeros primos en un arreglo 14
let numeros = [7, 18 ,13];
let numerosprimos = [];
for (let i = 0; i < numeros.length; i++) {
    let num = numeros[i];
    if (num < 2) continue; 
    let esPrimo = true; 
    for (let c = 2; c < num; c++) {
        if (num % c === 0) {
            esPrimo = false; 
            break;
        }
    }
    if (esPrimo) {
        numerosprimos.push(num);
    }
    }
    console.log("Numeros primos: " + numerosprimos.join(", "));
