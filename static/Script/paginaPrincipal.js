
const contenedor = document.getElementById("contenedorPrincipal");

// Función para crear una tarjeta genérica
function crearTarjeta(imagen, titulo, destinoFlaskRoute) {
  const div = document.createElement("div");
  div.classList.add("TarjetaPedirCita");
  div.onclick = () => (window.location.href = destinoFlaskRoute);

  const img = document.createElement("img");
  img.src = `/static/Images/${imagen}`;
  img.alt = titulo;

  const h2 = document.createElement("h2");
  h2.textContent = titulo;

  div.appendChild(img);
  div.appendChild(h2);
  contenedor.appendChild(div);
}



// ✅ Verificar si hay un usuario autenticado
if (tipoUsuario && tipoUsuario !== "invitado") {
  // Generar tarjetas según el tipo de usuario
  if (tipoUsuario === "paciente") {
    crearTarjeta("Cita.png", "Agendar un turno", "/profesionales");
    crearTarjeta("Estadistica.png", "Datos del paciente", "/paciente");
  }
  else if (tipoUsuario === "especialista") {
    crearTarjeta("agenda.png", "Ver agenda", "/agenda");
    crearTarjeta("pacientes.png", "Lista de pacientes", "/pacientes");
    crearTarjeta("config.png", "Configuración", "/configuracion");
  }
} else {
  alert("Debes iniciar sesión primero.");
  window.location.href = "/login";
}