from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gardenbed.models import BedCategory, BedEntry
from gardenbed.forms import BedCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

@login_required(login_url='/login/')
def gardenbed(request):
    BedCategory(season = "spring").save()
    if(BedCategory.objects.count() == 0):
    	BedCategory(season = "summer").save()
    	BedCategory(season = "winter").save()
    	BedCategory(season = "fall").save()
    	BedCategory(season = "spring").save()

    if (request.method == "GET" and "delete" in request.GET):
    	id = request.GET["delete"]
    	BedEntry.objects.filter(id=id).delete()
    	return redirect("/gardenbed/")
    else:
    	table_data = BedEntry.objects.all()
    	context = {
                    "table_data": table_data
    	}
    	return render(request, 'gardenbed/gardenbed.html', context)

@login_required(login_url='/login/')
def add(request):
	if (request.method == "POST"):
		if ("add" in request.POST):
			add_form = BedCreationForm(request.POST, files=request.FILES)
			if (add_form.is_valid()):
				bedEntry = add_form.save(commit=False)
				bedEntry.user = request.user
				bedEntry.save()
				return redirect("/gardenbed/")
			else:
				context = {
                    "form_data": add_form
				}
				return render(request, 'gardenbed/add.html', context)
		else:
			# Cancel
			return redirect("/gardenbed/")
	else:
		context = {
            "form_data": BedCreationForm()
		}
	return render(request, 'gardenbed/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
	if (request.method == "GET"):
		# Load Bed Entry Form with current model data.
		bedEntry = BedEntry.objects.get(id=id)
		form = BedCreationForm(instance=bedEntry)
		context = {"form_data": form}
		return render(request, 'gardenbed/edit.html', context)
	elif (request.method == "POST"):
		# Process form submission
		if ("edit" in request.POST):
			form = BedCreationForm(request.POST)
			if (form.is_valid()):
				bedEntry = form.save(commit=False)
				bedEntry.user = request.user
				bedEntry.id = id
				bedEntry.save()
				return redirect("/gardenbed/")
			else:
				context = {
                    "form_data": form
				}
				return render(request, 'gardenbed/add.html', context)
		else:
			#Cancel
			return redirect("/gardenbed/")

@login_required(login_url='/login/')
def entry(request, id):
	if (request.method == "GET"):
		# Load Journal Entry Form with current model data.
		bedEntry = BedEntry.objects.get(id=id)
		form = BedCreationForm(instance=bedEntry)
		context = {"form_data": form}
		return render(request, 'gardenbed/entry.html', context)
