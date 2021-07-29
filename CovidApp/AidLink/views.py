from django.shortcuts import render,redirect
from .models import *
from .forms import *

SUB_TYPE=(

        ("0","Oxygen-NewCylinder"),
        ("1","Oxygen-Refill"),
        ("2","Beds-Information"),
        ("3","Beds-Formalities"),
        ("4","Medicines"),
        ("5","FoodDelivery"),
        ("6","Groceries"),
        ("7","Amenities")
)

def index(request):

    return render(request,'AidLink/index.html') 

def welcomePage(request):
    
    return render(request,'AidLink/welcomePage.html')

def saveVolunteer(volunteer):
    vol = Volunteers()
    vol.name=volunteer[0]
    vol.email=volunteer[1]
    vol.address=volunteer[2]
    vol.pincode=volunteer[3]
    vol.contact_Call=volunteer[4]
    vol.contact_WA=volunteer[5]
    vol.save()
    print(volunteer[6])
    id = vol.volunteer_id
    for i in volunteer[6]:
        res = Resource()
        res.volunteers_id=id
        res.res_type=i
        res.save()
        print(res.res_type)


    print(vol.name)



def volunteerRegister(request):
    context = {}
    if request.method=="POST":
        form=VolunteerRegisterForm(request.POST)
        context['form']=form
        volunteer = []
        print("POST METHOD")
        if form.is_valid():
            print("inside form")
            volunteer.append(form.cleaned_data['name'])
            volunteer.append(form.cleaned_data['email'])
            volunteer.append(form.cleaned_data['address'])
            volunteer.append(form.cleaned_data['pincode'])
            volunteer.append(form.cleaned_data['call'])
            volunteer.append(form.cleaned_data['whatsApp'])
            volunteer.append(form.cleaned_data['res_type_fields'])

        saveVolunteer(volunteer)
        print(volunteer)
        return redirect('welcomePage')
    else:
        form=VolunteerRegisterForm()
        context['form']=form

    return render(request,'AidLink/volunteerRegister.html',context)


def volunteerLogin(request):
    volunteer = Volunteers.objects.all()
    if request.method=="POST":
        email=request.POST.get("email")
        phone=request.POST.get("phone-number")
        print(email)
        print(phone)
        print("inside form")
        f=0
        for v in volunteer:
            print(v.email)
            print(v.contact_Call)
            if v.email==email and v.contact_Call==phone:
                print("exists")
                f=1
                return redirect('welcomePage')
            
        if f==0:
            print("does not exist")
            return redirect('volunteerRegister')
    return render(request,'AidLink/volunteerLogin.html')

def showResources(type):
    resourceList=[]
    volunteer_set=set()
    for i in SUB_TYPE:
        if i[0]==type:
            print(i[1])
    resource_objects=Resource.objects.all()
    for r in resource_objects:
        if r.res_type==type:
            volunteer_set.add(r.volunteers_id)
    volunteer_object=Volunteers.objects.filter(volunteer_id__in=list(volunteer_set))
    for v in volunteer_object:
        resourceList.append(v)

    return resourceList

def resources(request):
    print("resources")
    context={}
    type=[]
    res_List=[]
    if request.method=="POST":
        form=ResourceDetailsForm(request.POST)
        context['form']=form
        if form.is_valid():
            type.append(form.cleaned_data['super_type'])
            type.append(form.cleaned_data['sub_type'])
        res_List = showResources(type[1])              
    else:
        form=ResourceDetailsForm()
        context['form']=form
    context['List']=res_List
    return render(request,'AidLink/resources.html',context)

def donations(request):
    print("donations")
    return render(request,'AidLink/donations.html')

def getDonations(type):
    List=[]
    result={}
    dons=Donations.objects.filter(donation_type=type)
    for d in dons:
        result={}
        print("Hello")
        for i in Donations.CAUSE_TYPE:
            if i[0]==d.cause_type:
                result['cause']=i[1]
        print(d.cause_type)
        result['amount']=d.amount_wanting
        print(d.amount_wanting)
        id=d.donation_id
        rec=ReciverDetails.objects.get(donation_id=id)
        result['name']=rec.name
        result['address']=rec.address
        result['pincode']=rec.pincode
        result['contact_Call']=rec.contact_Call
        result['contact_WA']=rec.contact_WA
        result['email']=rec.email
        List.append(result)

    return List

def donorPage(request):
    context={}
    context['List']=[]
    if request.method=="POST":
        form=DonorShowForm(request.POST)
        context['form']=form
        if form.is_valid():
            don_type=form.cleaned_data['donation_type']
        context['List']=getDonations(don_type)
    else:
        form=DonorShowForm()
        context['form']=form
    
    return render(request,'AidLink/donorPage.html',context)

def donatePage(request):

    return render(request,'AidLink/donatePage.html')

def setDonation(donation):
    donation_obj=Donations()
    donation_obj.donation_type=donation[0]
    donation_obj.cause_type=donation[1]
    donation_obj.amount_wanting=donation[2]
    donation_obj.save()
    return donation_obj.donation_id

def setReciever(reciever,id):
    reciever_obj=ReciverDetails()
    reciever_obj.name=reciever[0]
    reciever_obj.address=reciever[1]
    reciever_obj.pincode=reciever[2]
    reciever_obj.contact_Call=reciever[3]
    reciever_obj.contact_WA=reciever[4]
    reciever_obj.email=reciever[5]
    reciever_obj.donation_id=id
    reciever_obj.save()

def donationRegister(request):
    context={}
    donation=[]
    reciever=[]
    if request.method=="POST":
        form=DonationRegisterForm(request.POST)
        context['form']=form
        if form.is_valid():
            donation.append(form.cleaned_data['donation_type'])
            donation.append(form.cleaned_data['cause_type'])
            donation.append(form.cleaned_data['amount_wanting'])
            reciever.append(form.cleaned_data['name']) 
            reciever.append(form.cleaned_data['address'])
            reciever.append(form.cleaned_data['pincode'])
            reciever.append(form.cleaned_data['call'])
            reciever.append(form.cleaned_data['whatsApp'])
            reciever.append(form.cleaned_data['email'])

        print(donation)
        print(reciever)
        don_id = setDonation(donation)
        setReciever(reciever,don_id)
        print("Donation & Reciever Saved")
        return redirect('donations')
            
    else:
        form=DonationRegisterForm()
        context['form']=form

    return render(request,'AidLink/donationRegisterPage.html',context)

def volunteer(request):
    print("volunteer")
    return render(request,'AidLink/volunteer.html')

def floatVolunteers(request):
    List=[]
    res = Resource.objects.filter(res_type="8")
    for r in res:
        result={}
        id=r.volunteers_id
        rec=Volunteers.objects.get(volunteer_id=id)
        result['name']=rec.name
        result['address']=rec.address
        result['pincode']=rec.pincode
        result['contact_Call']=rec.contact_Call
        result['contact_WA']=rec.contact_WA
        result['email']=rec.email
        List.append(result)
    

    return render(request,'AidLink/floatVolunteers.html',{
        'List':List
    })
