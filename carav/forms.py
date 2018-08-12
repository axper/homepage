from django import forms

from carav import models


class WaterFountainForm(forms.ModelForm):
    class Meta:
        model = models.WaterFountain
        exclude = ['created', 'updated']
