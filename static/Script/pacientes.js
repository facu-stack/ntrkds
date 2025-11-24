let todosLosPacientes = [];

// pacientes.js (Corregido)

// pacientes.js (Versión limpia)

// pacientes.js (Versión corregida usando la clave original de la DB)

function crearTarjetaPaciente(p) {
    console.log("ID del Paciente:", p.ID_usuario); 
    return `
        <div class="tarjeta-paciente">
            <h3>${p.Nombre} ${p.Apellido}</h3>
            <p>DNI: ${p.DNI}</p>

            <button onclick="window.location.href='/paciente/${p.ID_usuario}'">
                Ver ficha
            </button>

            <button onclick="window.location.href='/anamnesis/${p.ID_usuario}'">
            Anamnesis alimentaria
        </button>
        

            <button onclick="window.location.href='/cita/${p.ID_usuario}'">
                Cita de rutina
            </button>
        </div>
    `;
}
// ...
// ... el resto de tu código
function renderPacientes(lista) {
    const contenedor = document.getElementById("listaPacientes");
    contenedor.innerHTML = "";

    lista.forEach(p => {
        contenedor.innerHTML += crearTarjetaPaciente(p);
    });
}

function filtrarPacientes() {
    const texto = document.getElementById("buscador").value.toLowerCase();

    const filtrados = todosLosPacientes.filter(p =>
        (p.Nombre + " " + p.Apellido).toLowerCase().includes(texto) ||
        p.DNI.toString().includes(texto)
    );

    renderPacientes(filtrados);
}

// 🔵 Cargar pacientes al iniciar
fetch("/api/pacientes")
    .then(r => r.json())
    .then(lista => {
        todosLosPacientes = lista;
        renderPacientes(lista);
    });

// 🔵 Agregar evento de búsqueda en vivo
document.getElementById("buscador").addEventListener("input", filtrarPacientes);
