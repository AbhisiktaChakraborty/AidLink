from django.contrib import admin
from django.urls import path
from AidLink import views

urlpatterns = [
    path('',views.index,name="index"),
    path('volunteerRegister/',views.volunteerRegister,name="volunteerRegister"),
    path('volunteerLogin/',views.volunteerLogin,name="volunteerLogin"),
    path('welcomePage/',views.welcomePage,name="welcomePage"),
    path('resources/',views.resources,name="resources"),
    path('donations/',views.donations,name="donations"),
    path('volunteer/',views.volunteer,name="volunteer"),
    path('donorPage/',views.donorPage,name="donorPage"),
    path('floatVolunteer/',views.floatVolunteers,name="floatVolunteers"),
    path('donatePage/',views.donatePage,name="donatePage"),
    path('donationRegisterPage/',views.donationRegister,name="donationRegister"),
    path('admin/', admin.site.urls),
]
