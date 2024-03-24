from rest_framework import serializers

from account.models import CustomUser
from quize.models import Teacher_Subject


def validate_unique_subject(data):
    """
    Validate that the subject is unique for each user_email.
    """
    user_email = data['user_email']
    subject = data['subject']
    user = CustomUser.objects.get(email=user_email)

    if (not Teacher_Subject.objects.filter(subject=subject, user_email=user_email).exists() and
            user.user_type == "Teacher"):
        pass
    elif user.user_type != "Teacher":
        raise serializers.ValidationError("You are not teacher")
    else:
        raise serializers.ValidationError("This subject already exists for this user.")
