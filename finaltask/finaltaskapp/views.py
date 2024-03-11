
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import order,department,course
from .forms import orderForm
# Create your views here.
def index(request):
    return render(request,"base.html")

def order(request):
    form = orderForm()
    if request.method =='POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirm')
    return render(request, 'order.html', {'form': form})

def register(request):
    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        cpassword1=request.POST['cpassword']
        if password1==cpassword1:
            if User.objects.filter(username=username1).exists():
                messages.info(request,"Username already taken...")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username1,password=password1)
                user.save();
                print("user created..")
                return redirect('login')
        else:
            messages.info(request,"password not matching....")
            return redirect("register")
        return redirect("/")
    return render(request, "register.html")

def login(request):
    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        user=auth.authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request,user)
            print("logged in")
            return redirect("placeorder")
        else:
            messages.info(request,"invalid credentials")

            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

def placeorder(request):

    return render(request,'placeorder.html')

def confirm(request):
     return render(request,'confirm.html')


# AJAX
def load_courses(request):
    dept_id = request.GET.get('dept_id')
    courses = course.objects.filter(dept_id=dept_id).all()
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)