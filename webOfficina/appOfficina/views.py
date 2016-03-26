from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

import json
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
# Create your views here.

from .models import Client,Reservation,Vehicle

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class JSONResponse(HttpResponse):
    """
    a HttpRensonse that rendres its content into JSON

    """
    def __init__(self, data, **kwargs):
        content = JSONRendemodel=Clientrer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class VehiclesView(generic.ListView):
    model = Vehicle
    template_name = 'appOfficina/base_vehicles.html'
    context_object_name =  'list_vehicles'

class DetailsVehicleView(generic.DetailView):
    model = Vehicle
    template_name = 'appOfficina/detailsVehicle.html'
    context_object_name =  'vehicle'


class ClientsView(generic.ListView):
    model = Client
    template_name = 'appOfficina/base_clients.html'
    context_object_name =  'list_clients'

    """
    def clients(request):
        try:
            list_clients = Client.objects.all()
        except Client.DoesNotExist:
            raise Http404("Clienti don't exist")
        template = loader.get_template('appOfficina/clients.html')
        context = RequestContext(request,{
            'list_clients':list_clients,
        })
        return HttpResponse(template.render(context))
    """
class DetailsClientView(generic.DetailView):
    model = Client
    template_name = 'appOfficina/detailsClient.html'
    context_object_name =  'client'


class ResultsView(generic.DetailView):
    model = Client
    template_name = 'appOfficina/results.html'

class ReservationsView(generic.ListView):
    model = Reservation
    template_name = 'appOfficina/base_reservations.html'
    context_object_name = 'list_reservations'

class DetailReservationView(generic.DetailView):
    model = Reservation
    template_name = 'appappOfficina/detailsReservation.html'
    context_object_name = 'reservation'

    """
    def detailReservation(request, reservation_id):
        reservation = get_object_or_404(Reservation,pk=reservation_id)
        return render(request,'officina/detailReservation.html',{'reservation':reservation})
    """

def results(request, client_id):
    response = "You are looking for the reservations of the client %s."
    return HttpResponse(response % client_id)

def erase(request, client_id):
    c = get_object_or_404(Client,pk=client_id)
    try:
        reservation = c.reservation_set.get(pk=request.POST['erase'])
    except (KeyError, Reservation.DoesNotExist):
        #Redislpay the erase form if there is an error
        return (request, 'appOfficina/detailClient.html',{
            'client':c,
            'error_message':"You didn't select an erasing elment",
            })
    else:
        Reservation.objects.get(pk=reservation.id).delete()
        # always return HTTPResponseRedirect. THis preventi data
        # from being posted twice, when user hits the back button
        # reverse django function for url: /officina/3/results/
        return HttpResponseRedirect(reverse('appOfficina:results', args=(c.id,)))

def results(request, client_id):
    client =  get_object_or_404(Client, pk = client_id)
    return render( request, 'appOfficina/results.html',{'client':client})


def clients_json( request):
    """
    List all clients, or create new client

    """

    clients = Client.objects.all()
    data = serializers.serialize("json",clients)
    #return JsonResponse( data , encoder=MyJSONEncode, safe=False)
    return HttpResponse(data , content_type="application/json")
    """
    if request.method == 'GET':
        clients = Client.objects.all()

        serializer = ClientSerializer(clients, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        """
