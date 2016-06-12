// global variables
var csrftoken = getCookie('csrftoken');

$(function() {
    // add tooltips
    $('[data-toggle="tooltip"]').tooltip();

    //
    // add to cart
    //
    $('.cart-add').click(function() {
        var link = this;
        var data = {'product_id': $(this).data('product')};
        $.post('/cart/add/', data, function(data) {
            var current_count = parseInt($('#cart_count').text());
            $('#cart_count').text(current_count + 1);
            $(link).hide();
        });
        $(this).blur();
        return false;
    });

    // delete from cart
    $('.cart-remove').click(function() {
        var link = this;
        var data = {'product_id': $(this).data('product')};
        $.post('/cart/remove/', data, function(data) {
            var current_count = parseInt($('#cart_count').text());
            $('#cart_count').text(current_count - 1);
            $(link).closest('tr').hide();
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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});