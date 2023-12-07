from django.db import models

# Possible improvement: move ROLE_CHOICES to a new folder for constants.
ROLE_CHOICES = (
        (False, 'Regular - Can\'t delete members'),
        (True, 'Admin - Can delete members'),
    )

class Member(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    role = models.BooleanField(default=False, choices=ROLE_CHOICES)
