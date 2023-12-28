from django.contrib import admin
from django.urls import path
from courier.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('branches/', branches, name='branches'),
    path('admin_login', admin_login, name='admin_login'),
    path('staff_login', staff_login, name='staff_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('addBranch', addBranch, name='addBranch'),
    path('manageBranch', manageBranch, name='manageBranch'),
    path('editBranch/<int:pid>', editBranch, name='editBranch'),
    path('deleteBranch/<int:pid>', deleteBranch, name='deleteBranch'),
    path('addStaff', addStaff, name='addStaff'),
    path('manageStaff',manageStaff, name='manageStaff'),
    path('editStaff/<int:pid>', editStaff, name='editStaff'),
    path('deleteStaff/<int:pid>', deleteStaff, name='deleteStaff'),
    path('newCourier', newCourier, name='newCourier'),
    path('courierPickup', courierPickup, name='courierPickup'),
    path('shipped', shipped, name='shipped'),
    path('intransit', intransit, name='intransit'),
    path('arriveatDestination', arriveatDestination, name='arriveatDestination'),
    path('outforDelivery', outforDelivery, name='outforDelivery'),
    path('delivered', delivered, name='delivered'),
    path('totalCourier', totalCourier, name='totalCourier'),
    path('deleteCourier/<int:pid>', deleteCourier, name='deleteCourier'),
    path('viewCourierDetails/<int:pid>', viewCourierDetails, name='viewCourierDetails'),
    path('betweendateReport', betweendateReport, name='betweendateReport'),
    path('requestCount', requestCount, name='requestCount'),
    path('salesReport', salesReport, name='salesReport'),
    path('search', search, name='search'),
    path('changePassword', changePassword, name='changePassword'),


    path('staffdashboard', staffdashboard, name='staffdashboard'),
    path('profile', profile, name='profile'),
    path('addCourier', addCourier, name='addCourier'),
    path('staffcouriers', staffcouriers, name='staffcouriers'),
    path('staffcourierPickup', staffcourierPickup, name='staffcourierPickup'),
    path('staffshipped', staffshipped, name='staffshipped'),
    path('staffintransit', staffintransit, name='staffintransit'),
    path('staffarriveatDestination', staffarriveatDestination, name='staffarriveatDestination'),
    path('staffoutforDelivery', staffoutforDelivery, name='staffoutforDelivery'),
    path('staffdelivered', staffdelivered, name='staffdelivered'),
    path('stafftotalCourier', stafftotalCourier, name='stafftotalCourier'),
    path('searchCourier', searchCourier, name='searchCourier'),
    path('staffviewCourierDetails/<int:pid>', staffviewCourierDetails, name='staffviewCourierDetails'),
    path('staffchangePassword', staffchangePassword, name='staffchangePassword'),

    path('logout/', Logout, name='logout'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
