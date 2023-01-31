from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

# class MyValidator(ASCIIUsernameValidator):
#     regex = r'^[\w.@+-\s]+$'


# class MyUser(User):
#     username_validator = MyValidator()

#     class Meta:
#         proxy = True  # If no new field is added.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    brand_name = models.CharField(max_length=20,default="none")
    phone_number = models.CharField(max_length=10)
    google_map = models.URLField(null=True,blank=True) #change
    county = models.CharField(max_length=15)
    sub_county = models.CharField(max_length=15,null=True)
    local_town = models.CharField(max_length=15,null=True)
    profile_pic = models.ImageField(upload_to="photos/profiles",null=True,blank=True)

    def __str__(self):
      return self.user.username

class Bussiness(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    brand_name = models.CharField(max_length=20,default="none")
    logo = models.ImageField(upload_to="photos/logos",null=True,blank=True)
    google_map = models.URLField()
    dealing_list = models.CharField(max_length=50,default="selling")
    dealings = models.CharField(max_length=1000)
    other_info = models.CharField(max_length=200,null=True,blank=True)
    liscences = models.ImageField(upload_to="photos/liscences",null=True,blank=True)
    phone_number = models.CharField(max_length=10)
    images = models.FileField(upload_to="photo/bussiness",null=True,blank=True)
    county = models.CharField(max_length=15,default="meru")
    sub_county = models.CharField(max_length=15,default="nchiru")
    local_town = models.CharField(max_length=15,default="nchiru")

    def __str__(self):
       return self.user.username

class Expertise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    brand_name = models.CharField(max_length=20,default="none")
    logo = models.ImageField(upload_to="photos/logos",null=True,blank=True)
    google_map = models.URLField()
    dealing_list = models.CharField(max_length=50,default="selling") # products or services or both
    dealings = models.TextField(max_length=1000) # descibe what you do
    county = models.CharField(max_length=15,default="meru")
    sub_county = models.CharField(max_length=15,default="nchiru")
    local_town = models.CharField(max_length=15,default="nchiru")
    other_info = models.TextField(max_length=200,null=True,blank=True)
    liscences = models.ImageField(upload_to="photos/liscences",null=True,blank=True)
    phone_number = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="photos/bussiness",null=True,blank=True)

    def __str__(self):
       return self.user.username

class Branch(models.Model):
    location = models.CharField(max_length=254)
    googgle_map = models.ImageField(upload_to="photos/google_map/Branch") 

class Events(models.Model):
    categories =(
        ('political','active'),
        ('educational','educational'),
        ('entertainment','entertainment'),    
        ('other','other'),      
    )
    title = models.CharField(max_length=15)
    host = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    neccesary_info = models.TextField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    google_map= models.URLField()
    # google_map = models.ImageField(upload_to="photos/google_maps/events")
    category = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    # visits = models.IntegerField(null=True,blank=True) # filled after the visits are determined
    place = models.CharField(max_length=30)

    def __str__(self):
      return self.title

class Merchandise(models.Model):
    seller = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(null=True) # this can be blank for services
    images = models.FileField(upload_to="photo/bussiness")
    video = models.FileField(upload_to="videos")
    description = models.TextField(max_length=200)
    mode_of_delivery = models.TextField(max_length=50)
    upload_time = models.DateField(null=True,blank=True) # subject to change

    def __str__(self):
      return self.name

class StateMerchandise(models.Model):
    merchendise = models.ForeignKey("Merchandise",on_delete=models.CASCADE)
    available = models.BooleanField()
    description = models.TextField(max_length=50, null=True,blank=True)

class DiscountMerchandise(models.Model):
    product = models.ForeignKey("Merchandise",on_delete=models.CASCADE)
    discount = models.IntegerField()
    duration = models.DurationField()

class DiscountService(models.Model):
    service = models.ForeignKey("Service",on_delete=models.CASCADE)
    discount = models.IntegerField()
    duration = models.DurationField()

class Service(models.Model):
    seller = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    charges = models.DecimalField(max_digits=6, decimal_places=2)
    images = models.FileField(upload_to="photo/bussiness")
    video = models.FileField(upload_to="videos")
    description = models.TextField(max_length=200)
    mode_of_delivery = models.TextField(max_length=50)
    operation_time = models.DateField()
    # state = models.BooleanField() #whether it is sold or out of stock

    def __str__(self):
      return self.name

class StateService(models.Model):
    service = models.ForeignKey("Service",on_delete=models.CASCADE)
    available = models.BooleanField()
    description = models.TextField(max_length=50, null=True,blank=True)

class Subscription(models.Model):
    customer = models.ForeignKey("Customer",on_delete=models.CASCADE)
    bussiness = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    state = models.BooleanField()

    def __str__(self):
       return str(self.state)

class News(models.Model): 
    outlet = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    title = models.TextField(max_length=200)
    message = models.TextField(max_length=500)
    category = models.TextField(max_length=200)
    date = models.DateField() # change 

    def __str__(self):
       return self.title

class NewsReads(models.Model):
    news = models.ForeignKey("News",on_delete=models.CASCADE)
    reads = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()

class Feedback(models.Model):
    customer = models.ForeignKey("Customer",on_delete=models.CASCADE)
    bussiness = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    feed = models.TextField(max_length=200)

    def __str__(self):
       return self.feed

class RatingService(models.Model):
    merch = models.ForeignKey("Merchandise",on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    comment = models.TextField(max_length=200)

    def __str__(self):
       return self.comment

class RatingExpertise(models.Model):
    expert = models.ForeignKey("Expertise",on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    comment = models.TextField(max_length=200)

    def __str__(self):
       return self.comment

class RatingBussiness(models.Model):
    bussiness = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    comment = models.TextField(max_length=200)

    def __str__(self):
       return self.comment

class RatingProduct(models.Model):
    product = models.ForeignKey("Merchandise",on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    comment = models.TextField(max_length=200)

    def __str__(self):
       return self.comment

class ReferBussiness(models.Model):
    referee = models.CharField(max_length=30)
    # referee = models.OneToOneField(User,on_delete=models.CASCADE)
    refered = models.ForeignKey("Customer",on_delete=models.CASCADE)
    bussiness = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    message = models.TextField(max_length=50,default="none")

class ReferProduct(models.Model):
    referee = models.CharField(max_length=30)
    refered = models.ForeignKey("Customer",on_delete=models.CASCADE)
    product = models.ForeignKey("Merchandise",on_delete=models.CASCADE)
    message = models.TextField(max_length=50,default="none")

class ReferExpert(models.Model):
    referee = models.CharField(max_length=30)
    refered = models.ForeignKey("Customer",on_delete=models.CASCADE)
    expert = models.ForeignKey("Expertise",on_delete=models.CASCADE)
    message = models.TextField(max_length=50,default="none")

class TestimoniesBussiness(models.Model):
    customer = models.ForeignKey("Customer",on_delete=models.CASCADE)
    bussiness = models.ForeignKey("Bussiness",on_delete=models.CASCADE)
    testimony = models.TextField(max_length=200)

class TestimoniesExpert(models.Model):
    customer = models.ForeignKey("Customer",on_delete=models.CASCADE)
    expert = models.ForeignKey("Expertise",on_delete=models.CASCADE)
    testimony = models.TextField(max_length=200)
