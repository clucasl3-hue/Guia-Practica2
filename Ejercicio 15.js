//Factorial de numeros con arreglos 15
let numeros = [3 , 5];
for (let i = 0; i < numeros.length; i++) {
    let num = numeros [i];
    let factorial = 1;
    for (let c = 1; c <= num; c++) {
        factorial *= c;
        console.log("Factorial de " + num + " = " + factorial);
    }
}
