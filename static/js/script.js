// 1. Pedimos los datos a nuestra propia API (el endpoint /earthquakes de app.py)
async function cargarSismos() {
  const respuesta = await fetch('/earthquakes');
  const sismos = await respuesta.json();

  // Cada "sismo" llega como una lista: [id, magnitude, location, date]
  // porque database.py usa "SELECT * FROM earthquakes"
  pintarTabla(sismos);
  pintarEstadisticas(sismos);
}

// 2. Recorremos los sismos y creamos una fila <tr> por cada uno
function pintarTabla(sismos) {
  const cuerpo = document.getElementById('cuerpo-tabla');
  cuerpo.innerHTML = '';

  sismos.forEach(sismo => {
    const [id, magnitud, ubicacion, fecha] = sismo;

    const fila = document.createElement('tr');
    fila.innerHTML = `
      <td class="magnitud">${magnitud.toFixed(1)}</td>
      <td>${ubicacion}</td>
      <td>${formatearFecha(fecha)}</td>
    `;
    cuerpo.appendChild(fila);
  });
}

// 3. El campo "date" viene como timestamp en milisegundos (formato USGS)
function formatearFecha(timestampMs) {
  const fecha = new Date(Number(timestampMs));
  return fecha.toLocaleString('es-PE', {
    day: '2-digit', month: 'short', year: 'numeric',
    hour: '2-digit', minute: '2-digit'
  });
}

// 4. Estadísticas simples calculadas aquí mismo, en el navegador
function pintarEstadisticas(sismos) {
  const contenedor = document.getElementById('stats');

  if (sismos.length === 0) {
    contenedor.innerHTML = '<p>No hay sismos registrados todavía.</p>';
    return;
  }

  const magnitudes = sismos.map(s => s[1]);
  const total = sismos.length;
  const maxima = Math.max(...magnitudes).toFixed(1);
  const promedio = (magnitudes.reduce((a, b) => a + b, 0) / total).toFixed(1);

  contenedor.innerHTML = `
    <div class="stat"><span class="numero">${total}</span><span class="etiqueta">Sismos</span></div>
    <div class="stat"><span class="numero">${maxima}</span><span class="etiqueta">Magnitud máxima</span></div>
    <div class="stat"><span class="numero">${promedio}</span><span class="etiqueta">Magnitud promedio</span></div>
  `;
}

// Ejecutamos todo al cargar la página
cargarSismos();
