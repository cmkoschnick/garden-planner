from django.contrib import admin
from gardenbed.models import BedCategory, BedEntry, Bed

# Register your models here.
admin.site.register(BedCategory)
admin.site.register(BedEntry)
admin.site.register(Bed)
