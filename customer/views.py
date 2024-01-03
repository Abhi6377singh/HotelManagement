from django.shortcuts import render,redirect
from django.http import HttpResponse
from customer.models import customers_h
from random import randint
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def index_view(request):
    if 'email' in request.session:
      user_obj = customers_h.objects.get(email=request.session['email'])
      return render(request, 'index.html', {'user_data':user_obj})
    else:
       return render(request, 'index.html')

def login(request):
   if request.method=="GET":
      return render(request, 'login.html')
   else:
      try:
         session_user = customers_h.objects.get(email = request.POST['email'])
         if request.POST['password'] == session_user.password:
            request.session['email'] = session_user.email
            return render(request, 'index.html', {'user_data':session_user})
         else:
            return render(request, 'login.html', {'msg':"Invalid Password"})
      except:
         return render(request, 'login.html', {'msg':"The email is not registered"})



def about_view(request):
   return render(request,'about.html')

def service_view(request):
   return render(request,'services.html')

def contact_view(request):
   
   return render(request,'contact.html')

def signup(request):
   global c_otp
   c_otp = randint(100_00,999_999)
   if request.method == 'GET':
        return render(request, 'signup.html')
   else:
        form_email=request.POST['email']
        try:
         
            user_obj=customers_h.objects.get(email= form_email)
            return render(request,'signup.html',{'msg':'This email is already exists.'})
        except:
        # create one row in db table
             if request.POST['password'] == request.POST['cpassword']:
            
                 global user_data
                 user_data = {
                'full_name': request.POST['name'],
                'email': request.POST['email'],
                'password':request.POST['password'],
                'phone': request.POST['phone'],
                'address': request.POST['address'],
                'cpassword': request.POST['cpassword'],
                'address' : request.POST['address'],
                'adharcard_no' : request.POST['adharcard_no']
            }

                 subject = 'Ecommerce Registration'
                 message = f'Hello!! your OTP is {c_otp}'
                 sender = settings.EMAIL_HOST_USER
                 rec = [request.POST['email']]
                 send_mail(subject, message, sender, rec)
                 return render(request, 'otp.html')
             else:
                return render(request, 'signup.html', {'msg': 'BOTH passwords do not matchh!!!'})
   return render(request,'signup.html')

def otp_view(request):
   # global c_otp
   # c_otp = randint(100_00,999_999)
   #return render(request,'otp.html')
   # print(c_otp, request.POST['u_otp'])
   if str(c_otp) == request.POST['u_otp']:
      customers_h.objects.create(
            full_name = user_data['full_name'],
            email = user_data['email'],
            password = user_data['password'],
            address = user_data['address'],
            phone = user_data['phone'],
            Adharcard_no = user_data['adharcard_no']
      )
      return render(request, 'signup.html', {'msg': "Account Created Successfully!!!"})
   else:
      return render(request, 'otp.html', {'msg': "entered OTP is INVALID"})   
   

def logout_view(request):
    del request.session['email']
    return redirect('index')