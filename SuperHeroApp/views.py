from django.shortcuts import render
from .forms import SuperForm

# Create your views here.

# For form function
def index(request):
    # if information is entered
    if(request.method =="POST"):
        superForm = SuperForm(request.POST)
        # so info has to be entered
        if superForm.is_valid():
            # to save information
            superForm.save()
            # print in console
            print(request.POST)
        else:
            print("Error!")

# to direct to index page
    return render(request, "SuperHeroApp/index.html", {"superForm": SuperForm()})


# to direct to thank you page
def thankyou(request):
    return render(request, "SuperHeroApp/thankyou.html")

# to direct to welcome page
def welcome(request):
    return render(request, "SuperHeroApp/welcome.html")