from discord.models import User
from django.contrib import admin


from .models import Room, User

# Register your models here.

admin.site.register(User)
admin.site.register(Room)
