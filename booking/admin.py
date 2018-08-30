# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from booking.models import NewProducts,BookingProduct
# Register your models here.

admin.site.register(NewProducts)
admin.site.register(BookingProduct)
