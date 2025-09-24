const supabase = supabase.createClient(
  'https://qxpgnrbavoovbhrrunkz.supabase.co',
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF4cGducmJhdm9vdmJocnJ1bmt6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTY5NDEyOTQsImV4cCI6MjA3MjUxNzI5NH0.6NZNGTYUzDU3MEYaO9WpiVK23rGQ8IRr29Y1HYOVExQ'
);

async function cargarProductos() {
  const { data, error } = await supabase
    .from('productos')
    .select('id_p, producto, cantidad, precio_venta')
    .order('producto', { ascending: true });

  if (error) {
    console.error('Error al cargar productos:', error);
    return;
  }

  const tbody = document.querySelector('#tabla-productos tbody');
  tbody.innerHTML = ''; // Limpiar tabla

  data.forEach(producto => {
    const fila = document.createElement('tr');
    fila.innerHTML = `
      <td>${producto.id_p}</td>
      <td>${producto.producto}</td>
      <td>${producto.cantidad}</td>
      <td>${producto.precio_venta}</td>
    `;
    tbody.appendChild(fila);
  });
}

// Suscripción en tiempo real
supabase
  .channel('productos-cambios')
  .on('postgres_changes', { event: '*', schema: 'public', table: 'productos' }, () => {
    cargarProductos();
  })
  .subscribe();

cargarProductos();
