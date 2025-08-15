from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
    path('about/', views.aboutus, name='aboutus'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.product_search, name='product_search'),
    path('login/', views.login_view, name='login'),
    path('blog/', views.blog, name='blog'),
    path('categories/', views.categories_view, name='categories'),
    path('categories/<slug:slug>/', views.category_view, name='category_page'),
    path('cakes/', views.cakes_view, name='cakes'),
     path("wishlist/", views.wishlist_view, name="wishlist"),
     path('sweets/', views.sweets_view, name='sweets'),
     path('product_detail/', views.product_detail_view, name='product_detail'),
      path('cart/', views.cart_view, name='cart'),
       path('pastries/', views.pastries_view, name='pastries'),

 
]
