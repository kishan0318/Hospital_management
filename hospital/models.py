from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Department(models.Model):
    d_name=models.CharField(max_length=50)
    d_desc=models.CharField(max_length=200)
    d_image=models.ImageField()
    dr_name=models.CharField(max_length=70)
    def __str__(self):
       return self.d_name

class Contact(models.Model):
    title = models.CharField(max_length=3, choices=TITLE_CHOICES,default="")
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    querry=models.TextField()
    def __str__(self):
       return self.name 
    def get_absolute_url(self):
      return reverse('hospital:contact')

INTEGER_CHOICES= [tuple([x,x]) for x in range(0,100)]

class Appointment(models.Model):
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=50)
    age = models.IntegerField(choices=INTEGER_CHOICES)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    address=models.TextField()
    description=models.CharField(max_length=300)
    previous_prescription=models.FileField(default=None,blank=True)
    notes=models.TextField(default=None,null=True)
    date = models.DateField(default=date.today,blank="True",help_text="YYYY/MM/DD")
    def __str__(self):
       return self.email
    def get_absolute_url(self):
      return reverse('hospital:appointments')
   
class Beds(models.Model):
   Total_beds = models.IntegerField(default=None)
   Avilable_beds = models.IntegerField(default=None)
   def get_absolute_url(self):
      return reverse('hospital:bed')
