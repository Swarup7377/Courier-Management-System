import random

from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from .models import *
from datetime import date
from datetime import datetime
from django.db.models import Count
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    error = ""
    if request.method == "POST":
        sd = request.POST['searchdata']

        try:
            courier = Courier.objects.get(Q(RefNumber=sd))
            report1 = CourierTracking.objects.filter(CourierId=courier)
            reportcount = CourierTracking.objects.filter(CourierId=courier).count()
        except:
            courier = ""
    return render(request, 'index.html', locals())

def branches(request):
    branch = Branch.objects.all()
    return render(request, 'branches.html', locals())

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalcourier = Courier.objects.all().count()
    totalcourierpickup = Courier.objects.filter(Status='Courier Pickup').count()
    totalcouriershipped = Courier.objects.filter(Status='Shipped').count()
    totalcourierintransit = Courier.objects.filter(Status='Intransit').count()
    totalcourieratdes = Courier.objects.filter(Status='Arrived at Destination').count()
    totalcourieroutfordelivery = Courier.objects.filter(Status='Out for Delivery').count()
    totalcourierdelivery = Courier.objects.filter(Status='Delivered').count()
    totalbranch = Branch.objects.all().count()
    totalstaff = Staff.objects.all().count()
    return render(request, 'admin/dashboard.html', locals())

