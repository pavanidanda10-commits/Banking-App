from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

@ensure_csrf_cookie
def account_opening(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        role = request.POST.get('role', '').strip()

        # checkbox booleans: present when checked
        is_staff = bool(request.POST.get('is_staff'))
        is_active = bool(request.POST.get('is_active'))  # default True if your form checks it
        kyc_verified = bool(request.POST.get('kyc_verified'))
        is_superuser = bool(request.POST.get('is_superuser'))

        # Basic validation
        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect(request.path)

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect(request.path)

        # create_user handles password hashing
        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        first_name=first_name,
                                        last_name=last_name,
                                        phone=phone,
                                        role=role or 'CUSTOMER',
                                        is_staff=is_staff,
                                        is_active=is_active,
                                        kyc_verified=kyc_verified,
                                        is_superuser=is_superuser,
                                        date=timezone.now().date())

        user.save()

        messages.success(request, "Account created successfully.")
        return redirect('account_opening')

    return render(request, 'users/account_opening.html')