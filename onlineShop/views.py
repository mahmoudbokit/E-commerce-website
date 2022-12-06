from django.shortcuts import render, redirect
from .models import Product, Command, Comment
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'onlineShop/index.html', {'product_object': product_object})


def detail(request, product_id):
    product_object = Product.objects.get(id=product_id)
    return render(request, 'onlineShop/detail.html', {'product': product_object})


def checkout(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        totalPrice = request.POST.get('totalPrice')
        totalQuantity = request.POST.get('totalQuantity')
        items = request.POST.get('items')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        State = request.POST.get('State')
        zipcode = request.POST.get('zipcode')
        command = Command(name=name, email=email, address=address, city=city,
                          State=State, zipcode=zipcode, items=items,
                          totalPrice=totalPrice, totalQuantity=totalQuantity)
        commenter = Comment(name=name, comment=comment)
        commenter.save()
        command.save()
        return redirect('confirmation')

    return render(request, 'onlineShop/checkout.html')


def confirmation(request):
    message = Command.objects.all()[:1]
    for item in message:
        name = item.name

    return render(request, 'onlineShop/confirmation.html', {'name': name})