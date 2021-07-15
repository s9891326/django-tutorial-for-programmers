from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import Http404, HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect
# from django.forms.models import modelform_factory
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, mixins, permissions

from events.forms import EventForm
from stores.serializers import StoreSerializer, MenuItemRelatedSerializer
from .models import Store, MenuItem
from .forms import StoreForm, MenuItemFormSet


# Create your views here.

# def home(request):
#     return render(request, 'home.html')

def store_list(request):
    stores = Store.objects.all()
    return render(request, "stores/store_list.html", {"stores": stores})


def store_detail(request, pk):
    print("store detail")
    try:
        store = Store.objects.get(pk=pk)
        event_form = EventForm(initial={"store": store}, submit_title="建立活動")
        event_form.helper.form_action = reverse("event:event_create")
    except Store.DoesNotExist:
        raise Http404
    return render(request, "stores/store_detail.html", {
        "store": store,
        "event_form": event_form,
    })


def store_create(request):
    # StoreForm = modelform_factory(Store, fields=("name", "notes",))

    if request.method == "POST":
        form = StoreForm(request.POST, submit_title="建立")
        # if form.is_valid():
        #     store = form.save()
        #     return redirect(store.get_absolute_url())

        if form.is_valid():
            store = form.save(commit=False)
            print(f"is_authenticated: {request.user.is_authenticated}")
            if request.user.is_authenticated:
                store.owner = request.user
            store.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(submit_title="建立")

    return render(request, "stores/store_create.html", {"form": form})


def store_update(request, pk):
    print("store update")
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404

    # StoreForm = modelform_factory(Store, fields=("name", "notes",))
    if request.method == "POST":
        form = StoreForm(request.POST, instance=store, submit_title="更新")

        menu_item_formset = MenuItemFormSet(request.POST, instance=store)
        if form.is_valid():
            store = form.save()
            menu_item_formset.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(instance=store, submit_title="更新")
        form.helper.form_tag = False

        menu_item_formset = MenuItemFormSet(instance=store)

    # MenuItemFormSet = inlineformset_factory(
    #     parent_model=Store,
    #     model=MenuItem,
    #     fields=("name", "price",),
    #     extra=1
    # )
    # menu_item_formset = MenuItemFormSet(instance=store)

    return render(request, "stores/store_update.html", {
        "form": form,
        "store": store,
        "menu_item_formset": menu_item_formset,
    })


@login_required
@require_http_methods(["POST", "DELETE"])
def store_delete(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404

    # if (not store.owner or store.owner == request.user
    #         or request.user.has_perm('store_delete')):
    #     store.delete()
    #     return redirect('store:store_list')
    # return HttpResponseForbidden()

    # 把邏輯改寫到model內
    if store.can_user_delete(request.user):
        store.delete()
        # 增加ajax判斷
        if request.is_ajax():
            return HttpResponse()
        return redirect("store:store_list")
    return HttpResponseForbidden()


class MenuItemViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemRelatedSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     store = serializer.save()
    #     print(store)
        # serializer.save(menu_items=)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
