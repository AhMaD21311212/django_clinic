from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.title

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name='department')
    image = models.ImageField(upload_to="image/doctor")
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Cantact(models.Model):
    name = models.CharField(max_length=100)
    email= models.CharField(max_length=500)
    message = models.TextField()


    def __str__(self):
        return self.message[:30]