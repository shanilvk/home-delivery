from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic import ListView
from .models import Cart,Orders
from items.models import foods
from django.contrib.auth.models import User
# from django.utils.decorators import method_decorator
from django.contrib import messages
from items.models import foods



class addcartv(View):
    def get(self,request,*args,**kwargs):
        food=foods.objects.get(id=kwargs.get('iid'))
        user=request.user
        Cart.objects.create(foods=food,user=user)
        messages.success(request,'product added to cart successfully')
        return redirect('index')
    
    
class cartshowview(ListView):
    template_name='cartshow.html'
    model=Cart
    context_object_name='cartitem'
    
    def get_queryset(self):
        cart=Cart.objects.filter(user=self.request.user,status='cart')
        # total=Cart.objects.filter(user=self.request.user).aggregate(tot=Sum("Books__price"))
        return {"item":cart}
    
    
def cartdeleteview(request,id):
    cd=Cart.objects.get(id=id)
    cd.delete()
    return redirect('cartshow')


class checkoutview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"checkout.html")
    def post(self,request,*args,**kwargs):
        id=kwargs.get('cid')
        cart=Cart.objects.get(id=id)
        food=cart.foods
        user=request.user
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        Orders.objects.create(foods=food,user=user,address=address,phone=phone)
        cart.status="order placed"
        cart.save()
        messages.success(request,"order placed successfully!!!")
        return redirect('index')
    
    