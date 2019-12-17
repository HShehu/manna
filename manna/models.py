from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    community = models.CharField(max_length=60)
    brief_description = models.TextField(max_length=100)
    ongoing = models.BooleanField(default=False)
    project_details = models.TextField()
    project_photo = models.ImageField(upload_to="manna", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk':self.pk})


class Phone_No(models.Model):
    p_num = PhoneNumberField()


class Email(models.Model):
    mail = models.EmailField()

class Account(models.Model):
    name = models.CharField(max_length=100)
    naira_number = models.CharField(max_length=20)
    dollar_number = models.CharField(max_length=20,null = True,blank= True)
    pound_number = models.CharField(max_length=20,null = True,blank= True)
    bank = models.CharField(max_length=100)
    def __str__(self):
        return self.bank
