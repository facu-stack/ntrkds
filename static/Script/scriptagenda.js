// scriptagenda.js

const grillaDias = document.getElementById("grillaDias");
const grillaHorarios = document.getElementById("grillaHorarios");
const seccionHorarios = document.getElementById("seccionHorarios");
const textoInstruccion = document.getElementById("textoInstruccion");
const fechaSeleccionadaTexto = document.getElementById("fechaSeleccionadaTexto");
const btnConfirmar = document.getElementById("btnConfirmar");
const btnVolverDia = document.getElementById("btnVolverDia");

const ESPECIALISTA_ID = 1;
const horariosDisponibles = [
    "09:00", "09:30", "10:00", "10:30", "11:00",
    "11:30", "12:00", "12:30", "13:00", "13:30",
    "14:00", "14:30", "15:00", "15:30", "16:00"
];

let fechaSeleccionada = null;
let horaSeleccionada = null;

// -----------------------------
// Funciones API
// -----------------------------
async function cargarHorariosOcupados(fechaCompleta) {
    try {
        const response = await fetch(`/api/horarios-ocupados?fecha=${fechaCompleta}&especialista_id=${ESPECIALISTA_ID}`);
        const data = await response.json();

        if (data.success) {
            return data.ocupados;
        } else {
            console.error('Error al cargar horarios:', data.error);
            return [];
        }
    } catch (error) {
        console.error('Error de conexión:', error);
        return [];
    }
}

// -----------------------------
// Funciones auxiliares
// -----------------------------
function generarFechas(dias = 30) {
    const fechas = [];
    const hoy = new Date();

    for (let i = 0; i < dias; i++) {
        const fecha = new Date(hoy);
        fecha.setDate(hoy.getDate() + i);
        const dia = fecha.getDate().toString().padStart(2, '0');
        const mes = (fecha.getMonth() + 1).toString().padStart(2, '0');
        const fechaCompleta = fecha.toISOString().split('T')[0]; // YYYY-MM-DD

        fechas.push({
            display: `${dia}/${mes}`,
            completa: fechaCompleta,
            objeto: fecha
        });
    }
    return fechas;
}

function formatearFecha(fechaObj) {
    const opciones = { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' };
    return fechaObj.toLocaleDateString('es-ES', opciones);
}

// -----------------------------
// Inicializar grilla de días
// -----------------------------
async function inicializarGrillaDias() {
    const fechas = generarFechas(30);
    grillaDias.innerHTML = '';

    fechas.forEach(fechaObj => {
        const div = document.createElement("div");
        div.textContent = fechaObj.display;
        div.classList.add("dia", "libre");
        div.setAttribute('data-fecha', fechaObj.completa);
        div.title = `Click para seleccionar ${formatearFecha(fechaObj.objeto)}`;

        div.addEventListener("click", async () => {
            document.querySelectorAll(".dia.seleccionado").forEach(e => e.classList.remove("seleccionado"));
            div.classList.add("seleccionado");

            fechaSeleccionada = {
                display: fechaObj.display,
                completa: fechaObj.completa,
                objeto: fechaObj.objeto
            };

            console.log("Día seleccionado:", fechaSeleccionada);

            await cargarHorariosParaFecha(fechaSeleccionada);
        });

        grillaDias.appendChild(div);
    });
}

// -----------------------------
// Cargar horarios por fecha
// -----------------------------
async function cargarHorariosParaFecha(fecha) {
    try {
        grillaHorarios.innerHTML = '<div class="cargando">Cargando horarios...</div>';
        seccionHorarios.style.display = 'block';
        btnVolverDia.style.display = 'inline-block';
        document.querySelector('.seccion-dias').style.display = 'none';
        textoInstruccion.textContent = 'Ahora seleccioná un horario:';
        fechaSeleccionadaTexto.textContent = formatearFecha(fecha.objeto);

        // ⚠️ Usar fecha.completa para la API
        const horariosOcupados = await cargarHorariosOcupados(fecha.completa);

        // Formatear correctamente a HH:MM
        const horariosOcupadosFormateados = horariosOcupados.map(h => {
            let partes = h.split(':');
            let hh = partes[0].padStart(2, '0');
            let mm = partes[1] ? partes[1].padStart(2, '0') : '00';
            return `${hh}:${mm}`;
        });

        window.horariosOcupadosGlobal = horariosOcupadosFormateados; // para debug
        console.log("Horarios ocupados formateados:", horariosOcupadosFormateados);

        grillaHorarios.innerHTML = '';

        horariosDisponibles.forEach(hora => {
            const div = document.createElement("div");
            div.textContent = hora;
            div.classList.add("horario");
            div.setAttribute('data-hora', hora);

            if (horariosOcupadosFormateados.includes(hora)) {
                div.classList.add("ocupado");
                div.title = "Horario no disponible";
            } else {
                div.classList.add("libre");
                div.title = "Click para seleccionar este horario";

                div.addEventListener("click", () => {
                    document.querySelectorAll(".horario.seleccionado").forEach(e => e.classList.remove("seleccionado"));
                    div.classList.add("seleccionado");
                    horaSeleccionada = hora;
                    btnConfirmar.disabled = false;
                    btnConfirmar.textContent = `Confirmar Turno a las ${hora}`;
                    console.log("Horario seleccionado:", hora);
                });
            }

            grillaHorarios.appendChild(div);
        });

    } catch (error) {
        console.error('Error al cargar horarios:', error);
        grillaHorarios.innerHTML = '<div class="error">Error al cargar horarios</div>';
    }
}

// -----------------------------
// Volver a la selección de días
// -----------------------------
function volverADias() {
    seccionHorarios.style.display = 'none';
    btnVolverDia.style.display = 'none';
    document.querySelector('.seccion-dias').style.display = 'block';
    textoInstruccion.textContent = 'Seleccioná un día:';

    fechaSeleccionada = null;
    horaSeleccionada = null;
    btnConfirmar.disabled = true;
    btnConfirmar.textContent = 'Confirmar Turno';

    document.querySelectorAll(".seleccionado").forEach(e => e.classList.remove("seleccionado"));
}

// -----------------------------
// Confirmar turno
// -----------------------------
async function confirmarTurno() {
    if (!fechaSeleccionada || !horaSeleccionada) {
        alert('Por favor selecciona un día y un horario');
        return;
    }

    const confirmacion = confirm(
        `¿Confirmar turno para el ${formatearFecha(fechaSeleccionada.objeto)} a las ${horaSeleccionada}?`
    );

    if (confirmacion) {
        try {
            const response = await fetch('/api/guardar-turno', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    fecha: fechaSeleccionada.completa, // YYYY-MM-DD
                    hora: horaSeleccionada,
                    especialista_id: ESPECIALISTA_ID,
                    motivo: 'Consulta programada'
                })
            });

            const data = await response.json();

            if (data.success) {
                alert('¡Turno reservado exitosamente!');
                window.location.href = '/paginaprincipal';
            } else {
                alert('Error al reservar turno: ' + data.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexión al reservar turno');
        }
    }
}

// -----------------------------
// Event Listeners
// -----------------------------
btnConfirmar.addEventListener('click', confirmarTurno);
btnVolverDia.addEventListener('click', volverADias);

document.addEventListener('DOMContentLoaded', inicializarGrillaDias);
