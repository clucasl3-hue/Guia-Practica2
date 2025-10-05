// Divisores 11
let numeros = [6, 10];
for (let i = 0; i < numeros.length; i++) {
    let num = numeros[i]; 
for (let c = 1; c <= num; c++) {
    if (num % c === 0) {
        console.log("Divisor de " + num + ": " + c);
    } else {
        console.log(c + " no es divisor de " + num);
    }
    }
}
