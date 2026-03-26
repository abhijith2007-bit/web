from django.db import models
# Create your models here.
class studentdetail(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    phone = models.CharField(max_length=10,null=True)
    is_active = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)