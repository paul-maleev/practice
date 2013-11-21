import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from django.contrib import admin
from orders.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['itemld', 'created']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'address', 'is_approved', 'email']


admin.site.register(Order, OrderAdmin)
# admin.site.register(BookImage,BookImageAdmin)
admin.site.register(Customer, CustomerAdmin)
