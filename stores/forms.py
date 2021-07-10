from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import inlineformset_factory

from .models import Store, MenuItem


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["name", "notes"]

    def __init__(self, *args, submit_title="Submit", **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        if submit_title:
            self.helper.add_input(Submit("submit", submit_title))

BaseMenuItemFormSet = inlineformset_factory(
    parent_model=Store,
    model=MenuItem,
    fields=("name", "price",),
    extra=1
)

class MenuItemFormSet(BaseMenuItemFormSet):
    def __init__(self, *args, **kwargs):
        super(MenuItemFormSet, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False  # 我們要自己包。
        self.helper.disable_csrf = True  # StoreForm 已經有 CSRF token，不需要重複產生。
