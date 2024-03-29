from django.shortcuts import render,redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages

class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        return render(request, 'app/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles})

class ProductDetailsView(View):
 def get(self, request, pk):
  product =Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html', {'product':product})
 
 
def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product =Product.objects.get(id=product_id)
 #print(product_id)
 Cart(user=user, product= product).save()
 return redirect('/cart')

def show_cart(request):
   if request.user.is_authenticated:
      user = request.user
      cart = Cart.objects.filter(user=user)
      amount =0.0
      shipping_amount=70.0
      total_amount =0.0
      cart_product =[p for p in Cart.objects.all() if p.user == user]
     
      print(cart_product)
      if cart_product:
        for p in cart_product:
            tempamount =(p.quantity * p.product.discounted_price)
            amount += tempamount
            totalamount = amount + shipping_amount
        return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount':totalamount, 'amount':amount})
      else:
         return render(request, 'app/emptycart.html', {'carts': cart, 'totalamount':totalamount, 'amount':amount})

  
     
      



def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 add = Customer.objects.filter(user = request.user)
 return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

#def change_password(request):
 #return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data is None:
        mobiles = Product.objects.filter(category='M')
    elif data == "Realme" or data == 'Samsung' or data == 'Vivo':
        mobiles = Product.objects.filter(category='M').filter(brand=data)

    elif data == "below":
        mobiles = Product.objects.filter(category='M', discounted_price__lt=10000)
    elif data == "above":
        mobiles = Product.objects.filter(category='M', discounted_price__gt=10000)
   
    else:
        mobiles = Product.objects.none()  # or handle other cases

    return render(request, 'app/mobile.html', {'mobiles': mobiles})


 
#def customerregistration(request):
 #return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
  def get(self, request):
    form = CustomerRegistrationForm()
    return render(request,'app/customerregistration.html',{'form':form})
  
  def post(self, request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      messages.success(request,'Congratulations!! Registered Successfully')
      form.save()
    return render(request,'app/customerregistration.html',{'form':form})


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            # Use lowercase 'user' instead of 'User'
            reg = Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')

        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
