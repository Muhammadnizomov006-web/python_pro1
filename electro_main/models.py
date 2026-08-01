from django.db import models

# Create your models here.



class Catigorya(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to='./img')
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Catigorya,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='./img')
    chegirma=models.BooleanField(default=False)
    narx=models.FloatField()
    new=models.BooleanField(default=False)
    text=models.TextField()
    size=models.IntegerField()
    color=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name






class Checkout(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    adres=models.TextField()
    sity=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=400)
    telepfone=models.IntegerField()
    acca=models.BooleanField(default=False)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.last_name

class Tek(models.Model):
    text=models.TextField()
    ism=models.CharField(max_length=200)
    def __str__(self):
        return self.ism








