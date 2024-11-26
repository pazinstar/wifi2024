from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserBalance
from django.utils import timezone

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
    
        user = UserBalance.objects.filter(username=username).first()
       
        if user:
            return redirect('balance:show_balance', username=username)
        else:
            messages.error(request, 'User does not exist. Contact admin.')
    return render(request, 'balance/home.html')

def show_balance(request, username):
    user = UserBalance.objects.get(username=username)
    return render(request, 'balance/show_balance.html', {'user': user})
def Contact_view(request):
    
    return render(request, 'balance/contact.html')

def external_page(request):
    # Replace 'https://www.example.com' with the actual external link you want to display
    external_url = 'https://bluecash.co.ke/new_phone_deposit/'
    return render(request, 'balance/external_page.html', {'external_url': external_url})
from django.shortcuts import redirect

from django.shortcuts import redirect

def admin_login_view(request):
    # Redirect to the admin login page
    return redirect('admin:login')

    
   
