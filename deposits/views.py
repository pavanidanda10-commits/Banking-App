from django.shortcuts import render


# Create your views here.
def deposits(request):
   return render(request, 'deposits/deposits.html')