from rest_framework import serializers
from quize.models import Teacher_Subject

def validate_unique_subject(data):
    """
    Validate that the subject is unique for each user_email.
    """
    user_email = data['user_email']
    subject = data['subject']

    if Teacher_Subject.objects.filter(subject=subject, user_email=user_email).exists():
        raise serializers.ValidationError("This subject already exists for this user.")



