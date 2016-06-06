// global variables
var csrftoken = getCookie('csrftoken');

$(function() {

    // add to cart
    $('.cart-add').click(function() {
        var data = {
            'product_id': $(this).data('product'),
            'csrfmiddlewaretoken': csrftoken,
        };
        
        $.post('/cart/add/', data, function(data) {
            console.log(data);
        });

        $(this).blur();
        return false;
    });

});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}