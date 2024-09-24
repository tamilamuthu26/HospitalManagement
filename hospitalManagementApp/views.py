from django.shortcuts import redirect, render


from hospitalManagementApp.forms import AppointmentForm
from hospitalManagementApp.models import Doctor

# Create your views here.
def index(request):
    doctors = Doctor.objects.filter(status=0)
    return render(request,"index.html", {'doctors': doctors})
# Create your views here.
def index(request):
    doctors = Doctor.objects.filter(status=0)
    form = AppointmentForm()  # Instantiate the form
    return render(request,"index.html", {'doctors': doctors, 'form': form})

def addnew(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AppointmentForm()
    return render(request, "index.html", {'form': form})



def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")
def feature(request):
    return render(request,"feature.html")
  
def appointment(request):
    return render(request,"appointment.html")
def error(request):
    return render(request,"404.html")
def contact(request):
    return render(request,"contact.html")
def team(request):
    return render(request,"team.html")
def testimonial(request):
    return render(request,"testimonial.html")