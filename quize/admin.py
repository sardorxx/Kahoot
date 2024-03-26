from django.contrib import admin

from quize.models import Teacher_Subject, Question_Set, Question


# Register your models here.
class TeacherSubjectAdmin(admin.ModelAdmin):
    list_display = 'subject'


admin.site.register(Teacher_Subject)


class QuestionSetAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'subject', 'level']


admin.site.register(Question_Set, QuestionSetAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_date']


admin.site.register(Question, QuestionAdmin)
