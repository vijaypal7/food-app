from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#landmark/town/city/district/state/pincode/phone_no.
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_post", on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    FOOD_CHOICES = (
        ('0', 'RAW'),
        ('1', 'FRESH'),
        ('2', 'OLD'),
    )
    type = models.CharField(max_length=1, choices=FOOD_CHOICES)
    amount = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    itime = models.DateTimeField(auto_now_add=True, blank=True)
    finaltime = models.DateTimeField(blank=True)
    landmark = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    dist = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

    pin = models.PositiveIntegerField()
    mobile = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('reg:list') # ,kwargs={'pk':self.pk}

    # def check_food(self):
    #     if


class Organisation(models.Model):
    user = models.OneToOneField(User,related_name="organisations", on_delete = models.CASCADE)
    Categ_CHOICES = (
        ('D', 'Donor'),
        ('F', 'Feeder'),
    )
    phone_no = models.CharField(max_length = 10)
    Name = models.CharField(max_length = 20)
    organisations = models.CharField(max_length=1, choices=Categ_CHOICES)


class address1(models.Model):
    user = models.OneToOneField(User,related_name="address", on_delete = models.CASCADE)
    house = models.CharField(max_length = 120,blank = True)
    street = models.CharField(max_length = 120,blank = True)
    area = models.CharField(max_length = 120,blank = True)
    pincode = models.CharField(max_length = 6,blank = True)
    district = models.CharField(max_length = 25,blank = True)
    state = models.CharField(max_length = 50,blank = True)
