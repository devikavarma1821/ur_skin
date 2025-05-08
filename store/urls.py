from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'store'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),


    path('favourites/', views.favourites_view, name='favourites'),
    path('cart/', views.cart_view, name='cart'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-favourites/<int:product_id>/', views.add_to_favourites, name='add_to_favourites'),


]
