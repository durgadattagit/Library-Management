from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Book
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# def front_page(request):
#      # if request.
#     return render(request, "00_about.html")


def Student_page(request):
    # if 
    return render(request,"04student.html")

def student_signup_page(request):
    if request.method == "POST":
        data = request.POST

        enrolment =data.get('enrolment') 
        # reg_number = data.get('reg_number')
        year_sem = data.get('year_sem')
        department = data.get('department')
        username = data.get('username')
        password = data.get('password')
        
        print(enrolment)
        # print(reg_number)
        print(year_sem)
        print(department)
        print(username)

        user = User.objects.filter(usernane = username)

        if user.exists():
            messages.info(request,"You can chose different Reg_Number number, its alredy taken")
            return redirect("/student_signup_page/")

        user = User.objects.create(
            enrolment = enrolment,
            # reg_number = reg_number,
            year_sem = year_sem,
            department = department,
            username = username,
        )
        user.set_password(password)
        user.save() 
        queryset = User.objects.all()  
        print(queryset)  
        
        context = {'students' : queryset }
        messages.info(request,"Your account has been created succesfully")
        return redirect("/student_login_page/",context)
     
    return render(request, "05studentsignup.html")

def student_login_page(request):
    if request.method == "POST":
        # user_email = request.POST.get("user_email")
        username = request.POST.get("username")
        password = request.POST.get("password")
       
        if not User.objects.filter(username = username).exists():
            messages.error(request,"Invalid Email")
            return redirect("/student_login_page/")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request,"Invalid passwprd")
            return redirect("/student_login_page/")
        else:
            login(request,user)
            return redirect("")
            
    return render(request, "06studentlogin.html")


def student_logout_page(request):
    logout("")
    return (request, "")



def admin_page(request):
    return render(request, "01admin.html")

def admin_signup_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        # reg_number = request.POST.get("reg_number")
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = User.objects.filter(username = username)
        # user = User.objects.filter(reg_number = reg_number)
        if user.exists():
            messages.info(request,"Reg_Number alredy taken")
            return redirect("/admin_signup_page/")
        
        user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                # reg_number = reg_number,
                username = username,
        )
        user.set_password(password)
        user.save()

        # x = User.objects.all()
        
        messages.info(request,"your accounrt succesfully created")
        return redirect('/admin_signup_page/')
    return render(request, "02adminsignup.html")


def admin_login_page(request):     
    if request.method == "POST":   
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request,"Invalid User")
            return redirect("/admin_login_page/")

        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request,"Invalid password")
            return redirect("/admin_login_page/")
        else:
            login(request,user)
            return redirect("/student_signup_page/")
    return render(request, "03adminLogin.html")

def admin_logout_page(request):
    logout("")
    return (request, "")






def add_BOOK(request):
    recommended_books = Book.objects.filter(recommended_books =True)
    coding_books = Book.objects.filter(coding_books = True)
    business_book = Book.objects.filter(business_book = True)
    friction_books = Book.objects.filter(friction_books = True)
    

    # if request.method == "POST":
    #     book_name = request.POST.get('book_name')
    #     Author = request.POST.get('Author')
    #     ISBN = request.POST.get('ISBN')
    #     summery = request.POST.get('summery')
    #     cover_image = request.POST.FILES.get('cover_image')
    #     Category = request.POST.get('Category')
        
    #     user = Book.objects.filter(book_name = book_name, Author = Author)
    #     if user.exists():
    #         messages.info(request,"This Book name and auther is alteady exists ")
            
    #     Book.objects.create(
    #         book_name = book_name,
    #         Author = Author,
    #         ISBN = ISBN,
    #         summery = summery,
    #         cover_image = cover_image,
    #         Category = Category,
    #      )
    #     return redirect("/add_BOOK/")
    
    # queryset = Book.objects.all()
    
    # context = {'add_BOOK':queryset}
    return render(request,"08addbook.html", {'recommended_books':recommended_books,'coding_books':coding_books,'business_book':business_book,'friction_books':friction_books})



def issue_book(request):
    if request.method == "POST":
        enrolment = request.POST.get('enrolment')
        ISBN = request.POST.get('ISBN')
        issue_date = request.get('issu_date')
        expary_date = request.get('expary_date')


    #     user = Issuebook.objects.filter(book_name = book_name, Author = Author)
    #     if user.exists():
    #         messages.info(request,"This Book name and auther is alteady exists ")
            
    bool.objects.create(
        enrolment = enrolment,
        ISBN = ISBN,
        issue_date = issue_date,
        expary_date = expary_date,
    )
    
    return render(request,"07issuebook.html")


def Avalable_book(request):
    # if request.method == "POST":
    #     data = request.POST
    recommended_books = Book.objects.filter(recommended_books =True)
    coding_books = Book.objects.filter(coding_books = True)
    business_book = Book.objects.filter(business_book = True)
    friction_books = Book.objects.filter(friction_books = True)

    return render(request,"09avalablebook.html",{'recommended_books':recommended_books,'coding_books':coding_books,'business_book':business_book,'friction_books':friction_books})


# def bookissue_to_you_Studentpart(request, username):
#     queryset = User.objects.get(username = username)

#     if request.method == "POST":
#         first_name = request


#     return render(request,"bookissue_to_you_Studentpart.html")

# def Issuedbook_to_student_adminpart(request):
#     return render(request,"Issuedbook_to_student_adminpart.html")

