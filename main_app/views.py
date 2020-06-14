from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.mail import send_mail, mail_admins
from django.shortcuts import render, redirect
from django.views.generic import ListView
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser
from .models import Tire, Cart, CartDetail


def home(req):
  return render(req, 'home.html')

def signup(req):
    if req.method == 'POST':
      form = CustomUserCreationForm(req.POST)
      if form.is_valid():
        user = form.save() # Add the user to the database
        login(req, user) #logs in on signup
        email = user.email
        
        send_mail(
          'Thank you for registering',
          'You registered with {user.company_name}. Please wait to be verified before shopping. If urgent, please contact us during business hours at 111-111-1111',
          'settings.EMAIL_HOST_USER',
          [email],
          fail_silently=False
        )
        mail_admins(
          'new signup: {user.company_name}',
          'this user needs to be verified.',
          fail_silently=False
        )

        return redirect('account')
    else:
      form = CustomUserCreationForm()
    return render(req, 'signup.html', {'form': form}) # redirect to signup page

def signin(req):
  if req.user.is_authenticated:
    return redirect('tire_list')

  if req.method == 'POST':
    username = req.POST.get('username').lower()
    password = req.POST.get('password')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(req, user)
      return redirect('tire_list')

    else: 
      messages.error(req, 'Wrong email/password')
  
  form = CustomUserCreationForm()
  return render(req, 'signup.html', {'form': form})

def logout(req):
  auth.logout(req)
  return render(req, 'home.html')

def account(req):
  user = req.user
  carts = Cart.objects.filter(user_id=req.user.id).order_by('-date_ordered')
  return render(req, 'account.html', { 'user': user, 'carts': carts })

def custom_user_edit(req):
  user = req.user
  form = CustomUserChangeForm(instance=user) #initiates form with user info
  if req.method == 'POST': # will only show validation errors on POST, not GET
    form = CustomUserChangeForm(req.POST, instance=user) #'instance=user' ensures you are overwriting current user and NOT creating a new one with same info
    if form.is_valid():
      user_update = form.save(commit=False)
      user_update.is_active = False # turns user to inactive and kicks them out
      form.save() # saves all the info
      return redirect('account')
  context = {
    "form": form
  }
  return render(req, 'custom_user_edit_form.html', context)

# THIS USES DJANGO PURE FORMS AND IS LEFT IN AS AN EXAMPLE
# def custom_user_edit(request):
#   form = CustomUserEditForm() #initiates form 
#   if request.method == 'POST': # will only show validation errors on POST, not GET
#     form = CustomUserEditForm(request.POST)
#     if form.is_valid():
#       user = CustomUser(**form.cleaned_data) # uses all form data to create a user
#       user.id = request.user.id # makes sure info is tied to current user
#       user.date_joined = request.user.date_joined
#       user.discount_ratio = request.user.discount_ratio
#       user.is_active = True # turns user to inactive
#       user.is_staff = False
#       user.is_superuser = True # ONLY KEEPING FOR TESTING PURPOSES
#       user.save() # saves all the info
#   context = {
#     "form": form
#   }
#   return render(request, 'custom_user_edit_form.html', context)

def about(req):
  return render(req, 'about.html')

def services(req):
  return render(req, 'services.html')

def tires(req):
  return render(req, 'tires.html')

def cartDetail(req):
  return render(req, 'cart.html')

def orderDetail(req, cart_id):
  order = Cart.objects.get(id=cart_id)
  order_detail = CartDetail.objects.filter(cart_id=cart_id)
  return render(req, 'order_detail.html', { 'order': order, 'order_detail': order_detail })

def orderCancel(req, cart_id):
  order = Cart.objects.get(id=cart_id)
  order.status = 2
  order.save()
  return redirect('order_detail', cart_id)

class TireList(ListView):
  model = Tire