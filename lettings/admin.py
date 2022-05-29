from django.contrib import admin

from .models import Letting
from .models import Addresses



admin.site.register(Letting)
admin.site.register(Addresses)
