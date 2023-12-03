const nombre = document.getElementById("nombre");
const edad = document.getElementById("edad");
const direccion = document.getElementById("direccion");
const email = document.getElementById("email");
const sexo = document.getElementById("sexo");
const tipoSangre = document.getElementById("tipoSangre");
const btn = document.getElementById("btn");

btn.addEventListener("click", (e) => {
    e.preventDefault();
    if (
        nombre.value.trim() === "" || edad.value.trim() === "" || direccion.value.trim() === "" ||
        email.value.trim() === "" || sexo.value.trim() === "" || tipoSangre.value.trim() === ""
    ) {
        alert("Por favor, completa todos los datos.");
    }
    else {
        alert("Datos enviados correctamente.");
        nombre.value = "";
        edad.value = "";
        direccion.value = "";
        email.value = "";
        sexo.value = "";
        tipoSangre.value = "";
    }
});