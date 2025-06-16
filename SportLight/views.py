from sre_constants import CATEGORY

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

from SportLight.models import *


# Create your views here.
def index(request):
    allevents = EVENT.objects.all()
    print(allevents)
    context = {
        'eventdata': allevents
    }
    return render(request,'index.html',context)


def Registretion(request):
    return render(request,'Registretion.html')

def insertregister(request):
    uname=request.POST.get('name')
    udob=request.POST.get('dob')
    uemail=request.POST.get('email')
    uphone=request.POST.get('phone')
    upassword=request.POST.get('password')
    urole=request.POST.get('urol')
    # ustatus=request.POST.get('usta')
    uaddres=request.POST.get('address')
    ugender=request.POST.get('gender')
    udp=request.FILES['id_image']

    if Registretion.objects.filter(EMAIL=uemail).exists():
        messages.error(request, 'Account already exists')
        return render(request,'Registretion.html')
    else:
        insertquery=Registretion(NAME=uname,DOB=udob,EMAIL=uemail,PHONE=uphone,PASSWORD=upassword,ROLE=urole,ADDRESS=uaddres,GENDER=ugender,DP=udp)
        insertquery.save()
        messages.success(request, 'Registeration Successfull')
        return render(request,'login.html')

def login(request):
    return render(request,'login.html')

def verifyuser(request):
    uemail=request.POST.get('email')
    upassword=request.POST.get('password')
    try:
        userdata=Registretion.objects.get(EMAIL=uemail,PASSWORD=upassword)

        request.session['login_id']=userdata.id
        request.session['login_email']=userdata.EMAIL
        request.session['login_name']=userdata.NAME
        request.session['login_role']=userdata.ROLE
        print(request.session['login_role'])
        request.session.save()
        messages.success(request, 'Login Successful')
        return render(request,'index.html')
    except:
        messages.error(request, 'Invail Email OR Password')
        return render(request,'login.html')

def artist_event_form(request):
    allcatdata = CATEGORY.objects.all()
    context = {
        'catdata': allcatdata
    }
    return render(request,'artist-event-form.html',context)
def addevent(request):
    # fetch all category
    # query

    return render(request,'artist-event-form.html')

def insertevent(request):
    seller_id= request.session['login_id']
    ecat = request.POST.get("cat")
    ename= request.POST.get("E_NAME")
    eimage = request.POST.get("E_IMAGE")
    edate= request.POST.get("E_DATE")
    etime = request.POST.get("E_TIME")
    eadd = request.POST.get("E_ADDRESS_MAPLINK")
    eprice=request.POST.get('E_PRICE')
    edes = request.POST.get("E_DESCRIPTION")
    query=EVENT(SELLER_ID=Registretion(id=seller_id),CATEGORY_ID=CATEGORY(id=ecat),E_NAME=ename,E_IMAGE=eimage,E_DATE=edate,E_TIME=etime,E_ADDRESS_MAPLINK=eadd,E_PRICE=eprice,E_DESCRIPTION=edes)
    query.save()
    messages.success(request, 'Event Added Successfully')
    return render(request, 'index.html')


def manageevent(request):
    login_id = request.session['login_id']
    alleventsdat=EVENT.objects.filter(SELLER_ID=login_id)
    context={
        'alleventsdata':alleventsdat
    }
    return render(request,'manage-event.html',context)


def bookinghistory(request):
    login_id = request.session.get('login_id')
    if login_id:
        login_id = int(login_id)  # 👈 Force to integer

    alleventsdata = EVENT.objects.filter(SELLER_ID=login_id)

    context = {
        'alleventbookinghis': alleventsdata
    }
    return render(request, 'bookinghistory.html', context)

def event_list(request):
    events = EVENT.objects.all()  # Fetch all events
    return render(request, 'event_list.html', {'events': events})

def contact(request):
    return render(request,'contact.html')


def insertcontact(request):
    cname= request.POST.get("Name")
    cemaiil = request.POST.get("email")
    csubject= request.POST.get("sub")
    cphn = request.POST.get("phn")
    cmess = request.POST.get("mess")
    query=CONTACT(NAME=cname,EMAIL=cemaiil,SUBJECT=csubject,PHONE=cphn,MESSAGES=cmess)
    query.save()
    messages.success(request, 'Contact form submitted successfully!')

    return render(request, 'index.html')


def about(request):
    return render(request,'about.html')


