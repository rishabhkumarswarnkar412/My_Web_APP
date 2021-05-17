from django.db import models

#makemigrations: create changes and store in a file.
#migrate: apply the pending changes created by makemigrations.

# Create your models here.
class Get_quote(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    feedback=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

   
 
class Design(models.Model):
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='pics')
    description= models.TextField()

    def __str__(self):
        return self.name