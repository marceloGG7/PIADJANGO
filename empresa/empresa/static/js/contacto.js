const nombre = document.getElementById("nombre");
const email = document.getElementById("email");
const telefono = document.getElementById("telefono");
const mensaje = document.getElementById("mensaje");
const btn = document.getElementById("btn");

btn.addEventListener("click", (e) => {
    e.preventDefault();
    if (
        nombre.value.trim() === "" ||
        email.value.trim() === "" ||
        mensaje.value.trim() === "" ||
        telefono.value.trim() === ""
    ) {
        alert("Por favor, completa todos los datos.");
    } else {
        alert("Datos enviados correctamente.");
        nombre.value = "";
        email.value = "";
        mensaje.value = "";
        telefono.value = "";
    }
});
