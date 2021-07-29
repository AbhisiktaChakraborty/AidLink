from django.db import models
'''
Volunteers:
Volunteer_ID Contact-Details        

Resource:
Volunteer_ID    Resource             
  1             oxygenN
  1             oxygenR
'''
class Volunteers(models.Model): #floatVolunteers
    #Field
    volunteer_id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=10,default="700035")
    contact_Call=models.CharField(max_length=10)
    contact_WA=models.CharField(max_length=10)
    email=models.CharField(max_length=25)


class Resource(models.Model):
    #Field
    RESOURCE_TYPE=(
        ("0","Oxygen-NewCylinder"),
        ("1","Oxygen-Refill"),
        ("2","Beds-Information"),
        ("3","Beds-Formalities"),
        ("4","Medicines"),
        ("5","FoodDelivery"),
        ("6","Groceries"),
        ("7","Amenities"),
        ("8","Floating"),
        ("9","Others"),
    )
    res_id=models.BigAutoField(primary_key=True)
    volunteers_id=models.IntegerField(null=False,unique=False)
    res_type=models.CharField(max_length=1,choices=RESOURCE_TYPE)

class Donations(models.Model):
    #Choices
    DONATION_TYPE=(
        ("0","Fundraiser"),
        ("1","Donation")
    )
    CAUSE_TYPE=(
        ("0","Covid-19"),
        ("1","Vaccination"),
        ("2","Medicines"),
        ("3","Transplant"),
        ("4","Others") #set constraint at max20 letters
    )

    donation_type=models.CharField(max_length=1,choices=DONATION_TYPE,default="0")
    cause_type=models.CharField(max_length=1,choices=CAUSE_TYPE,default="0")
    donation_id=models.BigAutoField(primary_key=True)
    amount_wanting=models.IntegerField()
    amount_raised=models.IntegerField(default=0)
    other_type=models.CharField(max_length=20)



class DonorDetails(models.Model):
    donor_id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=10,default="700035")
    contact_Call=models.CharField(max_length=10)
    contact_WA=models.CharField(max_length=10)
    email=models.CharField(max_length=25)
    donation_id=models.IntegerField(unique=False,null=False)

class ReciverDetails(models.Model):
    reciever_id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=10,default="700035")
    contact_Call=models.CharField(max_length=10)
    contact_WA=models.CharField(max_length=10)
    email=models.CharField(max_length=25)
    donation_id=models.IntegerField(unique=False,null=False)



'''class Medical(models.Model):
    #Choices
    RESOURCE_TYPE= (
        ("0","Oxygen-NewCylinder"),
        ("1","Oxygen-Refill"),
        ("2","Beds-Information"),
        ("3","Beds-Formalities"),
        ("4","Medicines")
    )
    #Fields
    res_id=models.BigAutoField(primary_key=True)
    res_type=models.CharField(max_length=1,choices=RESOURCE_TYPE)
    name = models.CharField(max_length=30,default="")
    address=models.CharField(max_length=50,default="")
    contact_Call=models.CharField(max_length=10,default="")
    contact_WA=models.CharField(max_length=10,default="")
    email=models.CharField(max_length=25,default="")

class Resources_Others(models.Model):
    #Choices
    RESOURCE_TYPE= (
        ("0","Food"),
        ("1","Groceries"),
        ("2","Amenities"),
    )
    #Fields
    res_id=models.BigAutoField(primary_key=True)
    res_type=models.CharField(max_length=1,choices=RESOURCE_TYPE)
    name = models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    contact_Call=models.CharField(max_length=10)
    contact_WA=models.CharField(max_length=10)
    email=models.CharField(max_length=25)
'''