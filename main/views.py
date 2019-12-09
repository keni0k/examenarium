from django.shortcuts import render
from .forms import UserRegistrationForm, UserAuthForm


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if not request.user.is_staff and request.user.is_authenticated:
        pass
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/signin_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/signin.html', {'user_form': user_form})


def login(request):
    user_form = UserAuthForm()
    return render(request, 'registration/login.html', {'user_form': user_form})


def profile(request):
    return render(request, "account/profile.html")
