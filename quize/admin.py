from django.contrib import admin

from quize.models import Teacher_Subject

# Register your models here.
class TeacherSubjectAdmin(admin.ModelAdmin):

    list_display = ('subject')


admin.site.register(Teacher_Subject)