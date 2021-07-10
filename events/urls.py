from django.conf.urls import url
from . import views

app_name = "event"

urlpatterns = [
    url(r'^new/$', views.EventCreateView.as_view(), name='event_create'),
    url(r'^(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='event_detail'),
]
