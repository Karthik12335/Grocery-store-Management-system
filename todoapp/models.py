from django.db import models
from todoapp.manager import Customclass

# Create your models here.


class Product(models.Model): #apllicationname_classname = todoapp_Product

    name=models.CharField(max_length=50)
    pdesc=models.CharField(max_length=100)
    price=models.FloatField()
    cat=models.CharField(max_length=20)
    is_deleted=models.CharField(max_length=5)
    uid=models.IntegerField()
    


    obj1=models.Manager() #changing name of the default object of Manager class
    cobj1=Customclass()

    def __str__(self):
        #return self.column_name;
        return self.name