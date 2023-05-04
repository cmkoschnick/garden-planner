from django import forms
from gardenbed.models import BedCategory, BedEntry
from django.core import validators

class BedCreationForm(forms.ModelForm):
    width = forms.IntegerField()
    height = forms.IntegerField()
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    season = forms.ModelChoiceField(queryset=BedCategory.objects.all())
    class Meta():
        model = BedEntry
        fields = ('width', 'height', 'name', 'description', 'season')

class BedEntryForm(forms.Form):
    location=forms.CharField(min_length=4, max_length=4)
    value = forms.CharField(min_length=1, max_length=100)
