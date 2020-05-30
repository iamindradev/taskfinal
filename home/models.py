from django.db import models

# Create your models here.



class mark(models.Model):
    maths = models.IntegerField()
    chemisty= models.IntegerField()
    c_programming=models.IntegerField()
    english=models.IntegerField()
    
class student(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    section=models.CharField(max_length=2)
    def __str__(self):
        return self.name
        
    
class teacher(models.Model):

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

class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    


