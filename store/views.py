from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, FavouriteItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import JsonResponse



def home(request):
    categories = ['Moisturizer', 'Shampoo', 'Face Wash', 'Sun Screen']
    products = Product.objects.all()

    favourite_products = []
    if request.user.is_authenticated:
        favourite_products = Product.objects.filter(favouriteitem__user=request.user)

    return render(request, 'store/home.html', {
        'categories': categories,
        'products': products,
        'favourite_products': favourite_products
    })



def products(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})


@require_POST
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cart_count = CartItem.objects.filter(user=request.user).count()
        return JsonResponse({'success': True, 'cart_count': cart_count})

    return redirect('store:cart')

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'cart_items': cart_items})


@login_required
def favourites_view(request):
    favourite_items = FavouriteItem.objects.filter(user=request.user)
    return render(request, 'store/favourites.html', {'favourite_items': favourite_items})




@require_POST
@login_required
def add_to_favourites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favourite, created = FavouriteItem.objects.get_or_create(user=request.user, product=product)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        fav_count = FavouriteItem.objects.filter(user=request.user).count()
        return JsonResponse({'success': True, 'favourite_count': fav_count})

    return redirect(request.META.get('HTTP_REFERER', 'store:home'))

def register(request):
    if request.user.is_authenticated:  # Prevent logged-in users from accessing the register page
        return redirect('store:home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect('store:login')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('store:home')  # Redirect to home after login
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('store:home')  # After logging out, redirect to home page
@login_required
def profile_view(request):
    return render(request, 'store/profile.html')