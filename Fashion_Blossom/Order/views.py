from django.shortcuts import render,redirect,HttpResponse
from .models import *
from Product.models import Product

# Create your views here.
def item_add(request):
    u_id=request.user.id
    pid=request.POST.get('pid')
    color=request.POST.get('p_color')
    size=request.POST.get('p_size')
    qty=request.POST.get('product-quantity')
    prod=Product.objects.get(id=pid)
    prc=prod.price
    total=prc*int(qty)
    obj=Order_Items(user_id=u_id, product_id=pid, prod_color=color, prod_size=size, prod_qty=qty, total=total)
    obj.save()
    item=Order_Items.objects.get(id=obj.id)
    return render(request,'checkout.html',{'item':item})

def item_remove(request,odr_itm_id):
    order_item=Order_Items.objects.get(id=odr_itm_id)
    order_item.delete()
    return redirect('/')

def shipping_details(request):
    uid=request.user.id
    address=request.POST.get('address')
    zipcode=request.POST.get('zipcode')
    country=request.POST.get('country')
    state=request.POST.get('state')
    city=request.POST.get('city')
    phone=request.POST.get('phone')
    if Shipping_Address.objects.filter(user_id=uid,zipcode=zipcode).exists():
        return HttpResponse('Details Already Exist..')
    else:
        details=Shipping_Address(user_id=uid,address=address,zipcode=zipcode,country=country,state=state,city=city,phone_no=phone)
        details.save()
        msg=details.address+" "+details.phone_no
        return HttpResponse(msg)

def checkout(request):
    return render(request,'checkout.html')
