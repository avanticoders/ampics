from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(default="profile.svg", upload_to="profiles/", null=True, blank=True)
    uploads = models.IntegerField(null=True, default=0)
    downloads = models.IntegerField(null=True, default=0)

    def __str__(self):
        return str(self.user)

class Upload(models.Model):
    CATEGORY = (
        ('Portrait', 'Portrait'),
        ('Landscape', 'Landscape'),
        ("Sports", "Sports"),
        ('Fashion', 'Fashion'),
        ('Technology', 'Technology'),
        ('Science', 'Science')
    )
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    caption = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    image = models.ImageField(null=True, blank=True, upload_to="uploads/")

    def __str__(self):
        return self.caption