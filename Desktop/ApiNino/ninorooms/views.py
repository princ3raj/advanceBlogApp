from django.shortcuts import render, redirect

from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

from .models import NinoRooms, User

from django.urls import reverse

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from .forms import NinoCreateView

from django.contrib.auth.decorators import login_required


# Create your views here.




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "ninorooms/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "ninorooms/login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "ninorooms/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "ninorooms/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "ninorooms/register.html")



def PgRegistration(request):

    if request.method !='POST':
        form=NinoCreateView()
    
    else:       #Post data submitted; process data.
        form=NinoCreateView(request.POST,request.FILES)
        if form.is_valid():
            new_pg=form.save(commit=False)
            new_pg.user=request.user
            new_pg.save()
            return redirect('success')


    context={'form':form}
    return render(request,"ninorooms/pg_registration.html",context)

@login_required
def success(request):
    return render(request,"ninorooms/success.html")


