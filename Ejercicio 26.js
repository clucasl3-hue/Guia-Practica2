//Ejercicio 26
let A = [2, 4, 6];
let B = [1, 3, 5];
let C = [];
let c = 0;
while (c < A.length) {
C.push(A[c] + B[c]);
c = c + 1;
}
console.log("La suma del arreglo A y B es: "+C);
