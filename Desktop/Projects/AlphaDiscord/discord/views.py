from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User, Room
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


import datetime


# Create your views here.


@login_required
def index(request):

    x = datetime.datetime.now()

    time_for_user = x.strftime("%X")[:5]
    email = request.user.email
    location = "Nowhere"
    # location = request.geolocation

    username = request.user.username
    lst = []

    rooms = Room.objects.all()
    for room in rooms:
        lst.append(list(room.users.all()))

    temp_user = []
    new_users = []
    for user in lst:
        for t in user:
            temp_user.append(t.username)
        new_users.append(temp_user)
        temp_user = []

    count = 0
    room_id = []
    for check_user in new_users:
        if str(request.user) in check_user:
            room_id.append(count)
            count += 1
    final_room_object = []
    for i in room_id:
        final_room_object.append(rooms[i])

    print(final_room_object)

    return render(request, 'discord/index.html', {'rooms': final_room_object, 'username': username,'time':time_for_user,'location':location,'email':email})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "registration/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "registration/register.html")
