from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from datetime import datetime



def home(request):
    return render(request, 'main/home.html')

def blog(request):
    return render(request, 'main/blog.html')

def aboutus(request):
    return render(request, 'main/aboutus.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'main/products.html', {'products': products})

def contact(request):
    return render(request, 'main/contact.html')

def login_view(request):
    return render(request, 'main/login.html')

def product_search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'main/products.html', {'products': results, 'query': query})


def homepage(request):
    context = {
        "shop_categories": Category.objects.all(),
        "company_address": "No.45, Anna Salai, T. Nagar, Chennai - 600 017",
        "company_email": "info@cherii.com",
        "company_phone": "+123 456 7890",
        "social": {
            "instagram": "https://instagram.com/cherii",
            "linkedin": "https://linkedin.com/company/cherii",
            "facebook": "https://facebook.com/cherii",
            "youtube": "https://youtube.com/cherii"
        },
        "year": datetime.now().year
    }
    return render(request, "home.html", context)


# Show all products (all categories)
def categories_view(request):
    products = Product.objects.all()
    return render(request, 'main/products.html', {'products': products})


# Show products from a single category
def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'main/products.html', {
        'products': products,
        'category': category
    })

def cakes_view(request):
    cakes = Product.objects.all()
    return render(request, 'main/cakes.html', {'cakes': cakes})

def pastries_view(request):
     pastries = Product.objects.all()
     return render(request, 'main/pastries.html', {'pastries': pastries})

def wishlist_view(request):
    return render(request, "main/wishlist.html")

def sweets_view(request):
    sweets = Product.objects.all()
    return render(request, 'main/sweets.html', {'sweets': sweets})

def product_detail_view(request):
    name = request.GET.get('name')
    price = request.GET.get('price')
    image = request.GET.get('image')
    description = request.GET.get('description')

    context = {
        'name': name,
        'price': price,
        'image': image,
        'description': description,
    }
    return render(request, 'main/product_detail.html', context)

def cart_view(request):
    return render(request, "main/cart.html") 


