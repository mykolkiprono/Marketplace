from msilib import CAB
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    location = models.ImageField(upload_to="/photos/location")
    profile_pic = models.ImageField(upload_to="photos/profile_pics")

    def __str__(self):
      return self.name

class Bussiness(models.Model):
    choices =(
        ('entertainment','active'),
        ('technicians','dormant'),
        ('selling','dormant'),
        ('','dormant'),
        
    )
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="photos/logos")
    category = models.TextField(max_length=200) # bars,clubs,vets,technician,plumber
    location = models.ImageField()
    dealing_type = models.TextField(max_length=30) # products or services or both
    dealings = models.TextField(max_length=1000)
    # branches = models.TextField()
    other_info = models.TextField(max_length=200)
    liscences = models.ImageField(upload_to="/photos/liscences")
    rating = models.IntegerField()
    email = models.EmailField(max_length=154)
    phone_number = models.CharField(max_length=10)
    # subscribers = models.ForeignKey() # subject to change
    photo = models.ImageField(upload_to="photos/bussiness")

    def __str__(self):
       return self.name

class Branch(models.Model):
    location = models.CharField(max_length=254)
    googgle_map = models.ImageField(upload_to="photos/_google_loc") 

class Events(models.Model):
    categories =(
        ('political','active'),
        ('educational','dormant'),
        ('entertainment','dormant'),        
    )
    title = models.CharField(max_length=15)
    host = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    neccesary_info = models.TextField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    google_map = models.ImageField(upload_to="photos/_google_loc")
    category = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    visits = models.IntegerField() # filled after the visits are determined

    def __str__(self):
      return self.title

class Merchandise(models.Model):
    seller = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField()
    stock = models.IntegerField() # this can be blank for services
    photos = models.ImageField(upload_to="/images")
    video = models.FileField(upload_to="/videos")
    description = models.TextField(max_length=200)
    mode_of_delivery = models.TextField(max_length=50)
    state = models.BooleanField()
    rating = models.IntegerField()

    def __str__(self):
      return self.name

class Subscription(models.Model):
    customer = models.ForeignKey("Customer",on_delete=models.CASCADE)
    bussiness = models.ForeignKey()
    state = models.BooleanField()

    def __str__(self):
       return self.state

class Information(models.Model):
    sender = models.ForeignKey("Businness",on_delete=models.CASCADE)
    title = models.TextField(max_length=200)
    to = models.TextField(max_length=50)
    category = models.TextField(max_length=200)

    def __str__(self):
       return self.title
class Feedback(models.Model):
    customer = models.ForeignKey("Customer",on_delete=models.CASCADE)
    businness = models.ForeignKey("Bussiness",on_delete=,models.CASCADE)
    feed = models.TextField(max_length=200)

class Rating(models.Model):
    merch = models.ForeignKey("Merchandise",on_delete=models.CASCADE)
    rate = models.IntegerField()
    comment = models.TextField(max_length=200)
