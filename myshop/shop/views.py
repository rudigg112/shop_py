from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserOurRegistration
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


def read_book(request, slug):

    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/zagovor-hranitelej-put-korolej/hraniteli-1.html', {'product': product})


def register(request):
    if request.method == "POST":
        form = UserOurRegistration(request.POST);
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/auth/')
    else:
        form = UserOurRegistration()
    return render(request, 'shop/authuser.html', {'form': form})
