from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    

class student(models.Model):
    lib_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    section=models.CharField(max_length=2)
    def __str__(self):
        return self.name

class mark(models.Model):
    maths = models.IntegerField()
    chemisty= models.IntegerField()
    c_programming=models.IntegerField()
    english=models.IntegerField()
    
    
    
class teacher(models.Model):
    lib_id=models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    father_name= models.CharField(max_length=200)
    email=models.EmailField( max_length=254)
    branch = models.CharField(max_length=50)
    section=models.CharField(max_length=2)
    contact=models.IntegerField()
    Dob=models.DateField(auto_now=False)
    address=models.TextField(max_length=1000)
    def __str__(self):
        return self.name




