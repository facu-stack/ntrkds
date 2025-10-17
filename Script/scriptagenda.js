const fechas = [
    "1/10", "2/10", "3/10", "4/10", "5/10", "6/10", "7/10", "8/10", "9/10", "10/10",
    "11/10", "12/10", "13/10", "14/10", "15/10", "16/10", "17/10", "18/10", "19/10",
    "20/10", "21/10", "22/10", "23/10", "24/10", "25/10", "26/10", "27/10", "28/10",
    "29/10", "30/10", "31/10"
];

const ocupados = ["10/10", "15/10", "20/10"]; // ejemplo
const grilla = document.getElementById("grilla");

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
