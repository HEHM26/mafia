#chat/form

from django import forms
from .models import Player, Host


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = '__all__'