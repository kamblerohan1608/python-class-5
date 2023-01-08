from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LoginForm,Add_blog_Form
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import BlogModel
from django.contrib.auth.models import User,Group
# Create your views here.


class home(View):

    def get(self,request):

        form = LoginForm()

        if request.user.is_authenticated is False:
            return render(request,'MyApp/home.html',{'form':form})
        else:
            return redirect('blogs')

    def post(self,request):

        form = LoginForm(request.POST,data=request.POST)

        if form.is_valid():
            # print('form is valid')
            u_name=form.cleaned_data['username']
            u_pass=form.cleaned_data['password']
            # print(u_name,u_pass)

            user = authenticate(username=u_name,password=u_pass)
            if user is not None:
                login(request,user)
                messages.success(request,f'successfully user {u_name} login')
                return redirect('dashboard')
                
        messages.warning(request,'Something went wrong')       
        return render(request,'MyApp/home.html',{'form':form})

class register(View):

    def get(self,request):

        form = RegisterForm()

        return render(request,'MyApp/register.html',{'form':form})

    def post(self,request):

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            g = Group.objects.get(name='author')
            users = User.objects.all()
            for u in users:
                g.user_set.add(u)

            messages.success(request,'user registered successfully ')
            return redirect('home')


        return render(request,'MyApp/register.html',{'form':form})

class dashboard(View):

    def get(self,request):

        if request.user.is_authenticated:
            data = BlogModel.objects.all()
            return render(request,'MyApp/dashboard.html',{'data':data})
        else:
            return redirect('home')
    def post(self,request):
        return render(request,'MyApp/dashboard.html')


class signout(View):
    def get(self,request):

        logout(request)
        messages.success(request,'successfully loged out')
        return redirect('home')
        # return render(request , 'MyApp/home.html')

class blogs(View):
    def get(self,request):
        data = BlogModel.objects.all()
        return render(request,'MyApp/blogs.html',{'data':data})

class add_blog(View):
    def get(self,request):
        form=Add_blog_Form()
        return render(request,'MyApp/add_blog.html',{'form':form})

    def post(self,request):
        form=Add_blog_Form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        return render(request,'MyApp/add_blog.html')

class delete_blog(View):
    def get(self,request,pk):
        data = BlogModel.objects.get(id=pk)
        data.delete()
        messages.success(request,'Successfully deleted')
        return redirect('dashboard')

class edit_blog(View):
    def get(self,request,pk):
        data = BlogModel.objects.get(id=pk)
        return render(request,'MyApp/edit_blog.html',{'data':data})