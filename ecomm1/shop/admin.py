# Register your models here. (In Django admin panel you have to register the models to see your db tables there)

from django.contrib import admin
from .models import Product
from .models import PurchaseEnquiry
from .models import SellEnquiry
from .models import AllProductNames




admin.site.register(Product)
admin.site.register(PurchaseEnquiry)
admin.site.register(SellEnquiry)
admin.site.register(AllProductNames)



