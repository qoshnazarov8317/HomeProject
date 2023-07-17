from django.db import models

# Create your models here.

class House(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    humans_count = models.PositiveIntegerField()
    rooms_count = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    house_room = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    humans_count = models.PositiveIntegerField()
    color = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name