from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.files.images import ImageFile
from helper_app.models import User_profile
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def Profile(request):
    context = {} 
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.filter(id=user_id).first()
        if user is not None:
            context = {
                'user_item': User.objects.get(id=user_id),
                'email': user.email,
                'uploaded_imgs': User_profile.objects.filter(uploader_id=user_id),
                'count': User_profile.objects.filter(uploader_id=user_id).count(),
            }
            if request.method == 'POST':
                img = request.FILES['Img']
                instance = User_profile(uploader_id = user_id, img = ImageFile(img))
                instance.save()
                return redirect('profile')  # Refresh the page
        else:
            print("User not found.")
    return render(request, 'profile.html', context)
def Signup(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(username, email, password)
        my_user = User.objects.create_user(username, email, password)
        my_user.save()
        return redirect("login")
    
    return render(request, "signup.html")

def Login(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, "login.html")

def Logout(request):
    logout(request)
    return redirect("login")