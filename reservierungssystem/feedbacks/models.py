from django.db import models
from accounts.models import User
from reservations.models import Reservation


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username} for reservation {self.reservation.id}"