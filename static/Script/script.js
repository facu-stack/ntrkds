const horarios = [
  "9:00", "9:30", "10:00", "10:30", "11:00",
  "11:30", "12:00", "12:30", "13:00", "13:30",
  "14:00", "14:30", "15:00", "15:30", "16:00"
];

const ocupados = ["10:00", "11:30", "15:00"]; // horarios ya ocupados

const grilla = document.getElementById("grilla");

horarios.forEach(hora => {
  const div = document.createElement("div");
  div.textContent = hora;
  div.classList.add("horario");

  if (ocupados.includes(hora)) {
    div.classList.add("ocupado");
  } else {
    div.addEventListener("click", () => {
      if (div.classList.contains("seleccionado")) {
        div.classList.remove("seleccionado");
      } else {
        document.querySelectorAll(".seleccionado").forEach(e => e.classList.remove("seleccionado"));
        div.classList.add("seleccionado");
      }
    });
  }

  grilla.appendChild(div);
});

function mostrarPaciente() {
  document.getElementById('tutor').style.display = 'none';
  document.getElementById('paciente').style.display = 'block';
}

function mostrarTutor() {
  document.getElementById('paciente').style.display = 'none';
  document.getElementById('tutor').style.display = 'block';
}
