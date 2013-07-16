from django.http import HttpResponse, HttpResponseRedirect
from activities.models import ActivityForm, Activity
from django.shortcuts import render
from django.core.urlresolvers import reverse

def index(request):
    """List activities, by date desc limited to most recent 50"""
    recent_activities = Activity.objects.order_by('-date')[:50]
    return render(request, "activities/listing.html", {"recent_activities": recent_activities})

def add(request):
    """Add an activity"""
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            # save the data
            form.save()
            return HttpResponseRedirect(reverse('activities:index'))
        else:
            return render(request, "activities/add.html", {
                "form": form,
            })
    else:
        # Display a blank form
        form = ActivityForm()

        return render(request, "activities/add.html", {
            "form": form,
        })
        
