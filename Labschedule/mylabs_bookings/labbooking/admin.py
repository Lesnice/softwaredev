from django.contrib import admin
from .models import Equipment, Booking, Experiment, Antibody, Protocol, Chemical

admin.site.register(Equipment)
admin.site.register(Booking)
admin.site.register(Experiment)
admin.site.register(Antibody)
admin.site.register(Protocol)

@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ('name', 'formula', 'quantity', 'unit')