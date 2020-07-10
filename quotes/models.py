from django.db import models

# Create your models here.
from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['name_input']) < 2:
            errors ['first_name'] = "Come on put a real name in !"
        if not EMAIL_REGEX.match(postData['email_input']):
            errors['email'] = 'not a real email retry!'
        if len(postData['password_input']) < 5:
             errors['password'] = 'you need 5 characters for a slight secure password'
        if postData['confirmpw_input'] != postData['password_input']:
            errors['confirm_pw'] = "Your password and what you typed in comfirm pw dont match try agian"
        return errors

    def quote_validator(self, postData):
        errors = {}
        if len(postData['quotedby_input'])<2:
            errors['author'] = 'someone said this quote that hade a name of two letter or more!'
        if len(postData['message_input'])< 10:
            errors['quote'] = 'you should have 10 characters to fill messages out.' 
        return errors      
        


class User(models. Model):
    first_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.CharField(max_length=255) 
    posted = models.ForeignKey(User, related_name="quotes", on_delete = models.CASCADE)
    objects = UserManager()