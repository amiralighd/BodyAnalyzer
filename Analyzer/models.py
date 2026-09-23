from django.db import models
from django.conf import settings


class BodyAnalysis(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    weight = models.FloatField()
    height = models.FloatField()
    age = models.IntegerField()

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )

    blood_sugar = models.FloatField()
    cholesterol = models.FloatField()

    bmi = models.FloatField(
        null=True,
        blank=True
    )

    bmi_status = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    blood_sugar_status = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    cholesterol_status = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )