from django import forms
from plantlog.models import PlantEntry, PlantCategory

class PlantEntryForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'size': '25'}))
	season = forms.ModelChoiceField(queryset=PlantCategory.objects.all())
	companions = forms.CharField(widget=forms.TextInput(attrs={'size':'200'}))
	incompatible = forms.CharField(widget=forms.TextInput(attrs={'size':'200'}))
	class Meta():
		model = PlantEntry
		fields = ('name', 'season', 'companions', 'incompatible')
