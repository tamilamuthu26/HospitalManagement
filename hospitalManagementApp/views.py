from django.shortcuts import render


from hospitalManagementApp.models import Doctor

# Create your views here.
def index(request):
    doctors = Doctor.objects.filter(status=0)
    return render(request,"index.html", {'doctors': doctors})
# Create your views here.

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