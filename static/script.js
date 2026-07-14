// ===== CARRITO =====
let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

function guardarCarrito() {
  localStorage.setItem('carrito', JSON.stringify(carrito));
  actualizarContador();
}

function actualizarContador() {
  const contadores = document.querySelectorAll('.carrito-contador');
  const total = carrito.reduce((acc, p) => acc + p.cantidad, 0);
  contadores.forEach(c => {
    c.textContent = total;
    c.style.display = total > 0 ? 'inline-block' : 'none';
  });
}

function agregarCarrito() {
  const nombre = document.querySelector('.detalle-info h1').textContent.trim();
  const precio = document.querySelector('.detalle-precio').textContent.trim();
  const imgEl = document.querySelector('.detalle-imagen img');
  const imagen = imgEl ? imgEl.getAttribute('src') : '';

  const existe = carrito.find(p => p.nombre === nombre);
  if (existe) {
    existe.cantidad++;
  } else {
    carrito.push({ nombre, precio, imagen, cantidad: 1 });
  }

  guardarCarrito();
  alert('✅ Producto agregado al carrito!');
}

// ===== CARRUSEL =====
let actual = 0;

function mover(direccion) {
  const slides = document.querySelectorAll('.diapositiva');
  if (slides.length === 0) return;
  if (slides[actual].tagName === 'VIDEO') {
    slides[actual].pause();
  }
  slides[actual].classList.remove('activa');
  actual = (actual + direccion + slides.length) % slides.length;
  slides[actual].classList.add('activa');
  if (slides[actual].tagName === 'VIDEO') {
    slides[actual].play();
  }
}

setInterval(() => {
  const slides = document.querySelectorAll('.diapositiva');
  if (slides.length > 0) mover(1);
}, 4000);

// ===== ANIMACIONES =====
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

window.addEventListener('load', () => {
  document.querySelectorAll('.card, .novedades h2, .catalogo h2').forEach(el => {
    observer.observe(el);
  });
  actualizarContador();
});

// ===== BUSCADOR =====
const buscador = document.querySelector('.buscador');

if (buscador) {
  const params = new URLSearchParams(window.location.search);
  const textoBusqueda = params.get('buscar');
  if (textoBusqueda) {
    buscador.value = textoBusqueda;
    filtrar(textoBusqueda);
  }

  buscador.addEventListener('input', function() {
    filtrar(this.value.toLowerCase().trim());
  });
}

function filtrar(texto) {
  const secciones = document.querySelectorAll('.catalogo');
  secciones.forEach(seccion => {
    const cards = seccion.querySelectorAll('.card');
    const tituloSeccion = seccion.querySelector('h2').textContent.toLowerCase();
    let hayResultados = false;
    cards.forEach(card => {
      const nombre = card.querySelector('h3').textContent.toLowerCase();
      const descripcion = card.querySelector('p').textContent.toLowerCase();
      if (nombre.includes(texto) || descripcion.includes(texto) || tituloSeccion.includes(texto)) {
        card.style.display = 'block';
        hayResultados = true;
      } else {
        card.style.display = 'none';
      }
    });
    seccion.style.display = hayResultados ? 'block' : 'none';
  });
}

function buscarProducto(event) {
  if (event.key === 'Enter') {
    const texto = document.querySelector('.buscador').value.trim();
    if (texto) {
      window.location.href = '/catalogo?buscar=' + encodeURIComponent(texto);
    }
  }
}