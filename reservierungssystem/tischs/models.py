from django.db import models


class Tisch(models.Model):
    tisch_nummer = models.CharField(max_length=10, unique=True)
    seats = models.IntegerField()
    status = models.BooleanField(default=False)
    location = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'Tisch {self.tisch_nummer} ist {"frei" if self.status else "reserviert"}'
