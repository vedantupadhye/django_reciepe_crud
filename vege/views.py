from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def reciepes(request):

    if request.method == "POST":

        data = request.POST
        reciepe_name = data.get('reciepe_name')
        reciepe_description = data.get('reciepe_description')
        reciepe_image = request.FILES.get('reciepe_image')
 
        Reciepe.objects.create(
            reciepe_name = reciepe_name,
            reciepe_description =  reciepe_description,
             reciepe_image =  reciepe_image,

        )
        return redirect('/reciepes/')

    queryset = Reciepe.objects.all()
    context ={'reciepes': queryset}
    return render(request , 'reciepes.html' , context)

# delete 

def delete_reciepe(request , id):

    queryset = Reciepe.objects.get(id=id)
    queryset.delete()
    return redirect('/reciepes/')


# update

def update_reciepe( request , id):

    queryset = Reciepe.objects.get(id=id)
    
    if request.method == "POST":
        data = request.POST

        reciepe_name = data.get('reciepe_name')
        reciepe_description = data.get('reciepe_description')
        reciepe_image = request.FILES.get('reciepe_image')

        queryset.reciepe_name =  reciepe_name,
        queryset.reciepe_description = reciepe_description

        if reciepe_image:
            queryset.reciepe_image = reciepe_image
        
        queryset.save()
        return redirect('/reciepes/')
    context ={'reciepe': queryset}
    return render(request , 'update_reciepe.html' , context)