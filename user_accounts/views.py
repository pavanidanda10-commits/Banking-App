from django.shortcuts import render
from user_accounts.models import UserAccount
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def signup(request):
    
    if request.method == "POST":
        fname = request.POST.get("first_name")
        lname = request.POST.get("last name")
        email = request.POST.get("email")
        password = request.POST.get("psw")
        confirm_password = request.POST.get("psw-repeat")
        print(fname,lname,email,password,confirm_password)
        if password != confirm_password:
            return render(request,'user_accounts/signup.html',{
                "error":"Password and Confirm password do not match"
            })
        if UserAccount.objects.filter(email=email).exists():
            return render(request,'user_accounts/signup.html',{
                "error":"User with this email already exists"
            })

        UserAccount.objects.create(
            first_name = fname,
            last_name = lname,
            email = email,
            password = password,
        )
        # send_mail(
        #     subject = "Welcome to My Bank",
        #     message= f"Hi {fname}, welcome to my bank. your username setup is successfull",
        #     from_email = settings.DEFAULT_FROM_EMAIL,
        #     recipient_list= {email}
        # )
        return render(request,'user_accounts/signup.html')
    return render(request,'user_accounts/signup.html')










