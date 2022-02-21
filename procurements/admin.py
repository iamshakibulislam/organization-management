from django.contrib import admin
from .models import *

admin.site.register(procurement_plan_for_goods)
admin.site.register(procurement_plan_for_services)
admin.site.register(procurement_plan_for_work)
