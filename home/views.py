from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from vage.views import Receipe 
from django.http import HttpResponse 
from .utils import Send_email_to_client , Send_email_with_attachment
from django.conf import settings 
from .forms import EmailForm
from django.core.mail import EmailMessage
# Create your views here.







@login_required(login_url="/login/")
def home(request):
   
    serveses = [
        {"name": "simpel graphic dising","price": 350},
        {"name": "Advance graphic dising","price": 550},
        {"name": "computer composing ","price":50},
        {"name": "online applycation","price":150},
        {"name": "semple photo shoting","price":250},
        {"name": "Advance photo shoting","price":650},
        {"name": "Advance photo edting","price":500},
        {"name": "Advance video editing","price":850},
    ]
        
    if request.method == "POST":
         data = request.POST

         receipe_image = request.FILES.get("receipe_image")
         receipe_name = data.get("receipe_name")
         receipe_description = data.get("receipe_description")
         
         Receipe.objects.create(
              
               receipe_name =  receipe_name ,
               receipe_description = receipe_description,
               receipe_image = receipe_image,

               )
         return redirect("/receipes/")
    
    qureyset = Receipe.objects.all()

    if request.GET.get("Search"):
         qureyset = qureyset.filter(receipe_name__icontains = request.GET.get("Search"))





    context = {"receipes": qureyset,
               "page":"Graphics Printing",
               "serveses":serveses, 
               }
    

    return render(request,"home.t/index.html",context)
 





        
    


@login_required(login_url="/login/")
def contact(requste):
    context = {"page":"contact"}
    return render(requste,"home.t/contact.html",context)

@login_required(login_url="/login/")
def about(requste):
    context = {"page":"about"}
    return render(requste,"home.t/about.html",context )


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = ["graphicsprinting123@gmail.com"]

            mail = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=recipient_list
            )

            # Attach the file if provided
            attachment = request.FILES.get('attachment')
            if attachment:
                mail.attach(attachment.name, attachment.read(), attachment.content_type)

            mail.send()

            return redirect("/")
    else:
        form = EmailForm()


    context = {'form': form}   

    return render(request, 'your_template.html',context )
