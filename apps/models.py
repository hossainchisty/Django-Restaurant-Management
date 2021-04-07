from django.db import models

# Create your models here.

class specialty(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(max_length=4)
    detail = models.TextField()
    image = models.CharField(max_length=2033)   

    def __str__(self):
        return self.name

class salads(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    detail = models.TextField()
    image = models.CharField(max_length=2033) 

    def __str__(self):
        return self.name

class starters(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    detail = models.TextField()
    image = models.CharField(max_length=2033) 

    def __str__(self):
        return self.name


class chefs(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Photos')
    twitter = models.URLField(max_length=3000, null=True, blank=True)
    facebook = models.URLField(max_length=3000, null=True, blank=True)
    instagram = models.URLField(max_length=3000, null=True, blank=True)
    linkedin = models.URLField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=400)
    message = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    time = models.TimeField(auto_now_add=True, null=True, blank=True)
    people = models.CharField(max_length=10000, null=True, blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
