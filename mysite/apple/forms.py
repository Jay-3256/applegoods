from django import forms

from .models import Item
from django.contrib.auth.models import User

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['titleline','what','price','region','userfile','body']
