let todosLosPacientes = [];

/**
 * Genera la estructura HTML para la tarjeta del paciente.
 * Aplica clases CSS basadas en el estado de la cita.
 */
function crearTarjetaPaciente(p) {
    // ... (otras variables de clase)
    const estadoClase = p.EstadoCita.toLowerCase() === 'confirmado' ? 'estado-confirmado' : 'estado-en-espera';
    let botonCancelarHTML = `
        <button class="btn-cancelar-cita" data-id="${p.id}" onclick="cancelarCita(${p.id})">
            Cancelar Cita
        </button>
    `;
    // Define el botón de Aceptar solo si el estado es 'en espera'
    let botonConfirmarHTML = '';
        if (p.EstadoCita.toLowerCase() === 'programada') {
            botonConfirmarHTML = `
                <button class="btn-confirmar-cita" data-id="${p.id}" onclick="confirmarCita(${p.id})">
                    Confirmar Cita
                </button>
            `;
            }
    


    return `
        <div class="tarjeta-paciente ${estadoClase}">
            <h3>${p.Nombre} ${p.Apellido} - ${p.HoraCita}</h3>
            <p>DNI: ${p.DNI}</p>
            <p class="estado-texto">Estado: ${p.EstadoCita.toUpperCase()}</p>

            <button data-id="${p.id}" class="btn-ver-ficha">
                Ver ficha
            </button>

            
            
            ${botonConfirmarHTML}
            ${botonCancelarHTML}
            </div>;
            

    `
}

// ------------------------------------------------------------------
// NUEVA FUNCIÓN JS PARA MANEJAR EL CLIC
// ------------------------------------------------------------------

function confirmarCita(idCita) {
    if (!confirm("¿Estás seguro de que quieres confirmar esta cita?")) {
        return; // El especialista canceló la acción
    }

    // 1. Envía la solicitud a Flask para actualizar la BD
    fetch(`/api/turno/confirmar/${idCita}`, {
        method: 'POST', // Usamos POST para acciones de modificación
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al confirmar la cita');
        }
        return response.json();
    })
    .then(data => {
        alert(data.message);
        
        // 2. Recarga los datos para actualizar la interfaz inmediatamente
        // Esto asume que tienes una función para recargar la lista de la API
        recargarPacientes(); 
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al confirmar la cita.');
    });
}

// Asegúrate de que tu lógica de carga esté envuelta en una función para recargar:
function recargarPacientes() {
    fetch("/api/turnos")
        .then(r => r.json())
        .then(lista => {
            todosLosPacientes = lista;
            renderPacientes(lista);
        });
}

// Llama a la nueva función al inicio:
recargarPacientes();
/**
 * Ordena, filtra y renderiza la lista de pacientes en el DOM.
 * Implementa:
 * 1. Ordenamiento por HoraCita.
 * 2. Filtrado de citas canceladas (solo muestra las activas).
 * 3. Mejora de rendimiento del DOM (usa createElement).
 */
function renderPacientes(lista) {
    const contenedor = document.getElementById("listaPacientes");
    contenedor.innerHTML = ""; // Limpiar antes de renderizar

    // 1. ORDENAR por HoraCita (formato 'HH:mm' permite la comparación con localeCompare)
    lista.sort((a, b) => a.HoraCita.localeCompare(b.HoraCita)); 

    // 2. FILTRAR CITAS CANCELADAS (Solo renderiza las citas donde p.Cancelado es falso)
    const citasActivas = lista.filter(p => !p.Cancelado);

    // 3. RENDERIZAR
    citasActivas.forEach(p => {
        // Usando createElement para una inserción más eficiente en el DOM
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = crearTarjetaPaciente(p).trim();
        
        // El primer hijo es la tarjeta-paciente
        contenedor.appendChild(tempDiv.firstChild); 
    });
}

// ------------------------------------------------------------------
// NUEVA FUNCIÓN JS PARA CANCELAR CITA
// ------------------------------------------------------------------

function cancelarCita(idCita) {
    if (!confirm("¿Estás seguro de que quieres CANCELAR esta cita? La cita se marcará como cancelada (campo 'cancelado' a 1).")) {
        return; // El especialista canceló la acción
    }

    // 1. Envía la solicitud a Flask para actualizar el campo 'cancelado' a 1
    fetch(`/api/turno/cancelar/${idCita}`, {
        method: 'POST', // Usamos POST para acciones de modificación
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        if (!response.ok) {
            // Si la respuesta no es 200-299, lanza un error
            throw new Error('Error al cancelar la cita en el servidor.');
        }
        return response.json();
    })
    .then(data => {
        alert(data.message || 'Cita cancelada exitosamente.');
        
        // 2. Recarga los datos para actualizar la interfaz. 
        // Como 'renderPacientes' filtra las canceladas, esta cita desaparecerá.
        recargarPacientes(); 
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al intentar cancelar la cita.');
    });
}

/**
 * Filtra los pacientes en tiempo real por nombre, apellido o DNI.
 * Llama a renderPacientes, que se encarga del ordenamiento y las cancelaciones.
 */
function filtrarPacientes() {
    const texto = document.getElementById("buscador").value.toLowerCase();

    const filtrados = todosLosPacientes.filter(p =>
        (p.Nombre + " " + p.Apellido).toLowerCase().includes(texto) ||
        p.DNI.toString().includes(texto)
    );

    renderPacientes(filtrados);
}

// Ahora:
fetch("/api/turnos") 
    .then(r => r.json())
    .then(lista => {
        todosLosPacientes = lista; // La lista ahora contiene la info de los turnos
        renderPacientes(lista);
    });

// 🔵 Delegación de eventos para el botón "Ver ficha"
// Maneja el clic en todos los botones de la lista sin añadir un listener a cada uno.
document.getElementById("listaPacientes").addEventListener("click", (e) => {
    // Verificar si el elemento clickeado o su padre es el botón
    const target = e.target.closest(".btn-ver-ficha");

    if (target) {
        const pacienteId = target.dataset.id;
        window.location.href = `/paciente/${pacienteId}`;
    }
});