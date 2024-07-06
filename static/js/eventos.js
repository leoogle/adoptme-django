function loadContent(url) {
    fetch(url)
        .then(response => response.text())
        .then(data => {
            const contentContainer = document.getElementById('content-container');
            contentContainer.innerHTML = data;
        });
}
function setupEventListeners() {
    setTimeout(() => {
    const navLinks = document.querySelectorAll('.nav-link');
    const carouselLinks = document.querySelectorAll('.carousel-href');
    console.log('CarouselLinks:', carouselLinks);
    console.log('NavLinks:', navLinks);



    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const urlNav = link.getAttribute('href');
            console.log('Nav link clicked:', urlNav); 
            loadContent(urlNav);
        });
    });

    
        
        
        
    
        carouselLinks.forEach(link => {
            link.addEventListener('click', function(event) {
                event.preventDefault();
                const url = link.getAttribute('href');
                console.log('Carousel link clicked:', url);
                loadContent(url);
            });
        });
    }, 2000); 
    
}










console.log('correcto')





function leerProductos(letraInicial){
    console.log('Letra recibida:', letraInicial);
    let res = document.querySelector('#res');
    res.innerHTML = '';
    fetch('https://raw.githubusercontent.com/leoogle/adoptme/main/jsons/data.json')
    .then(respuesta => respuesta.json())
    .then(productos => {
        console.log(productos.productos)
        const productosFiltrados = productos.productos.filter(item => item.idProducto.charAt(0).toLowerCase() === letraInicial);
        console.log(productosFiltrados)
        productosFiltrados.forEach(item =>{
            
            
                
            res.innerHTML += `
                <div class="col mb-4">
                    <div class="card mx-auto shadow" style="width: 18rem;">
                        <img src="${item.strImg}" class="card-img card-img-top" alt="...">
                            <div class="card-body">
                                <h7 class="card-text">${item.strNomproducto}</h7>
                                <p class="tit-modal1"> Descripción </p>
                                <p class= "descr-modal1">${item.strDescripcion}</p>
                                <h5 class="card-title" style="color: #FF460B">${item.strPrecio}</h5>
                
                            </div>
                    </div>
                </div>

                
                
                `
                

      
    })
        
    })
}



document.body.addEventListener('click', function(event) {
    if (event.target.classList.contains('boton-stl1')) {
        let clasesBoton = event.target.classList;
        if (clasesBoton.contains('c')) {
            console.log('Letra "c" detectada');
            leerProductos('c');
        } else if (clasesBoton.contains('j')) {
            console.log('Letra "j" detectada');
            leerProductos('j');
        } else if (clasesBoton.contains('h')) {
            console.log('Letra "h" detectada');
            leerProductos('h');
        }
        console.log('Clickeado');
    } else {
        console.log('No clickeado');
    }
});


document.body.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("contactForm");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        if (validateForm()) {
            
            alert("Formulario válido. Enviando datos...");
        }
    });

    function validateForm() {
        let isValid = true;
        const inputs = form.querySelectorAll("input, textarea");

        inputs.forEach(input => {
            if (!input.checkValidity()) {
                isValid = false;
                
                input.classList.add("is-invalid");
            } else {
                
                input.classList.remove("is-invalid");
            }
        });

        return isValid;
    }
});

document.body.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("contactForm");
    const fundacionSelect = document.getElementById("fundacion");

    fetch("https://raw.githubusercontent.com/leoogle/adoptme/main/jsons/fundaciones.json")
        .then(response => response.json())
        .then(data => {
            data.fundacion.forEach(fundacion => {
                const option = document.createElement("option");
                option.value = fundacion.id;
                option.textContent = fundacion.nombre;
                fundacionSelect.appendChild(option);
            });
        })
        .catch(error => console.error("Error al cargar las fundaciones:", error));

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        if (validateForm()) {
            alert("Formulario válido. Enviando datos...");
        }
    });

    function validateForm() {
        let isValid = true;
        const inputs = form.querySelectorAll("input, textarea, select");

        inputs.forEach(input => {
            if (!input.checkValidity()) {
                isValid = false;
                input.classList.add("is-invalid");
            } else {
                input.classList.remove("is-invalid");
            }
        });

        return isValid;
    }
});






