from django.shortcuts import render
from controls.models import Country, State, City


def controls(request):
    countryid = request.GET.get('country', None)
    stateid = request.GET.get('state', None)
    state = None
    city = None
    if countryid:
        getcountry = Country.objects.get(id=countryid)
        state = State.objects.filter(country=getcountry)

    if stateid:
        getstate = State.objects.get(id=stateid)
        city = City.objects.filter(state=getstate)

    country = Country.objects.all()

    return render(request, 'controls.html', locals())
