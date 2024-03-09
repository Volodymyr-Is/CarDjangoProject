from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from car_app.models import Vehicle
from car_app.forms import *



def Vehicles(request):
    distinct_types = Vehicle.objects.values_list('type', flat=True).distinct()
    distinct_brand = Vehicle.objects.values_list('brand', flat=True).distinct()

    if request.method == 'POST':
        selected_type = request.POST.get('Type')
        selected_brand = request.POST.get('Brand')

        if selected_type == 'All' and selected_brand == 'All':
            vehicle_list = Vehicle.objects.all()
        elif selected_type == 'All':
            vehicle_list = Vehicle.objects.filter(brand=selected_brand)
        elif selected_brand == 'All':
            vehicle_list = Vehicle.objects.filter(type=selected_type)
        else:
            vehicle_list = Vehicle.objects.filter(type=selected_type, brand=selected_brand)
    else:
        vehicle_list = Vehicle.objects.all()


    context = {
        'vehicleList': vehicle_list,
        'distinctTypes': distinct_types,
        'distinctBrands': distinct_brand,
    }
    return render(request, 'vehicleList.html', context)


def GetVehicleById(response, vehicleId):
    vehicle = get_object_or_404(Vehicle, pk=vehicleId)
    return render(response, 'vehicle.html', {'vehicle': vehicle})


def GetVehicleByType(response, vehicleType):
    vehicle_list = get_object_or_404(Vehicle, type=vehicleType)
    return render(response, 'vehicleList.html', {'vehicleList': vehicle_list})


def GetVehicleByName(response, vehicleBrand):
    vehicle_list = get_object_or_404(Vehicle, brand=vehicleBrand)
    return render(response, 'vehicleList.html', {'vehicleList': vehicle_list})


def GetVehicleByModel(response, vehicleModel):
    vehicle_list = get_object_or_404(Vehicle, model=vehicleModel)
    return render(response, 'vehicleList.html', {'vehicleList': vehicle_list})


def NewVehicle(response):
    if response.method == 'POST':
        form = VehicleForms(response.POST)

        vehicle = Vehicle(
            brand = form.changed_data['brand'],
            model = form.changed_data['model'],
            type = form.changed_data['type'],
            image = form.changed_data['image'],
            price = form.changed_data['price'],
            distanceTraveled = form.changed_data['distanceTraveled'],
            maxSpeed = form.changed_data['maxSpeed'],
        )
        vehicle.save()
        return HttpResponseRedirect(f'/vehicles/')

    # vehicles = Vehicle.objects.all()
    return render(response, 'addVehicle.html', {'form': VehicleForms})