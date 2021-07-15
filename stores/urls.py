from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "store"

urlpatterns = [
    path("", views.store_list, name="store_list"),
    path("<int:pk>", views.store_detail, name="store_detail"),
    path("new/", views.store_create, name="store_create"),
    path("<int:pk>/update/", views.store_update, name="store_update"),
    path("<int:pk>/delete/", views.store_delete, name="store_delete"),
]

# rest api
v1 = routers.DefaultRouter()
v1.register("store", views.StoreViewSet)
v1.register("stores/menu_item", views.MenuItemViewSet)

urlpatterns += [
    path("api/v1/", include(v1.urls)),
]
