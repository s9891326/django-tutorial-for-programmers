from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=20)
    notes = models.TextField(blank=True, default="")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, related_name="owned_stores", on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:store_detail', kwargs={"pk": self.pk})

    def can_user_delete(self, user):
        if not self.owner or self.owner == user:
            return True
        if user.has_perm("stores.delete_store"):
            return True
        return False

class MenuItem(models.Model):
    store = models.ForeignKey('Store', related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name

