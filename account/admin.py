from django.contrib import admin
from account.models import CustomUser


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'user_type')


admin.site.register(CustomUser, AccountAdmin)
