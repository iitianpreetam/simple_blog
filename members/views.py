from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm

# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'register/register.html'
#     success_url = reverse_lazy('login')


@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'login.html', context)


@unauthenticated_user
def register_view(request):
    form = UserRegisterForm()
    # role_form = RoleRegister()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # user_save = form.save()
            # if form.cleaned_data.get('is_doctor') == 'YES':
            #     set_group = Group.objects.get(name='doctor')
            #     user_save.groups.add(set_group)
            # else:
            #     set_group = Group.objects.get(name='commonUser')
            #     user_save.groups.add(set_group)
            form.save()

            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
