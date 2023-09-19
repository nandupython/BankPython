from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ApplicationForm
from django.http import JsonResponse
from .models import Branch


# Create your views here.
def demo(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,'Invalid Credential')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        cpassword = request.POST["password1"]
        if password==cpassword:
            if User.objects.filter(username=username):
                messages.info(request,'User name Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request,'Password is mismatching')
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# def newpage(request):
#     if request.method == 'POST':
#         form = ApplicationForm(request.POST)
#         if form.is_valid():
#             # Handle the data (save or process) and provide feedback
#             return render(request, 'confirmation.html', {'message': 'Application accepted'})

    # else:
    #     form = ApplicationForm()
    #
    # return render(request, 'form_page.html', {'form': form})

# def get_branches_for_district(request, district_id):
#     branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
#     branch_list = list(branches)
#     return JsonResponse(branch_list, safe=False)
def get_branches_for_district(request, district_id):
    branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
    branch_list = list(branches)
    return JsonResponse(branch_list, safe=False)


def newpage(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
        else:
            print("Form is invalid", form.errors)
            # Handle the data (save or process)

            # Return a render with a message and a link
            return render(request, 'confirmation.html', {'message': 'Application accepted'})
    else:
        form = ApplicationForm()

    return render(request, 'form_page.html', {'form': form})

##NEW CODE ##

