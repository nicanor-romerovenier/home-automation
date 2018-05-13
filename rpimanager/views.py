from django.shortcuts import render
from django.http import HttpResponse
from .models import RelaySwitch


def index(request):
    switches = RelaySwitch.objects.all()
    context = {
        'switches': switches,
    }
    return render(request, 'rpimanager/index.html', context)


def switch_details(request, switch_id):
    return HttpResponse("These are the details for switch {0}".format(switch_id))

