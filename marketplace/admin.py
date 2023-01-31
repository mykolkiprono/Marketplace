from ast import Sub
from symbol import subscript
from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    customers = Customer.objects.all().count()
    list_display=['brand_name','phone_number','county','local_town','sub_county','profile_pic','google_map']
    
admin.site.register(Customer,CustomerAdmin)

class ExpertiseAdmin(admin.ModelAdmin):
    customers = Expertise.objects.all().count()
    list_display=['brand_name','logo','google_map','dealing_list','dealings','county','sub_county','local_town','other_info','liscences','phone_number','photo']
    
admin.site.register(Expertise,ExpertiseAdmin)

class BussinessAdmin(admin.ModelAdmin):
    bussinesses = Bussiness.objects.all().count()
    list_display = ['user','brand_name','logo','google_map','dealings','dealing_list','county','sub_county','local_town','other_info','liscences','phone_number','images']

admin.site.register(Bussiness,BussinessAdmin)

class EventsAdmin(admin.ModelAdmin):
    events = Events.objects.all().count()
    list_display = ['title','host','category','start_time','end_time','place','google_map','neccesary_info','google_map','description']

admin.site.register(Events,EventsAdmin)

class MerchandiseAdmin(admin.ModelAdmin):
    merchs = Merchandise.objects.all().count()
    list_display = ['name','price','description','stock','images','video','mode_of_delivery']

admin.site.register(Merchandise,MerchandiseAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    subscriptions = Subscription.objects.all().count()
    list_display = ['customer','bussiness','state']

admin.site.register(Subscription,SubscriptionAdmin)

class NewsAdmin(admin.ModelAdmin):
    information = News.objects.all().count()
    list_display = ['title','category','outlet','message']

class NewsReadsAdmin(admin.ModelAdmin):
    information = NewsReads.objects.all().count()
    list_display = ['news','reads','likes']

admin.site.register(NewsReads,NewsReadsAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    feeds = Feedback.objects.all().count()
    list_display = ['customer','bussiness','feed']

admin.site.register(Feedback,FeedbackAdmin)

class RatingServiceAdmin(admin.ModelAdmin):
    ratings = RatingService.objects.all().count()
    list_display = ['merch','rate','comment']

admin.site.register(RatingService,RatingServiceAdmin)

class RatingBussinessAdmin(admin.ModelAdmin):
    ratings = RatingBussiness.objects.all().count()
    list_display = ['bussiness','rate','comment']

admin.site.register(RatingBussiness,RatingBussinessAdmin)


class RatingProductAdmin(admin.ModelAdmin):
    ratings = RatingProduct.objects.all().count()
    list_display = ['product','rate','comment']

admin.site.register(RatingProduct,RatingProductAdmin)


class ReferBussinesAdmin(admin.ModelAdmin):
    ratings = ReferBussiness.objects.all().count()
    list_display = ['referee','refered','bussiness','message']

admin.site.register(ReferBussiness,ReferBussinesAdmin)


class ReferProductAdmin(admin.ModelAdmin):
    ratings = ReferProduct.objects.all().count()
    list_display = ['referee','refered','product','message']

admin.site.register(ReferProduct,ReferProductAdmin)


class ReferExpertAdmin(admin.ModelAdmin):
    ratings = ReferExpert.objects.all().count()
    list_display = ['referee','refered','expert','message']

admin.site.register(ReferExpert,ReferExpertAdmin)


class TestimoniesBussinessAdmin(admin.ModelAdmin):
    ratings = TestimoniesBussiness.objects.all().count()
    list_display = ['customer','bussiness','testimony']

admin.site.register(TestimoniesBussiness,TestimoniesBussinessAdmin)


class TestimoniesExpertAdmin(admin.ModelAdmin):
    ratings = TestimoniesExpert.objects.all().count()
    list_display = ['customer','expert','testimony']

admin.site.register(TestimoniesExpert,TestimoniesExpertAdmin)