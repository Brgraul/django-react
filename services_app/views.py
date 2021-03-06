from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Service, VetsDisplay, CustomerDisplay
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import Http404

# Create your views here.

#Individual Service Page
def ServicePage(request, service_url):
    service = get_object_or_404(Service, url = service_url)
    vets = VetsDisplay.objects.filter(published_slider=True)
    customers = CustomerDisplay.objects.filter(published=True)
    context = {
        'service' : service,
        'vets':vets,
        'customers':customers,
    }
    return render(request, "services_app/service.html", context)

def ServicesIndex(request):
    vets = VetsDisplay.objects.filter(published_slider=True)
    customers = CustomerDisplay.objects.filter(published=True)
    context = {
        'vets':vets,
        'customers':customers,
    }
    request.session.set_test_cookie()
    return render(request, "services_app/services_index.html", context)


def MeetTheVetsPage(request):
    vets = VetsDisplay.objects.filter(published_lasvets=True)
    customers = CustomerDisplay.objects.filter(published=True)
    context = {
        'vets':vets,
        'customers':customers,
    }
    print request.session.test_cookie_worked()
    return render(request, "services_app/meet_vets.html", context)

def Index(request):
    vets = VetsDisplay.objects.filter(published_slider=True)
    customers = CustomerDisplay.objects.filter(published=True)
    context={
        'vets':vets,
        'customers':customers,
    }
    return render(request, "services_app/index.html", context)

def VetProfile(request, vet_id):
	#return HttpResponse("You are looking at Coach: %s." % coach_id)
	vet = get_object_or_404(Vet, pk=vet_id)
	return render(request, 'booking/vet.html', {'vet': vet})

# Vista provisional para las tarifas

def Pricing(request):
    context={}
    return render(request, "services_app/pricing.html", context)

def Terms(request):
    context={}
    return render(request, "services_app/terms.html", context)

def Privacy(request):
    context={}
    return render(request, "services_app/privacy.html", context)
