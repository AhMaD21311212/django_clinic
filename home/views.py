from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from Doctors.models import Doctor,Department


# Create your views here.




def home(request):
    doctor = Doctor.objects.all()
    department = Department.objects.all()

    return render(request,'home/index.html',{'doctor':doctor,'department':department})
