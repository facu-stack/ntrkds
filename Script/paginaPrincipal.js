// Obtener el tipo de usuario desde localStorage
// ⚠️ Solo para pruebas
if (!localStorage.getItem("tipoUsuario")) {
  localStorage.setItem("tipoUsuario", "especialista");
}


const tipoUsuario = localStorage.getItem("tipoUsuario");
const contenedor = document.getElementById("contenedorPrincipal");

// Función para crear una tarjeta genérica
function crearTarjeta(imagen, titulo, destino) {
  const div = document.createElement("div");
  div.classList.add("TarjetaPedirCita");
  div.onclick = () => (window.location.href = destino);

  const img = document.createElement("img");
  img.src = imagen;
  img.alt = titulo;

  const h2 = document.createElement("h2");
  h2.textContent = titulo;

  div.appendChild(img);
  div.appendChild(h2);
  contenedor.appendChild(div);
}

// Generar tarjetas según el tipo de usuario
if (tipoUsuario === "paciente") {
  crearTarjeta("../static/Images/Cita.png", "Agendar un turno", "formulario.html");
  crearTarjeta("../static/Images/Estadistica.png", "Datos del paciente", "paciente.html");
} 
else if (tipoUsuario === "especialista") {
  crearTarjeta("../static/Images/agenda.png", "Ver agenda", "agenda.html");
  crearTarjeta("../static/Images/pacientes.png", "Lista de pacientes", "profesionales.html");
  crearTarjeta("../static/Images/config.png", "Configuración", "configuracion.html");
} 
else {
  // Si no hay tipo definido, volver al login
  alert("Debes iniciar sesión primero.");
  window.location.href = "login.html";
}
