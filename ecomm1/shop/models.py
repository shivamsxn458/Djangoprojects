from django.db import models
# from django import forms
# from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractUser




class AllProductNames(models.Model):
    # product_id = models.AutoField
    product_name = models.CharField(max_length= 30)

    def __str__(self):    #function/method to list model objects as product name in admin panel
        return self.product_name



class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length= 30)
    size = models.CharField(max_length=100, blank=True, default="onesize")
    purchase_date = models.DateField()
    category = models.CharField(max_length=25, default="")
    subcategory = models.CharField(max_length=25, default="")
    price = models.IntegerField(default= 0)
    image = models.ImageField(upload_to="shop/images", blank=True, default="")
    sideimage = models.ImageField(upload_to="shop/images", blank=True, default="/shop/images/imagecomingsoon.png")
    backimage = models.ImageField(upload_to="shop/images", blank=True, default="/shop/images/imagecomingsoon.png")
    url = models.URLField(max_length=200, blank=True, default= "")

    def __str__(self):    #function/method to list model objects as product name in admin panel
        return self.product_name


class PurchaseEnquiry(models.Model):
    # Customer_id = models.AutoField
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Contact_Number = models.CharField(max_length=10)
    Email = models.EmailField()
    Status = models.CharField(max_length=20, default="Status: under review")
    Product_Selected = models.CharField(max_length=200, default="")
    username = models.CharField(max_length=50, default="")


    class Meta:
        unique_together = (('Contact_Number', 'Product_Selected'))

    def __str__(self):
        return self.username





class SellEnquiry(models.Model):
    username = models.CharField(max_length=50, default="")
    # Customer_id = models.AutoField
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Contact_Number = models.CharField(max_length=10)
    Email = models.EmailField()
    # Product_Selected = models.CharField(max_length=100, default="")
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, default="")
    product = models.ForeignKey(AllProductNames, on_delete = models.DO_NOTHING, default="")
    dropdown_field = models.CharField(max_length=50, default="", blank=True)
    Brand_name = models.CharField(max_length=100)
    purchase_date = models.DateField()
    size = models.CharField(max_length=50, blank=True)
    your_ask_price = models.IntegerField(default=0)
    product_Front_Image = models.ImageField(upload_to="shop/sellenquiryimages",default="")
    product_Side_Image = models.ImageField(upload_to="shop/sellenquiryimages", default="")
    product_Back_Image = models.ImageField(upload_to="shop/sellenquiryimages", default="")
    product_Bill_or_Invoice = models.FileField(upload_to="shop/sellenquiryimages",blank=True ,default="")
    Status = models.CharField(max_length=20, default="Status: under review")



    class Meta:
        unique_together = (('Contact_Number', 'product'))


    def __str__(self):
        # return self.Contact_Number
        return self.username


    def get_dropdown_choices(self):
        choices = []
        products = Product.objects.all()
        for product in products:
            # choices.append((product.name, product.name))
            choices.append((product.name))
        return choices







# The __str__() method in the Product class is defined to return a string representation of a product instance
# ,which is used to display the product in the Django admin interface or any other place where the object needs
# to be displayed as a string. In this case, the __str__() method returns the product_name attribute of the Product instance,
# which is a CharField that stores the name of the product. This means that when you display a Product instance,
# it will be represented as its product name.

# If you don't use str method :   if you have a Product instance without a __str__() method defined, ' \
# 'and you call str() on that instance, you would get something like <Product: Product object (1)>, ' \
# 'where 1 is the ID of the product in the database.
# By defining a __str__() method, you can provide a custom string representation for your Django model that is more meaningful
# and easier to work with.'