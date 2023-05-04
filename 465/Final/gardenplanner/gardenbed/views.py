from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gardenbed.models import BedCategory, BedEntry, Bed
from gardenbed.forms import BedCreationForm, BedEntryForm
from django.contrib.auth.models import User
from django.shortcuts import render

@login_required(login_url='/login/')
def gardenbed(request):
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
    context = { "form_data": BedCreationForm, "rows": [] , "bed_form": BedEntryForm}
    bedEntry = BedEntry.objects.get(id=id)
    if (request.method == "GET"):
		# Load Journal Entry Form with current model data.
        #bedEntry = BedEntry.objects.get(id=id)
        form = BedCreationForm(instance=bedEntry)
        context["form_data"] = form
        if Bed.objects.filter(user=request.user, idx=id).count() == 0:
            blankBed(request, w=bedEntry.width, h = bedEntry.height, id = id)
    elif (request.method == 'POST'):
        f = BedEntryForm(request.POST)
        if(f.is_valid()):
            loc = f.cleaned_data["location"]
            value = f.cleaned_data["value"]
            Bed.objects.filter(user=request.user, location=loc, idx=id).delete()
            Bed(user=request.user, location=loc, value=value, idx=id).save()
            #print("Location "+ location + " has been updated")
    for row in range (1, bedEntry.width+1):
        row_data = {}
        for col in range (1, bedEntry.height+1):
            l= "r{}c{}".format(row,col)
            try:
                record = Bed.objects.get(user=request.user, location=l, idx = id)
                row_data[l] = record.value
            except Bed.DoesNotExist:
                row_data[l] = "err"
                print("Board DNE")
        context.get("rows").append(row_data)
    return render(request, 'gardenbed/entry.html', context)

def blankBed(request, w, h, id):
    # Populate board model objects from page_data
    for row in range (1, w+1):
        for col in range (1, h+1):
                l= "r{}c{}".format(row,col)
                #print("the value I am creating for l is:" + l + "\n")
                b = Bed(user=request.user, location=l, value=l, idx=id).save()
                #b.id = id
                #b.save()
