from django.db import models
from accounts.models import User

# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name_plural = 'Clients'
        db_table = 'clients'

