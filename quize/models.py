import uuid

from django.db import models

from account.models import CustomUser


# Create your models here.
class Teacher_Subject(models.Model):
    sub_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Question_Set(models.Model):
    OPTION1 = 'Easy'
    OPTION2 = 'Medium'
    OPTION3 = 'Difficult'
    OPTION4 = 'Hard'

    CHOICES = [
        (OPTION1, 'Easy'),
        (OPTION2, 'Medium'),
        (OPTION3, 'Difficult'),
        (OPTION4, 'Hard'),
    ]
    qs_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='Question_Sets')
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.CharField(
        max_length=10,
        choices=CHOICES,
        default=OPTION1)
    time_set = models.PositiveSmallIntegerField(default=5)
    is_deleted = models.BooleanField(default=False)


class Studen_Result(models.Model):
    result_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    qs_id = models.ForeignKey(Question_Set, on_delete=models.CASCADE)

    def __str__(self):
        return self.status


class Question(models.Model):
    question_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    qs_id = models.ForeignKey(Question_Set, on_delete=models.CASCADE)


class Answer(models.Model):
    answer_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
