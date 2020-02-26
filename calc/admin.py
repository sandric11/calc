from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin
@admin.register(Destination_from, Destination_to, Shipment, Zone_postal, Zone_price, Pretvornik)
class ViewAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
# admin.site.register(Destination_from)
# admin.site.register(Destination_to)
# admin.site.register(Shipment)
# admin.site.register(Zone_postal)
