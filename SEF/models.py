import json
from django.db import models

# Create your models here.
class Pet(models.Model):
    # name, species, breed, age, gender, description
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image_path = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    fee = models.PositiveIntegerField()
    date_added = models.CharField(max_length=100)

    def __str__(self):
        return json.dumps({
                "name": self.name,
                "species": self.species,
                "breed": self.breed,
                "age": self.age,
                "gender": self.gender,
                "description": self.description,
                "image_path": self.image_path,
                "status": self.status,
                "suburb": self.suburb,
                "state": self.state,
                "fee": self.fee,
                "date_added": self.date_added
            })