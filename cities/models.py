from django.db import models

class State(models.Model):
    class Meta:
        db_table = 'state'
    name = models.CharField(max_length=255)
    shortcut = models.CharField(max_length=2)
    capital = models.CharField(max_length=255)
    population = models.IntegerField()

class City(models.Model):
    class Meta:
        db_table = 'city'
    name = models.CharField(max_length=255)
    rank = models.IntegerField()
    state = models.ForeignKey(State)
    population = models.IntegerField()
    land_area = models.DecimalField(max_digits=10, decimal_places=2)
    population_density = models.DecimalField(max_digits=10, decimal_places=2)
