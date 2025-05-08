from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

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
    path('favourites/', views.favourites_view, name='favourites'),
    path('cart/', views.cart_view, name='cart'),


]
# Serve static and media files in development (only for DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])