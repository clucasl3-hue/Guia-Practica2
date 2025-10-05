//Ejercicio 23
let num = [3, 5];
let c = 0;
while (c < num.length) {
let mult = 1;
console.log("La tabla del " + num[c] + ":");
while (mult <= 10) {
console.log(num[c] * mult);
mult = mult + 1;
}
c = c + 1;
}
