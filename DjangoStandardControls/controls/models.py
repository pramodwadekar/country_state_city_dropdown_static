from django.db import models


class Country(models.Model):
    country_id = models.IntegerField()
    country_name = models.CharField(max_length=50)
    country_value = models.CharField(max_length=10)

    def __str__(self):
        return self.country_name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    state_id = models.IntegerField()
    state_name = models.CharField(max_length=50)
    state_value = models.CharField(max_length=10)

    def __str__(self):
        return self.state_name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=50)
    city_value = models.CharField(max_length=10)

    def __str__(self):
        return self.city_name

