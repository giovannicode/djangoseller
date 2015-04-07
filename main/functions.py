from carts.models import Cart

def get_cart(view):
    request = view.request

    if request.user.is_authenticated():
        cart = request.user.cart
    else:
        # May update try-catch later, as I think it is an ugly implementation.
        # Settin modified to True will make sure that session_key is not None
        try: 
            request.session.modified = True
            request.session.save()
            cart = Cart.objects.get(session_key=request.session.session_key)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(session_key=request.session.session_key)
    return cart

