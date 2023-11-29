from django.shortcuts import render,redirect
from .models import * 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


@login_required(login_url="/login/")
def receipes(request):
    
    
    
    
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





    context = {"receipes": qureyset,"page": "Receipe"}
    

    return render(request,"receipe.html",context)



@login_required(login_url="/login/")
def Update_receipe(request , slug):


     queryset = Receipe.objects.get(slug=slug)
     if request.method == "POST":
           data = request.POST
           receipe_image = request.FILES.get("receipe_image")
           receipe_name = data.get("receipe_name")
           receipe_description = data.get("receipe_description")

           queryset.receipe_name = receipe_name
           queryset.receipe_description = receipe_description

           if receipe_image :
                queryset.receipe_image = receipe_image

           queryset.save()
           return redirect("/receipes/")      


     context ={"receipe": queryset}
     return render(request,"Update_receipes.html",context)



@login_required(login_url="/login/")
def Delete_receipe(request,id):
     

     queryset = Receipe.objects.get(id = id)
     queryset.delete()
     
    

     return redirect("/receipes/")
 

     
def login_page(request):

     if request.method == "POST":
          phone_number = request.POST.get("phone_number")
          password = request.POST.get("password")
          
          if not get_user_model().objects.filter(phone_number = phone_number).exists():
               messages.error(request, "Invalad username.")
               return redirect("/login/")
          
          user = authenticate(phone_number = phone_number, password = password)

          if user is None :
               messages.error(request, "Invalad password")
               return redirect("/login/")
          
          else :
               login(request,user)
               return redirect("/receipes/")


          

     return render(request,"login.html")




def logout_page(request):

     logout(request)

     return redirect("/login/")



def Register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        user_bio = request.POST.get("user_bio")
        user_profile_image = request.FILES.get("user_profile_image")
        password = request.POST.get("password")

        # Check if the phone number already exists
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Phone number is already taken.")
            return redirect("/register/")

        # Create a new user
        user = get_user_model().objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            user_bio=user_bio,
            user_profile_image=user_profile_image,
        )

        # Set the password
        user.set_password(password)
        user.save()

        messages.success(request, "Account was created successfully.")
        return redirect("/register/")

    return render(request, "register.html")





@login_required(login_url="/login/")
def Get_students(request):


     queryset = Student.objects.all()
     
     if request.GET.get("Search"):
          Search = request.GET.get("Search")

          queryset = queryset.filter(
               Q(student_name__icontains = Search) | 
               Q(department__department__icontains = Search) |
               Q(student_id__student_id__icontains = Search) | 
               Q(student_email__icontains = Search)  
                )
      
     paginator = Paginator(queryset, 20)  # Show 20 contacts per page.

     page_number = request.GET.get("page",1)
     page_obj = paginator.get_page(page_number)


     print(page_obj)

     return render(request,"ReportCard/students.html", {"queryset":page_obj})


from .seed import Generate_report_card
@login_required(login_url="/login/")
def See_marks(request, student_id):
    # Retrieve student name and age from Student modele 
    #Generate_report_card()
    try:
        student = Student.objects.get(student_id__student_id=student_id)
        student_name = student.student_name
        student_age = student.student_age
        
    except Exception as e:
        
        print(e)

    # Retrieve subject marks for the given student_id
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id).order_by("-student__student_name")

    # Calculate total marks for the student
    
    total_marks = queryset.aggregate(total_marks=Sum("marks"))

    

    # Pass the data to the template
    context = {
        "queryset": queryset,
        "total_marks": total_marks,
        "student_name": student_name,
        "student_age": student_age,
        
    }

    return render(request, "ReportCard/see_marks.html", context)