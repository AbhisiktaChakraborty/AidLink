from django import forms

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

SUPER_TYPE=(
    ("0","Medical"),
    ("1","Food"),
    ("2","Others")
)

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

class VolunteerRegisterForm(forms.Form):
    
    name = forms.CharField(label="Name",max_length=25)
    email = forms.EmailField(label="Email",max_length=20)
    address = forms.CharField(label="Address",max_length=50)
    pincode=forms.CharField(label="Pin Code",max_length=10)
    call=forms.CharField(label="Contact No.",max_length=10)
    whatsApp=forms.CharField(label="WhatsApp No.",max_length=10,required=False)
    res_type_fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=RESOURCE_TYPE)


class ResourceDetailsForm(forms.Form):
    super_type = forms.ChoiceField(label="",choices=SUPER_TYPE)
    sub_type = forms.ChoiceField(label="",choices=SUB_TYPE)

class DonationRegisterForm(forms.Form):
    donation_type=forms.ChoiceField(choices=DONATION_TYPE)
    cause_type=forms.ChoiceField(choices=CAUSE_TYPE)
    amount_wanting=forms.IntegerField(min_value=1000)
    name = forms.CharField(label="Name",max_length=25)
    email = forms.EmailField(label="Email ID",max_length=20)
    address = forms.CharField(label="Address",max_length=50)
    pincode=forms.CharField(label="Pincode",max_length=10)
    call=forms.CharField(label="Contact (Call)",max_length=10)
    whatsApp=forms.CharField(label="Contact (WhatsApp)",max_length=10,required=False)
    medical_documents=forms.ImageField(allow_empty_file=True,required=False)
    

class DonorShowForm(forms.Form):
    donation_type=forms.ChoiceField(choices=DONATION_TYPE)