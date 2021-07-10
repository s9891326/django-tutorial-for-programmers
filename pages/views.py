from django.shortcuts import render

# Create your views here.
from events.models import Event


def home(request):
    # return render(request, 'pages/home.html')
    try:
        current_event = Event.objects.latest()
    except Event.DoesNotExist:
        current_event = None
    return render(request, "pages/home.html", {"current_event": current_event})

