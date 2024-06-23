from django.db import models
from accounts.models import User
from tischs.models import Tisch


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tisch = models.ForeignKey(Tisch, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    guest_count = models.IntegerField()
    special_request = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Confirmed')

    def __str__(self):
        return f"Reservation {self.id} by {self.user.username}"