def events(request):
    allevents = EVENT.objects.all()
    print(allevents)
    context = {
        'eventdata': allevents
    }
    return render(request, 'events.html', context)
def single(request):
    return render(request,'single.html')

def singleevent(request,eid):
    print(eid)

    singledata = EVENT.objects.get(id=eid)
    print(singledata)

    context = {
        'single': singledata
    }
    return render(request, 'single.html', context)

def delete(request,eid):
    eventdata=EVENT.objects.get(id=eid)
    eventdata.delete()
    messages.success(request, 'event deleted sucessfully!!!')
    return redirect(manageevent)

def editevent(request,eid):
    eventdata=EVENT.objects.get(id=eid)
    return render(request,'Edit-event-form.html',{"eventdata":eventdata})

def update(request):
    ename = request.POST.get("E_NAME")
    eimage = request.FILES["E_IMAGE"]
    edate = request.POST.get("E_DATE")
    etime = request.POST.get("E_TIME")
    eadd = request.POST.get("E_ADDRESS_MAPLINK")
    eprice = request.POST.get('E_PRICE')
    edes = request.POST.get("E_DESCRIPTION")
    eid=request.POST.get("eid")
    eventdata=EVENT.objects.get(id=eid)
    eventdata.E_NAME = ename
    eventdata.E_IMAGE = eimage
    eventdata.E_DATA = edate
    eventdata.E_TIME = etime
    eventdata.E_ADDRESS_MAPLINK = eadd
    eventdata.E_PRICE = eprice
    eventdata.E_DESCRIPTION = edes
    eventdata.save()
    messages.success(request, 'Event Updated sucessfully!!!')
    return redirect(manageevent)

def services(request):
    return render(request,'services.html')

def ecomm(request):
    return render(request,'ecomm.html')
def eror(request):
    return render(request,'eror.html')


def logout(request):
    try:
        del request.session['login_id']
        del request.session['login_email']
        del request.session['login_role']
        messages.success(request, 'Logout Successful')
    except:
        messages.error(request, 'Error occured')
    return render(request,'index.html')
import razorpay


def bookEvent(request, event_id):
    event = EVENT.objects.get(id=event_id)
    context = {
        "eventid": event.id,
        "amount": event.E_PRICE
    }
    return render(request, 'book-event.html', context)


def initiate_payment(request):
    if request.method == "POST":
        event_id = request.POST.get("event_id")
        print(event_id)
        event = EVENT.objects.get(id=event_id)
        user = request.session['login_id']# Assuming you store user ID in session

        # Create a Razorpay Order
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET
                                       ))
        order_amount = int(float(event.E_PRICE) * 100)
        razorpay_order = client.order.create({
            "amount": order_amount,
            "currency": "INR",
            "receipt": f"order_rcptid_{user}",
            "payment_capture": "1",
        })

        insertBooking = BOOKING(EVENT_ID=EVENT(id=event.id), Registretion_ID=Registretion(id=user), TOTAL_AMOUNT=event.E_PRICE)
        insertBooking.save()

        orderid = insertBooking.id
        userdata = Registretion.objects.get(id=user)

        context = {
            "razorpay_order_id": razorpay_order['id'],
            "key": settings.RAZORPAY_API_KEY,
            "userdata": userdata,
            "event_id": event.id,
            "amount": event.E_PRICE,
            "orderid":orderid
        }
        return render(request, 'payment.html', context)
    return render(request, 'payment.html')


def verify_payment(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_signature = request.POST.get("razorpay_signature")
        order = BOOKING.objects.get(id=order_id)

        print(order)
        print(razorpay_signature)
        print(razorpay_payment_id)
        try:
            insertpayment = PAYMENT(BOOKING_ID=BOOKING(id=order_id), PAYMENT_ID=razorpay_payment_id, PAYMENT_STATUS="SUCCESS",
                                    AMOUNT=order.TOTAL_AMOUNT, SIGNATURE=razorpay_signature)
            insertpayment.save()

            order.STATUS = "CONFIRMED"
            order.save()
            return redirect(paymentsuccess)
        except:
            return redirect(paymentfail)
    return render(request, "payment.html")


def paymentsuccess(request):
    messages.success(request, "Payment Captured Successful")
    return render(request, "payment_success.html")


def paymentfail(request):
    messages.success(request, "Payment Faild")
    return render(request, "payment_failed.html")