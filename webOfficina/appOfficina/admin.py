from django.contrib import admin

from .models import Reservation,Client,Vehicle,Mechanic


class ReservationAdmin(admin.ModelAdmin):
    fieldsets =  [
        ('Informazioni del cliente', {'fields':['id_client']}),
        ('Dettagli prenotazione'   , {'fields':['id_vehicle','date_reservation','hour_start_reservation','hour_end_reservation','id_mechanic']}),
        ('Specifiche prenotatione' , {'fields':['use','note']}),
        ]
    list_display = ('id_client','id_vehicle','date_reservation','was_reserved_recently','use','note')
    list_filter = ['date_reservation']
    search_fields =['use']

class ClientAdmin(admin.ModelAdmin):

    list_display = ('name','surname','nickname')

class VehicleAdmin(admin.ModelAdmin):

    list_display=('name','targa')
"""
class MeccanicoAdmin(admin.ModelAdmin):

    list_display=('name','surname')
"""
class MechanicAdmin(admin.ModelAdmin):
    list_display=('name','surname')

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Mechanic,MechanicAdmin)
