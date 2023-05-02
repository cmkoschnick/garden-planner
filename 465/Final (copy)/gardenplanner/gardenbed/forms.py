from django import forms
from gardenbed.models import BedCategory, BedEntry

class BedCreationForm(forms.ModelForm):
    width = forms.IntegerField()
    height = forms.IntegerField()
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    season = forms.ModelChoiceField(queryset=BedCategory.objects.all())
    class Meta():
        model = BedEntry
        fields = ('width', 'height', 'name', 'description', 'season')
