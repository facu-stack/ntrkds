const horarios = [
  "9:00", "9:30", "10:00", "10:30", "11:00",
  "11:30", "12:00", "12:30", "13:00", "13:30",
  "14:00", "14:30", "15:00", "15:30", "16:00"
];

const fechas= [
  "1/10","2/10","3/10","4/10","5/10","6/10","7/10","/8/10","9/10","10/10","11/10","12/10","13/10","14/10/","15/10","16/10","17/10","18/10","19,10","20/10","21/10","22/10","23/10","24/10","5/10","26/10","27/10","28/10","29/10","30/10","31/10"
]

// Ejemplo: estos horarios ya están ocupados
const ocupados = ["10:00", "13:00"];

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

