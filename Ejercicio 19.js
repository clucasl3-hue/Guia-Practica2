function mayoresDeEdad() {
  let edades = [15, 22, 18, 30, 12];
  let contar = 0;
  for (let i = 0; i < edades.length; i++) {
    if (edades[i] >= 18) {
      contar = contar + 1;
    }
  }
  console.log("Mayores de edad: " + contar);
}
