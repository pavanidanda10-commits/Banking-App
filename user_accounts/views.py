from django.shortcuts import render

# Create your views here.


def signup(request):
   if request.method == "POST":
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        email = request.POST.get("email")
        print(email)
        password = request.POST.get("psw")
        confirm_password = request.POST.get("psw-repeat")
        print(fname,lname,email,password,confirm_password)
        return render(request,'user_accounts/signup.html')
   
    


