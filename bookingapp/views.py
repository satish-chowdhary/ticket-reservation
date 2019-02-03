from django.shortcuts import render, get_list_or_404
from .models import Coaches,Passenger,Portions 
# Create your views here.
from django.views import generic



class PassengerView(generic.CreateView):
    class Meta:
        model = Passenger
        field = ['Name', 'Gender', 'Age', 'select_coach']

def search_result(request):
    tickets = get_list_or_404(Coaches.objects.filter(data=request.GET.get()))

class CoachesView(generic.ListView):
    class Meta:
        model = Coaches
        field = '__all__'

class PortionsView(generic.ListView):
    class Meta:
        model = Portions
        field = '__all__'
