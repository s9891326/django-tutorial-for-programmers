from django.conf import settings
from django.db import models
from django.urls import reverse
from stores.models import MenuItem


# Create your models here.


class Event(models.Model):
    store = models.ForeignKey("stores.Store", related_name="events", on_delete=models.CASCADE)

    class Meta:
        get_latest_by = "pk"

    def __str__(self):
        return str(self.store)

    def get_absolute_url(self):
        return reverse("event:event_detail", kwargs={"pk": self.pk})


class Order(models.Model):
    event = models.ForeignKey(Event, related_name="orders", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="orders", null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(MenuItem, related_name="orders", on_delete=models.CASCADE)
    notes = models.TextField(blank=True, default="")

    class Meta:
        # 代表 event 和 user 這兩個欄位的組合必須 unique——限制一個使用者只能在一次 event 中點一次餐。
        unique_together = ("event", "user",)

    def __str__(self):
        return f"{self.item} of {self.user} for {self.event}"
