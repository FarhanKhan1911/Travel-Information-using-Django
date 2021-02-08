from django.shortcuts import render
from .models import Destination
# Create your views here.
def home(request):

    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The city that never sleeps'
    # dest1.price = 700
    # dest1.image = 'destination_1.jpg'
    # dest1.offer = True

    # dest2 = Destination()
    # dest2.name = 'Hyderabad'
    # dest2.desc = 'The city'
    # dest2.price = 750
    # dest2.image = 'destination_2.jpg'
    # dest2.offer = False

    # dest3 = Destination()
    # dest3.name = 'Kolkata'
    # dest3.desc = 'The clean city '
    # dest3.price = 650
    # dest3.image = 'destination_3.jpg'
    # dest3.offer = True

    # dests = [dest1,dest2,dest3]

    dests = Destination.objects.all()                          ### To get all the data from the database 

    return render(request,'index.html', {'dests': dests} )

