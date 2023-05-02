from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from plantlog.models import PlantEntry, PlantCategory
from plantlog.forms import PlantEntryForm
from django.contrib.auth.models import User
from django.shortcuts import render
from plantlog.forms import PlantEntryForm

@login_required(login_url='/login/')
def plantlog(request):
	if(PlantCategory.objects.count() == 0):
		PlantCategory(season = "summer").save()
		PlantCategory(season = "winter").save()
		PlantCategory(season = "fall").save()
		PlantCategory(season = "spring").save()

	if (request.method == "GET" and "delete" in request.GET):
		id = request.GET["delete"]
		PlantEntry.objects.filter(id=id).delete()
		return redirect("/plants/")
	else:
		table_data = PlantEntry.objects.all()
		context = {
                    "table_data": table_data
		}
		return render(request, 'plantlog/plantlog.html', context)

@login_required(login_url='/login/')
def add(request):
	if (request.method == "POST"):
		if ("add" in request.POST):
			add_form = PlantEntryForm(request.POST, files=request.FILES)
			if (add_form.is_valid()):
				plantEntry = add_form.save(commit=False)
				plantEntry.user = request.user
				plantEntry.save()
				return redirect("/plantlog/")
			else:
				context = {
                    "form_data": add_form
				}
				return render(request, 'plantlog/add.html', context)
		else:
			# Cancel
			return redirect("/plantlog/")
	else:
		context = {
            "form_data": PlantEntryForm()
		}
	return render(request, 'plantlog/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
	if (request.method == "GET"):
		# Load Plant Entry Form with current model data.
		plantEntry = PlantEntry.objects.get(id=id)
		form = PlantEntryForm(instance=plantEntry)
		context = {"form_data": form}
		return render(request, 'plantlog/edit.html', context)
	elif (request.method == "POST"):
		# Process form submission
		if ("edit" in request.POST):
			form = PlantEntryForm(request.POST)
			if (form.is_valid()):
				plantEntry = form.save(commit=False)
				plantEntry.user = request.user
				plantEntry.id = id
				plantEntry.save()
				return redirect("/plantlog/")
			else:
				context = {
                    "form_data": form
				}
				return render(request, 'plantlog/add.html', context)
		else:
			#Cancel
			return redirect("/plantlog/")

@login_required(login_url='/login/')
def entry(request, id):
	if (request.method == "GET"):
		# Load Journal Entry Form with current model data.
		plantEntry = PlantEntry.objects.get(id=id)
		form = PlantEntryForm(instance=plantEntry)
		context = {"form_data": form}
		return render(request, 'plantlog/entry.html', context)
