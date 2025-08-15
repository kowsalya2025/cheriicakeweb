from .models import MenuItem

def navbar_context(request):
    return {
        'menu_items': MenuItem.objects.all()
    }
