from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def enter(request):
 return render(request, 'index.html')


def index(request):
 return render(request, 'index.html')

def home(request):
 return render(request, 'home.html')



def register(request):
     if request.method == 'POST':  
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password0']

        if password1==password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:    
                user = User.objects.create_user(username = username, password = password1, email = email)
                user.save();
                print('User created')
                return redirect('enter')
                
        else:
            print('password not matching')
            return redirect('register')
        return redirect('signin')

     else:
        return render(request, 'register.html')
#  return render(request, 'register.html')

def signin(request):
    #if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['Password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid details')
            return render(request, 'index.html')
    #else:
        #return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')