from django.shortcuts import render

# Create your views here.

def account_opening(request):
    return render(request, 'home/account_opening.html')
def home(request):
    return render(request, 'home/home.html')
    
