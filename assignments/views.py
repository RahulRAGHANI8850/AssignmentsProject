from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.


def indexpage(request):
    return render(request, "assignmentform.html")


def assignmentsubmit(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        message = request.POST.get("message")
        project = request.FILES["zipfile"]

        insert = assignment(username=name, email=email, msg=message, time="", projectFile=project)
        insert.save()

        messages.info(request, "Assigment Submited Sucessfully!!")
        return redirect(submitted)

    return render(request, 'assignmentform.html')



def submitted(request):
    return render(request, "submited.html")