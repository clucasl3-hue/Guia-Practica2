//Ejercicio 24
let n = [4, 6];
let f = [];
let c = 0;
while (c < n.length) {
let num = n[c];
let fact = 1;
let i = 1;
while (i <= num) {
fact = fact * i;
i = i + 1;
}
f.push(fact);
c = c + 1;
}
console.log("Los valores factoriales son: "+f);
