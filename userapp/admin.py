from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import *

from .models import *

# Register your models here.

class CustomAdmin(UserAdmin):


    form = CustomUserChangeForm

    add_form = CustomUserCreationForm

    model = CustomUser


admin.site.register(CustomUser, CustomAdmin)
