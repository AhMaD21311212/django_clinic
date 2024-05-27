from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView
from.models import Doctor,Cantact

# Create your views here.

class about(ListView):
    template_name = 'Doctors/about.html'
    model = Doctor
    context_object_name = 'doctor'


class service(TemplateView):
    template_name = 'Doctors/service.html'


def ContactView(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Cantact.objects.create(name=name,email=email,message=message)
        return redirect("Home:home")
    return render(request,"Doctors/contact.html",{})



