from .models import *
from django.contrib.auth.models import User
from django import forms
from . import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
# from django.utils.translation import ugettext_lazy as _   
from datetime import datetime
# from bootstrap_datepicker_plus.widgets import DateTimePickerInp

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer 
        fields= ['phone_number','google_map','county','sub_county','local_town','profile_pic']


    def clean(self):
        super(CustomerForm, self).clean()

        phone_number = self.cleaned_data.get('phone_number')
        # google_map = self.cleaned_data.get('google_ma')

        if len(str(phone_number))<10:
            self._errors['phone_number'] = self.error_class(['must be a minimum of 10 characters'])                      

        return self.cleaned_data

class UserForm(forms.ModelForm):

    class Meta:
        model = User 
        fields = ['username','password','email']

    def clean(self):
        super(UserForm, self).clean()
        username = self.cleaned_data.get('username')
        if username.isnumeric():
            self._errors['username'] = self.error_class(['username cannot be numbers'])
        if len(username) < 5:
            self._errors['username'] = self.error_class(['username must be more than 5 characters'])


class ExpertForm(forms.ModelForm):

    class Meta:
        model = Expertise 
        fields= ['logo','google_map','dealings','dealing_list','county','sub_county','local_town','other_info','liscences','phone_number','photo']


    # def clean(self):
    #     super(CustomerForm, self).clean()

    #     phone_number = self.cleaned_data.get('phone_number')
    #     # google_map = self.cleaned_data.get('google_ma')

    #     if len(str(phone_number))<10:
    #         self._errors['phone_number'] = self.error_class(['must be a minimum of 10 characters'])                      

    #     return self.cleaned_data

class BussinessForm(forms.ModelForm):

    class Meta:
        model = Bussiness 
        fields= ['brand_name','logo','google_map','dealings','dealing_list','county','sub_county','local_town','other_info','liscences','phone_number','images']
        def clean(self):
            super(CustomerForm, self).clean()

            phone_number = self.cleaned_data.get('phone_number')
        # google_map = self.cleaned_data.get('google_ma')

            if len(str(phone_number))<10:
                self._errors['phone_number'] = self.error_class(['must be a minimum of 10 characters'])                      

            return self.cleaned_data
