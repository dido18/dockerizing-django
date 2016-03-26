from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


#app_name='officina' # name for namespacing the template {% url %}
urlpatterns = [
    # root of /officina/
    #url(r'^$', views.index, name='officina'), # name= namespace of the urls
    url(r'^$', TemplateView.as_view(template_name="appOfficina/base.html"),name='index'),#

    #ex :/officina/clients/   (view of all the clients)
    url(r'^clients/$', views.ClientsView.as_view(), name='clients'),
    #ex :/autofficina/client/5    ( detail of the client 5)
    url(r'^client/(?P<pk>[0-9]+)/$', views.DetailsClientView.as_view(), name='detailsClient'),
    #ex: /autofficina/client/5/results  ( all the results reservations of the client 5)
    url(r'^client/(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view() , name='results'),
    #ex: (autofficina/)/3/erase  ( cancellazione prenotaione 2 del client 3)
    url(r'^(?P<client_id>[0-9])/erase/$' , views.erase, name='erase'),

    #ex :/autofficina/reservations/
    url(r'^reservations/$', views.ReservationsView.as_view(), name='reservations'),
    #ex :/autofficina/reservation/5
    url(r'^reservation/(?P<pk>[0-9]+)/$', views.DetailReservationView.as_view(), name='detailsReservation'),

    #ex :/autofficina/vehicles/
    url(r'^vehicles/$', views.VehiclesView.as_view(), name='vehicles'),
    #ex :/autofficina/vehicles/<targa>
    url(r'^vehicles/(?P<pk>[\w]+)/$', views.DetailsVehicleView.as_view(), name='detailsVehicle'),


]
