// static/js/dashboard_autoridad.js

// Funciones para manejar el modal de crear ticket
function abrirModalCrearTicket() {
    document.getElementById('modalCrearTicket').style.display = 'block';
}

function cerrarModalCrearTicket() {
    document.getElementById('modalCrearTicket').style.display = 'none';
}

// Función para ir a ver reportes
function irAVerReportes() {
    const lang = document.body.lang || 'es';
    window.location.href = `/modal_ver_reportes?lang=${lang}`;
}

// Cerrar modal al hacer clic fuera
function configurarCerrarModal() {
    window.onclick = function(event) {
        const modal = document.getElementById('modalCrearTicket');
        if (event.target === modal) {
            cerrarModalCrearTicket();
        }
    }
}

// Inicializar cuando el documento esté listo
document.addEventListener('DOMContentLoaded', function() {
    configurarCerrarModal();
    
    // También puedes agregar event listeners aquí en lugar de onclick en HTML
    // document.getElementById('btnCrearReporte').addEventListener('click', abrirModalCrearTicket);
    // document.getElementById('btnVerReportes').addEventListener('click', irAVerReportes);
});