from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Branch(models.Model):
    BranchName = models.CharField(max_length=250, null=True)
    BranchContactnumber = models.CharField(max_length=12, null=True)
    BranchEmail = models.CharField(max_length=50, null=True)
    BranchAddress = models.CharField(max_length=200, null=True)
    BranchCity = models.CharField(max_length=150, null=True)
    BranchState = models.CharField(max_length=150, null=True)
    BranchPincode = models.CharField(max_length=6, null=True)
    BranchCountry = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.BranchName

class Courier(models.Model):
    RefNumber = models.CharField(max_length=100, null=True)
    SenderBranch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    SenderName = models.CharField(max_length=250, null=True)
    SenderContactnumber = models.CharField(max_length=12, null=True)
    SenderAddress = models.CharField(max_length=250, null=True)
    SenderCity = models.CharField(max_length=150, null=True)
    SenderState = models.CharField(max_length=150, null=True)
    SenderPincode = models.CharField(max_length=6, null=True)
    SenderCountry = models.CharField(max_length=250, null=True)
    RecipientName = models.CharField(max_length=250, null=True)
    RecipientContactnumber = models.CharField(max_length=12, null=True)
    RecipientAddress = models.CharField(max_length=250, null=True)
    RecipientCity = models.CharField(max_length=150, null=True)
    RecipientState = models.CharField(max_length=150, null=True)
    RecipientPincode = models.CharField(max_length=6, null=True)
    RecipientCountry = models.CharField(max_length=150, null=True)
    CourierDes = models.CharField(max_length=250, null=True)
    ParcelWeight = models.CharField(max_length=150, null=True)
    ParcelDimensionlen = models.CharField(max_length=150, null=True)
    ParcelDimensionwidth = models.CharField(max_length=150, null=True)
    ParcelDimensionheight = models.CharField(max_length=150, null=True)
    ParcelPrice = models.CharField(max_length=150, null=True)
    Status = models.CharField(max_length=100, null=True)
    CourierDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.SenderName

class CourierTracking(models.Model):
    CourierId = models.ForeignKey(Courier, on_delete=models.CASCADE, null=True)
    remark = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=150, null=True)
    StatusDate = models.DateField(null=True)

    def __str__(self):
        return self.status

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    StaffMobilenumber = models.CharField(max_length=12, null=True)
    status = models.CharField(max_length=150, null=True)
    StaffRegdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name


