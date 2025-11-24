document.addEventListener("DOMContentLoaded", cargarProfesionales);

function cargarProfesionales() {
    fetch("/api/profesionales")
        .then(res => res.json())
        .then(datos => {
            datos.forEach(p => {
                document.getElementById("listaProfesionales").innerHTML += crearTarjetaProfesional(p);
            });
        })
        .catch(err => console.error("Error cargando profesionales:", err));
}

function crearTarjetaProfesional(p) {
    // IMAGEN POR DEFECTO SI NO TIENE FOTO
    let randomFace = `https://randomuser.me/api/portraits/women/${Math.floor(Math.random()*50)}.jpg`;

    return `
        <div class="card">
            <img src="${randomFace}" alt="${p.Nombre}">
            <h3>${p.Nombre}</h3>
            <p>${p.Especialidad}</p>
            <a href="/turno?id=${p.id}" class="btn">Agendar turno</a> 
        </div>
    `;
}
