from django.db import models
from users.models import User


class Rating(models.Model):
    restaurant_id = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    rate = models.FloatField()
    etc = models.CharField(max_length=250)

    class Meta:
        unique_together = (("restaurant_id", "user_id"))
