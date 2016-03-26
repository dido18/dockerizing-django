from django.utils import timezone
from django.db import models
import datetime
# Create your models here.

class Client(models.Model):
    name = models.CharField('Nome',max_length=30)
    surname = models.CharField('Cognome', max_length=30)
    nickname = models.CharField("Nominativo", max_length=30)

    class Meta :
	    verbose_name_plural = "Clienti"

    def __unicode__(self):  #__str__in python3.x
        return self.nickname

class Vehicle(models.Model):
    targa = models.CharField(primary_key=True,max_length=15)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.targa
    class  Meta :
	    verbose_name_plural = "Veicoli"

class Mechanic(models.Model):
    id_mechanic = models.AutoField(primary_key=True)
    name = models.CharField("Nome", max_length=30)
    surname  = models.CharField('Cognome', max_length=30)

    def __unicode__(self):  #__str__in python3.x
        return self.name

    class Meta :
	    verbose_name_plural = "Meccanici"


USE_CHOICHES = (
    ('c', "Comunitario"),
    ('m', "Medico"),
    ('p', "Personali")
)

class Reservation(models.Model):
    id_client = models.ForeignKey(Client,verbose_name="Cliente")
    id_vehicle = models.ForeignKey(Vehicle,verbose_name="Veicolo")
    date_reservation = models.DateField('Data di prenotazione')
    hour_start_reservation = models.TimeField()
    hour_end_reservation = models.TimeField()
    id_mechanic = models.ForeignKey(Mechanic, default=1)
    use = models.CharField("Uso",max_length=15,choices=USE_CHOICHES )
    note = models.CharField(max_length=200,blank=True)

    class Meta :
	    verbose_name_plural = "Prenotazioni"

    def __unicode__(self):
        return str(self.id)

    def was_reserved_recently(self):
        now = timezone.now()
        return False #now-date.timedelta(days=1) <= self.date_reservation <= now
    was_reserved_recently.admin_order_field = 'date_reservation'
    was_reserved_recently.boolean = True
    was_reserved_recently.short_description = 'Reservad recently( 1 day ago)?'
    """
    def isExpired(self):
        return self.hour_end_reservation >= timezone.now()
    """
