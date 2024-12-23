from django.db import models

# Create your models here.
class chairperson(models.Model):
    GENDER_CHOICES = {
        'M':'MALE',
        'F':'FEMALE',
    }
    name = models.CharField(max_length=20)
    age = models.CharField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f" {self.name}"
class street(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(null=True, blank=True)
    pop = models.IntegerField()
    chairperson = models.OneToOneField(chairperson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"    
class patient(models.Model):
    name = models.CharField(max_length=200)   