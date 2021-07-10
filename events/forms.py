from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Event, Order


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['store']

        # Django 在把 form 轉成 HTML form 時，會自動根據欄位形態選擇合適的 HTML tag；
        # 但如果你不滿意預設值，也可以用 widgets 來明確要求 Django 在某個欄位使用特定 widget
        widgets = {"store": forms.HiddenInput}

    def __init__(self, *args, submit_title='Submit', **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', submit_title))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item', 'notes']

    def __init__(self, *args, submit_title="Submit", **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields["item"].empty_label = None  # 把空值的顯示值設成 None
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', submit_title))
