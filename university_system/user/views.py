from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def index(request) :
    return render(request, template_name="home.html")
def login_enrollee(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("fail")

    return render(request=request, template_name="login-enrollee.html", context={})

def login_commission(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            return HttpResponse("fail")

    return render(request=request, template_name="login-commission.html", context={})
def signupuser(request):

    User = get_user_model()
    if request.user.is_authenticated:
        return render(request=request, template_name="home.html")

    if request.method == 'POST':
        first_name = request.POST.get('firstname', '')
        last_name = request.POST.get('lastname', '')
        father_name = request.POST.get('fathername', '')
        date_of_birth = request.POST.get('dateofbirth', '')
        gender = request.POST.get('gender', '')
        citizenship = request.POST.get('citizenship', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phonenumber', '')
        password = request.POST.get('password', '')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, father_name=father_name,
                                        date_of_birth=date_of_birth, gender=gender, citizenship=citizenship,
                                        email=email, phone_number=phone_number, password=password)

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home")

    return render(request=request, template_name="signup.html", context={})


def sign_out(request):
    logout(request)
    return redirect('home')


def room(request):
    return render(request, template_name="user-room.html")


