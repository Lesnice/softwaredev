from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import the timezone module

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #title = models.CharField(max_length=255)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"{self.user.username} - {self.equipment.name} ({self.start_time} to {self.end_time})"


class Experiment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(default=timezone.now)  # Add this field to store the date of the experiment
    notes = models.TextField(blank=True, null=True)  # Add this field for experiment notes

    def __str__(self):
        return f"{self.title} by {self.user.username}"


class Antibody(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255, blank=True, null=True)  # Add this field to specify the species
    concentration = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Add this field for concentration

    def __str__(self):
        return self.name
    

    def __str__(self):
        return self.name
class Chemical(models.Model):
    name = models.CharField(max_length=255)
    concentration = models.FloatField(default=1)
    description = models.TextField(blank=True)
    formula = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Protocol(models.Model):
    """
Protocol model representing a set of instructions or guidelines associated with an antibody.

This class captures the title and content of a protocol, along with an optional reference to an associated antibody. It provides a string representation of the protocol's title.

Attributes:
    title (str): The title of the protocol.
    content (str): The content or instructions of the protocol.
    antibody (Antibody): An optional reference to an associated antibody.

"""
    title = models.CharField(max_length=255)
    description = models.TextField(default="Default description")  # Add this field if you want to include a description
    notes = models.TextField(blank=True, null=True)  # Add this field if you want to include notes

    def __str__(self):
        return self.title

