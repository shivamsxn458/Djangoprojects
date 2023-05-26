# this file urls.py is manually made, it was not in shop app by default


from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.index, name= "ShopHome"), #here views.index is the path of index function in views.py file
    path('sendpurchaseenquiry/',  views.sendpurchaseenquiry, name= "sendpurchaseenquiry"),
    path('Sellenquiry/',  views.sellenquiry, name= ""),
    path('profile/', views.profile, name='profile'),

    path('categorydisplay/Sherwani',  views.sherwanifunc, name=""),
    path('categorydisplay/Jackets',  views.jacketsfunc, name=""),
    path('categorydisplay/ReceptionOutfits',  views.receptionoutfitsfunc, name=""),
    path('categorydisplay/BridalLehenga',  views.bridallehengafunc, name=""),
    path('categorydisplay/Gown',  views.gownfunc, name=""),
    path('categorydisplay/Saree',  views.sareefunc, name=""),
    path('categorydisplay/Pagdi',  views.pagdifunc, name=""),
    path('categorydisplay/FootwearMen',  views.footwearmenfunc, name=""),
    path('categorydisplay/JewelleryMen',  views.jewellerymenfunc, name=""),
    path('categorydisplay/JewelleryWomen',  views.jewellerywomenfunc, name=""),

    path('sizechart',  views.sizechart, name=""),
    path('formsubmitsuccess', views.formsubmitsuccess, name=""),

]


