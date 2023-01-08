from django.shortcuts import render,redirect
from .models import UserInfo

# Create your views here.

def index(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        qualification = request.POST['qualification']
        contact = request.POST['contact']
        email = request.POST['email']
        address = request.POST['address']

        info = UserInfo(f_name = f_name,l_name=l_name,qualification=qualification,contact=contact,email=email,address=address)

        info.save()

        return redirect('user_info')

    return render(request,'index.html')

def user_info(request):

    info = UserInfo.objects.all()

    data = {'info':info}

    return render(request,'user_info.html',data)