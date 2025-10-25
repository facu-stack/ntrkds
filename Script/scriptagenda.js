const grilla = document.getElementById("grilla");
const ocupados = ["10/10", "15/10", "20/10"]; // ejemplo

// Función para generar los próximos 30 días desde hoy
function generarFechas(dias = 30) {
    const fechas = [];
    const hoy = new Date();

    for (let i = 0; i < dias; i++) {
        const fecha = new Date(hoy);
        fecha.setDate(hoy.getDate() + i);
        const dia = fecha.getDate();
        const mes = fecha.getMonth() + 1;
        fechas.push(`${dia}/${mes}`);
    }

    return fechas;
}

const fechas = generarFechas(30);

// Crear la grilla
fechas.forEach(fecha => {
    const div = document.createElement("div");
    div.textContent = fecha;
    div.classList.add("fechas");

    if (ocupados.includes(fecha)) {
        div.classList.add("ocupado");
    } else {
        div.addEventListener("click", () => {
            document.querySelectorAll(".seleccionado").forEach(e => e.classList.remove("seleccionado"));
            div.classList.add("seleccionado");
        });
    }

    grilla.appendChild(div);
});

