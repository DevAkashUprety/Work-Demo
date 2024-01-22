$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$(document).ready(function () {
    $('.plus-cart').click(function () {
        var productId = $(this).attr('pid');
        var quantityElement = $(this).siblings('#quantity');
        var currentQuantity = parseInt(quantityElement.text());

        quantityElement.text(currentQuantity + 1);

        console.log('Incremented quantity for product ID:', productId);
    });

    $('.minus-cart').click(function () {
        var productId = $(this).attr('pid');
        var quantityElement = $(this).siblings('#quantity');
        var currentQuantity = parseInt(quantityElement.text());

        if (currentQuantity > 1) {
            quantityElement.text(currentQuantity - 1);

            console.log('Decremented quantity for product ID:', productId);
        }
    });

    $('.remove-item').click(function () {
        var productId = $(this).attr('pid');

        console.log('Removed item for product ID:', productId);
    });
});