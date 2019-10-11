var imagenes = ['Img/img1.jpg', 'Img/img2.jpg', 'Img/img4.png', 'Img/img4.jpg'],
    cont = 0;

function carrousel(carrusel) {
    carrusel.addEventListener('click', e => {
        let atras = carrusel.querySelector('.atras'),
            adelante = carrusel.querySelector('.adelante'),
            img = carrusel.querySelector('img'),
            tgt = e.target;
        if (tgt == atras) {
            if (cont > 0) {
                img.src = imagenes[cont - 1];
                cont--;

            } else {
                img.src = imagenes[imagenes.length - 1];
                cont = imagenes.length - 1;
            }
        } else if (tgt == adelante) {
            if (cont < imagenes.length - 1) {
                img.src = imagenes[cont + 1];
                cont++;

            } else {
                img.src = imagenes[0];
                cont = 0;
            }
        }
    });

}




document.addEventListener("DOMContentLoaded", () => {
    let contenedor = document.querySelector('.carrusel');

    carrousel(contenedor);
});