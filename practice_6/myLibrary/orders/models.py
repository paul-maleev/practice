from django.db import models
from utils.models import TimeStampedModel


class Order(TimeStampedModel):
    title = models.CharField(max_length=128)

# Create your models here.
