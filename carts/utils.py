from carts.models import Carts

def get_user_cart(request):
    if request.user.is_authenticated:
        return Carts.objects.filter(user=request.user)
    
    if not request.session.session_key:
        request.session.create()
    return Carts.objects.filter(session_key=request.session.session_key)