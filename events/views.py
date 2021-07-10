from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.utils.decorators import classonlymethod
from django.views.generic import CreateView, DetailView
from events.forms import EventForm, OrderForm
from events.models import Event, Order


# Create your views here.


class EventCreateView(LoginRequiredMixin, CreateView):
    # 預設template結尾為: template_name_suffix = '_form'
    form_class = EventForm

    # 只允許 POST，若硬是用get方式進行呼叫，會回傳405 Method not allowed
    # 既然get方法無法使用，那也不需要event_form.html
    http_method_names = ["post"]
    model = Event

class EventDetailView(LoginRequiredMixin, DetailView):
    # 預設template結尾為: template_name_suffix = '_detail'
    model = Event

    def get_context_data(self, **kwargs):
        data = super(EventDetailView, self).get_context_data(**kwargs)

        order = self.get_order(user=self.request.user)
        order_form = OrderForm(instance=order)

        # Django 的 select widget 可以擁有一個 queryset attribute，用來限制能選擇的選項
        order_form.fields["item"].queryset = self.object.store.menu_items.all()
        data["order_form"] = order_form
        return data

    # 用LoginRequiredMixin來取代
    # # 在 function-based views 中，我們可以使用 login_required decorator。
    # # 在 CBV 中也可以這麼做——但要記得，真正被使用的是 as_view() 回傳的 view，所以我們必須覆寫它，自己把 login_required 加上去：
    # @classonlymethod
    # def as_view(cls, **initkwargs):
    #     view = super().as_view(**initkwargs)
    #     return login_required(view)

    def post(self, request, *args, **kwargs):
        order = self.get_order(self.request.user)
        form = OrderForm(request.POST, instance=order)
        if not form.is_valid():
            return HttpResponseBadRequest()
        order = form.save(commit=False)
        order.user = request.user
        order.event = self.get_object()
        order.save()
        return redirect(order.event.get_absolute_url())

    def get_order(self, user):
        try:
            order = Order.objects.get(user=user, event=self.get_object())
        except Order.DoesNotExist:
            order = None
        return order

