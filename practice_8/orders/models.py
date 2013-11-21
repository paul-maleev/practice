from django.db import models, connection
from django.contrib import admin
from django.http import response
from library.models import Book
from utils.models import TimeStampedModel
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

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
        return unicode(self.itemld)


class CustomersList(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = "orders.html"

    def get_queryset(self):
        return Order.objects.all()


class CustomerDetails(DetailView):
    model = Customer
    template_name = 'customer.html'
    slug_field = 'id'
    context_object_name = 'customer'
