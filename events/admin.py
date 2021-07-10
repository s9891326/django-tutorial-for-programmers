from django.contrib import admin
from events.models import Order, Event


# Register your models here.


class OrderInline(admin.StackedInline):
    model = Order
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["event", "item", "user"]
