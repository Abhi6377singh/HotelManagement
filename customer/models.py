from django.db import models

# Create your models here.
#class customer(models.Model):
    #address = models.CharField(max_length=255)
    #ssword = models.CharField(max_length=255)

    #def __str__(self):
        #return self.email
    
class customers_h(models.Model):
    address = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    Adharcard_no = models.IntegerField()
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
class booking(models.Model):
    customer_id = models.ForeignKey(customers_h, on_delete=models.CASCADE)
    room_no = models.IntegerField()
    from_date = models.DateField()
    till_date = models.DateField()

    def __str__(self):
        return self.room_no