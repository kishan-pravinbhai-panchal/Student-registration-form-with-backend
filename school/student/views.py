from django.shortcuts import render
from .forms import StudForm
from .models import stud


# Create your views here.
def show (request):
    return render(request,"home.html" )
def register (request):
   title="Student Regestration"
   form= StudForm(request.POST or None) 

   if form.is_valid():
       name = form.cleaned_data['s_name']
       clas = form.cleaned_data['s_class']
       addr = form.cleaned_data['s_addr']
       school = form.cleaned_data['s_school']
       mail = form.cleaned_data['s_email']

       p = stud(s_name=name ,s_class=clas,s_addr=addr,s_school=school,s_email=mail)
       p.save()
       return render (request,'ack.html',{"title":"Regestration successfully" })
   context={
       "title":title,
       "form":form,
   }
   return render (request,'regester.html',context)

def existing(request):
    title="All The Registrate Students"
    queryset = stud.objects.all()

    context = {
        "title":title,
         "queryset":queryset ,  
           }
    return render (request,'existing.html',context)