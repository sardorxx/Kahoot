from django.contrib import admin
from account.models import CustomUser, TeacherSettings


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'user_type')


admin.site.register(CustomUser, AccountAdmin)


class TeacherSettingsAdmin(admin.ModelAdmin):
    list_display = ('teacher_settings_id', 'join_date')


admin.site.register(TeacherSettings, TeacherSettingsAdmin)
