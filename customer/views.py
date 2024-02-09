from django.shortcuts import render,redirect
from django.http import HttpResponse
from customer.models import *
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import BookingForm
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

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
   
   if 'email' in request.session:
      user_obj = customers_h.objects.get(email=request.session['email'])
      return render(request,'about.html', {'user_data':user_obj})
   else:
       return render(request, 'index.html', {'msg':'----------------Please login first !!--------------'})

def service_view(request):
   return render(request,'services.html')

def contact_view(request):
   
   if 'email' in request.session:
      user_obj = customers_h.objects.get(email=request.session['email'])
      return render(request,'contact.html', {'user_data':user_obj})
   else:
       return render(request, 'index.html', {'msg':'----------------Please login first !!--------------'})

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


   #)
    
     

   #if len(qs) >= room

#def hotel_detail(request):
   #(request,'services.html',{'message':'This room booked Successfully!!'})

#def check_booking(start_date, end_date):
   #qs = booking.objects.filter(
      #from_date__lte=start_date,
      #till_date__gte=end_date,)
   #room_count = 10
   #if len(qs) >= room_count:
    #  return False
   
   #return True


#def hotel_detail_view(request):
   #if request.method == 'GET':
        #return render(request, 'hotel_detail.html')
   #else:
      #checkin = request.POST.get('checkin')
     # checkout = request.POST.get('checkout')
      #room_no = 10
      #if not check_booking('2024-01-04', '2024-01-06'):
       #  messages.warning(request,'Sorry!! Room is already booked')
        # return redirect(request.META.get('HTTP_REFERER', 'hotel_detail.html'))
      
      #booking.objects.create(customer_id={customers_h.id},room_no=10, from_date='2024-01-04', till_date='2024-01-06')
      #messages.warning(request,'Successfully!!... Room is  booked')
      #return redirect(request.META.get('HTTP_REFERER', 'index.html'))

#def hotel_detail_view(request):
   #return render(request,'hotel_detail.html')
   #if request.method == 'post':
     # global user_data
      #user_data = {
       #     'checkin_ud' :request.POST['start_date'],
        #    'checkout_ud' : request.POST['end_date'],
            #'room_num_ud' : request.POST['room_num'],
         #}
  
      
      
      #form_checkin=request.POST['start_date']
      #global user_obj
      #user_obj=booking.objects.filter(from_date=form_checkin)
      #return render(request,'hotel_detail.html',{'message':'Sorry!! ,This room has already booked.'})
   #else: 
     
      #return render(request,'h.html')
   
   # views.py
def is_room_available(room, start_date, end_date):
    # Get existing bookings that overlap with the selected date range
    existing_bookings = BookingDate.objects.filter(
        room=room,
        date__range=[start_date, end_date]
    )

    # If there are overlapping bookings, the room is not available
    return not existing_bookings.exists()

def room_list(request):
   if 'email' in request.session:
      user_obj = customers_h.objects.get(email=request.session['email'])
      rooms = Room.objects.all()
      return render(request, 'room_list.html', {'rooms': rooms,'user_data':user_obj})
   else:
       return render(request, 'index.html', {'msg':'----------------Please login first !!--------------'})

razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
def book_room(request, room_id):
    room = Room.objects.get(pk=room_id)
   
    if request.method == 'GET':
        form = BookingForm(request.GET)
        if form.is_valid():
            checkin_date = form.cleaned_data['checkin_date']
            checkout_date = form.cleaned_data['checkout_date']

            if is_room_available(room, checkin_date, checkout_date):
                  # Room is available, proceed with the booking logic
                  # For example, you can create a new BookingDate entry for the selected range

                  #payment
                  currency = 'INR'
                  amount = 20000 # Rs. 200
                  razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))
                  # order id of newly created order.
                  razorpay_order_id = razorpay_order['id']
                  callback_url = 'paymenthandler/'
                  # we need to pass these details to frontend.

                
                  #room.available_dates.remove(*booked_dates)
                  context = {}
                  context['razorpay_order_id'] = razorpay_order_id
                  context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
                  context['razorpay_amount'] = amount
                  context['currency'] = currency
                  context['callback_url'] = callback_url

                    # Save theamount = 20000 # Rs. 200 new booking date
                  booking_date = BookingDate.objects.create(room=room, date=checkin_date)
                  room.available_dates.add(booking_date)
                  booking_date = BookingDate.objects.create(room=room, date=checkout_date)
                  room.available_dates.add(booking_date)
                  # Remove the booked dates from the available_dates field
                  booked_dates = BookingDate.objects.filter(
                     room=room,
                     date__range=[checkin_date, checkout_date]
                  )

                  return render(request, 'payment.html', context=context)
            
            else:
                  # Handle case where dates are not available
                  form.add_error(None, 'Selected dates are not available.')
    else:
        form = BookingForm()

    return render(request, 'book_room.html', {'form': form, 'room': room})


from django.shortcuts import render


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is not None:
				amount = 20000 # Rs. 200
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)

					# render success page on successful caputre of payment
					return render(request, 'paymentsuccess.html')
				except:

					# if there is an error while capturing payment.
					return render(request, 'paymentfail.html')
			else:

				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:

			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
	# if other than POST request is made.
		return HttpResponseBadRequest()