def addBranch(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    if request.method == "POST":
        BranchName = request.POST['BranchName']
        BranchContactnumber = request.POST['BranchContactnumber']
        BranchEmail = request.POST['BranchEmail']
        BranchAddress = request.POST['BranchAddress']
        BranchCity = request.POST['BranchCity']
        BranchState = request.POST['BranchState']
        BranchPincode = request.POST['BranchPincode']
        BranchCountry = request.POST['BranchCountry']

        try:
            Branch.objects.create(BranchName=BranchName, BranchContactnumber=BranchContactnumber, BranchEmail=BranchEmail,
                                  BranchAddress=BranchAddress, BranchCity=BranchCity, BranchState=BranchState, BranchPincode=BranchPincode,
                                  BranchCountry=BranchCountry)
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/addBranch.html', locals())

def manageBranch(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    branch = Branch.objects.all()
    return render(request, 'admin/manageBranch.html', locals())

def editBranch(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    branch = Branch.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        BranchName = request.POST['BranchName']
        BranchContactnumber = request.POST['BranchContactnumber']
        BranchEmail = request.POST['BranchEmail']
        BranchAddress = request.POST['BranchAddress']
        BranchCity = request.POST['BranchCity']
        BranchState = request.POST['BranchState']
        BranchPincode = request.POST['BranchPincode']
        BranchCountry = request.POST['BranchCountry']

        branch.BranchName = BranchName
        branch.BranchContactnumber = BranchContactnumber
        branch.BranchEmail = BranchEmail
        branch.BranchAddress = BranchAddress
        branch.BranchCity = BranchCity
        branch.BranchState = BranchState
        branch.BranchPincode = BranchPincode
        branch.BranchCountry = BranchCountry

        try:
            branch.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/editBranch.html', locals())

def deleteBranch(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    branch = Branch.objects.get(id=pid)
    branch.delete()
    return redirect('manageBranch')

def addStaff(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    branch = Branch.objects.all()
    error=""
    if request.method == "POST":
        bid = request.POST['branch']
        branchid = Branch.objects.get(id=bid)

        fname = request.POST['firstName']
        StaffMobilenumber = request.POST['StaffMobilenumber']
        email = request.POST['emailid']
        pwd = request.POST['Password']

        try:
            user = User.objects.create_user(username=email, password=pwd, first_name=fname)
            Staff.objects.create(user=user, branch=branchid, StaffMobilenumber=StaffMobilenumber)
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/addStaff.html', locals())

def manageStaff(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    staff = Staff.objects.all()
    return render(request, 'admin/manageStaff.html', locals())

def editStaff(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    branch = Branch.objects.all()
    staff = Staff.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        bid = request.POST['branch']
        branchid = Branch.objects.get(id=bid)

        fname = request.POST['firstName']
        StaffMobilenumber = request.POST['StaffMobilenumber']

        staff.user.first_name = fname
        staff.branch = branchid
        staff.StaffMobilenumber = StaffMobilenumber

        try:
            staff.user.save()
            staff.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/editStaff.html', locals())

def deleteStaff(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    User.objects.get(id=pid).delete()
    return redirect('manageStaff')

def newCourier(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    courier = Courier.objects.filter(Status__isnull=True)
    return render(request, 'admin/newCourier.html', locals())

def courierPickup(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    courier = Courier.objects.filter(Status='Courier Pickup')
    return render(request, 'admin/courierPickup.html', locals())

def shipped(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    courier = Courier.objects.filter(Status='Shipped')
    return render(request, 'admin/shipped.html', locals())

def intransit(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    courier = Courier.objects.filter(Status='Intransit')
    return render(request, 'admin/intransit.html', locals())

def arriveatDestination(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    courier = Courier.objects.filter(Status='Arrived at Destination')
    return render(request, 'admin/arriveatDestination.html', locals())

def outforDelivery(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    courier = Courier.objects.filter(Status='Out for Delivery')
    return render(request, 'admin/outforDelivery.html', locals())

def delivered(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    courier = Courier.objects.filter(Status='Delivered')
    return render(request, 'admin/delivered.html', locals())

def totalCourier(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    courier = Courier.objects.all()
    return render(request, 'admin/totalCourier.html', locals())

def deleteCourier(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    courier = Courier.objects.get(id=pid)
    courier.delete()
    return redirect('totalCourier')

def viewCourierDetails(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    courierdtls = Courier.objects.get(id=pid)
    report1 = CourierTracking.objects.filter(CourierId=courierdtls)
    reportcount = CourierTracking.objects.filter(CourierId=courierdtls).count()
    return render(request, 'admin/viewCourierDetails.html', locals())

def betweendateReport(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        fd = request.POST['fromDate']
        td = request.POST['toDate']
        rtype = request.POST['requesttype']
        if rtype == "all":
            courier = Courier.objects.filter((Q(CourierDate__gte=fd) & Q(CourierDate__lte=td)))
        else:
            courier = Courier.objects.filter((Q(CourierDate__gte=fd) & Q(CourierDate__lte=td)),Status=rtype)

        return render(request, 'admin/betweendateReportDtls.html', locals())
    return render(request, 'admin/betweendateReport.html')

def requestCount(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        fd = request.POST['fromDate']
        td = request.POST['toDate']

        courier = Courier.objects.filter(Q(CourierDate__gte=fd) & Q(CourierDate__lte=td))
        totalcouriershipped = Courier.objects.filter(Status='Shipped').count()
        return render(request, 'admin/requestcountdtls.html', locals())
    return render(request, 'admin/requestCount.html')

def salesReport(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin/salesReport.html')

def search(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    sd = None
    if request.method == "POST":
        sd = request.POST['searchdata']
        try:
            courier = Courier.objects.filter(Q(RefNumber=sd))
        except:
            courier = ""
    return render(request, 'admin/search.html', locals())

def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'admin/changePassword.html', locals())


def staff_login(request):
    if request.method == 'POST':
        e = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=e, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'staff_login.html', locals())

def staffdashboard(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)

    totalcourier = Courier.objects.all().count()
    totalcourierpickup = Courier.objects.filter(Status='Courier Pickup').count()
    totalcouriershipped = Courier.objects.filter(Status='Shipped').count()
    totalcourierintransit = Courier.objects.filter(Status='Intransit').count()
    totalcourieratdes = Courier.objects.filter(Status='Arrived at Destination').count()
    totalcourieroutfordelivery = Courier.objects.filter(Status='Out for Delivery').count()
    totalcourierdelivery = Courier.objects.filter(Status='Delivered').count()

    return render(request, 'staff/staffdashboard.html', locals())

def profile(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)

    if request.method == "POST":
        firstName = request.POST['firstName']
        StaffMobilenumber = request.POST['StaffMobilenumber']

        staff.user.first_name = firstName
        staff.StaffMobilenumber = StaffMobilenumber

        try:
            staff.user.save()
            staff.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'staff/profile.html', locals())

def addCourier(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)

    staffbranch = staff.branch
    courier = Courier.objects.filter(SenderBranch=staffbranch)

    error=""
    if request.method == "POST":
        branchid = request.POST['SenderBranch']
        branchh = Branch.objects.get(id=branchid)
        refNo = str(random.randint(10000000, 99999999))
        SenderName = request.POST['SenderName']
        SenderContactnumber = request.POST['SenderContactnumber']
        SenderAddress = request.POST['SenderAddress']
        SenderCity = request.POST['SenderCity']
        SenderState = request.POST['SenderState']
        SenderPincode = request.POST['SenderPincode']
        SenderCountry = request.POST['SenderCountry']
        RecipientName = request.POST['RecipientName']
        RecipientContactnumber = request.POST['RecipientContactnumber']
        RecipientAddress = request.POST['RecipientAddress']
        RecipientCity = request.POST['RecipientCity']
        RecipientState = request.POST['RecipientState']
        RecipientPincode = request.POST['RecipientPincode']
        RecipientCountry = request.POST['RecipientCountry']
        CourierDes = request.POST['CourierDes']
        ParcelWeight = request.POST['ParcelWeight']
        ParcelDimensionlen = request.POST['ParcelDimensionlen']
        ParcelDimensionwidth = request.POST['ParcelDimensionwidth']
        ParcelDimensionheight = request.POST['ParcelDimensionheight']
        ParcelPrice = request.POST['ParcelPrice']

        try:
            Courier.objects.create(SenderBranch=branchh, RefNumber=refNo, SenderName=SenderName, SenderContactnumber=SenderContactnumber, SenderAddress=SenderAddress,
                                   SenderCity=SenderCity, SenderState=SenderState, SenderPincode=SenderPincode, SenderCountry=SenderCountry,
                                   RecipientName=RecipientName, RecipientContactnumber=RecipientContactnumber, RecipientAddress=RecipientAddress, RecipientCity=RecipientCity,
                                   RecipientState=RecipientState, RecipientPincode=RecipientPincode, RecipientCountry=RecipientCountry, CourierDes=CourierDes, ParcelWeight=ParcelWeight,
                                   ParcelDimensionlen=ParcelDimensionlen, ParcelDimensionwidth=ParcelDimensionwidth, ParcelDimensionheight=ParcelDimensionheight, ParcelPrice=ParcelPrice)
            error = "no"
        except:
            error = "yes"
    return render(request, 'staff/addCourier.html', locals())

def staffcouriers(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)
    courier = Courier.objects.filter(Status__isnull=True)
    return render(request, 'staff/staffcouriers.html', locals())

def staffcourierPickup(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)

    courier = Courier.objects.filter(Status='Courier Pickup')
    return render(request, 'staff/staffcourierPickup.html', locals())

def staffshipped(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)

    courier = Courier.objects.filter(Status='Shipped')
    return render(request, 'staff/staffshipped.html', locals())

def staffintransit(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)

    courier = Courier.objects.filter(Status='Intransit')
    return render(request, 'staff/staffintransit.html', locals())

def staffarriveatDestination(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)

    courier = Courier.objects.filter(Status='Arrived at Destination')
    return render(request, 'staff/staffarriveatDestination.html', locals())

def staffoutforDelivery(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)

    courier = Courier.objects.filter(Status='Out for Delivery')
    return render(request, 'staff/staffoutforDelivery.html', locals())

def staffdelivered(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)

    courier = Courier.objects.filter(Status='Delivered')
    return render(request, 'staff/staffdelivered.html', locals())

def stafftotalCourier(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    staff = Staff.objects.get(user=user)

    courier = Courier.objects.all()
    return render(request, 'staff/stafftotalCourier.html', locals())

def staffviewCourierDetails(request,pid):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    courierdtls = Courier.objects.get(id=pid)
    report1 = CourierTracking.objects.filter(CourierId=courierdtls)

    reportcount = CourierTracking.objects.filter(CourierId=courierdtls).count()

    if request.method == "POST":
        remark = request.POST['remark']
        status = request.POST['status']

        try:
            reporttracking = CourierTracking.objects.create(CourierId=courierdtls, remark=remark, status=status, StatusDate=date.today())
            courierdtls.Status = status
            courierdtls.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'staff/staffviewCourierDetails.html', locals())

def searchCourier(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    sd = None
    if request.method == "POST":
        sd = request.POST['searchdata']
        try:
            courier = Courier.objects.filter(Q(RefNumber=sd))
        except:
            courier = ""
    return render(request, 'staff/searchCourier.html', locals())

def staffchangePassword(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'staff/staffchangePassword.html', locals())

def Logout(request):
    logout(request)
    return redirect('index')
