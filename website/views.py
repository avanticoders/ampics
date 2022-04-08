from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import Signin, AccountForm, UploadForm
from .models import Account, Upload
from .decorators import unauthenticated_user, allowed_users

from random import randint

# Create your views here.
@login_required(login_url='login')
def homepage(request):
    # Get all images in the database
    uploads = Upload.objects.all()

    return render(request, 'home.html', {'uploads':uploads})

@login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def search_images(request):
    if request.method == 'POST':
        searched = request.POST['search']
        image_results = Upload.objects.filter(caption__contains=searched) or Upload.objects.filter(category__contains=searched)

        if len(image_results) > 0:
            found = True
        else:
            found = False

        context = {'found': found, 'images':image_results}
        return render(request, 'search.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def user_profile(request):
    customer = request.user.account
    form = AccountForm(instance=customer)

    if request.method == 'POST':
        form = AccountForm(data=request.POST, files=request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            print(form)
            
    context = {'form':form}
    return render(request, 'user.html', context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def upload(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            caption = form.cleaned_data.get('caption')
            saved_form = Upload.objects.get(caption=caption)
            saved_form.account = request.user.account
            saved_form.save()
            acc = saved_form.account
            acc.uploads += 1
            acc.save()
            
            return redirect('home')

    context = {'form':form}
    return render(request, 'upload.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    all_users = User.objects.all()
    total_users = len(all_users)

    # Check for non-staff users
    active = 0
    for user in all_users:
        if user.is_active:
            if user.is_staff:
                pass
            else:
                active += 1

    accounts = Account.objects.all()
    uploads = len(Upload.objects.all())

    if total_users > 5:
        display_users = (total_users - 5)
    else:
        display_users = (total_users - 1)

    context = {'users' : all_users[display_users:], 'total_users' : total_users, 'active' : active, 'accounts':accounts[:7], 'uploads':uploads}
    return render(request, 'dashboard.html', context)

@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        form = Signin(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account created for " + user)

            return redirect('login')
    else:
        form = Signin()
    
    context = {'form' : form}
    return render(request, 'signin.html', context)

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username OR Password is incorect!")

    return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')