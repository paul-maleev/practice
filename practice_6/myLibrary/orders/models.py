from django.db import models
from django.contrib import admin
from library.models import Book
from utils.models import TimeStampedModel

# Create your models here.
import datetime


class Customer(TimeStampedModel):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.TextField()
    is_approved = models.BooleanField()
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Order(TimeStampedModel):

    itemld = models.ForeignKey(Book)
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.itemld
