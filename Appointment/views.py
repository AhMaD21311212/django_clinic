from django.shortcuts import render , redirect, reverse
from django.views.generic import TemplateView,ListView,DetailView
from .models import Appointment
from Doctors.models import Doctor

# Create your views here.

class AppointmentView(ListView):
    def post(self,request):
        doctor_id = request.POST.get('doctor_id')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        dctor = request.POST.get('doctor')
        time = request.POST.get('time')
        des= request.POST.get('description')
        Appointment.objects.create(name=name,mobile=mobile,time=time,doctor=dctor,description=des)
        return redirect('appointment:resid', doctor_id)
    def get(self,request):
        doctor = Doctor.objects.all()
        return render(request,'Appointment/appointment.html',{'doctor':doctor})


#class resid(DetailView):
#    template_name = 'Appointment/resid.html'
#    model = Doctor
#    context_object_name = 'resid'

def resid(request,pk):
    resid = Doctor.objects.filter(id=pk)


    return render(request,'Appointment/resid.html',{'resid':resid})