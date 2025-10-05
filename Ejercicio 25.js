//Ejercicio 25
let a = [3, 8, 11, 14, 25];
let pares = [];
let c = 0;
while (c < a.length) {
if (a[c] % 2 === 0) {
pares.push(a[c]);
}
c = c + 1;
}
console.log("Los valores pares son: " +pares);
