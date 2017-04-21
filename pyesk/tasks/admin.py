from django.contrib import admin
from .models import Ticket, Category, Status


admin.site.register([Ticket, Category, Status])
