from django.shortcuts import render
from django.shortcuts import redirect
# from google_auth_oauthlib.flow import Flow
# from google.oauth2.credentials import Credentials
# from django.shortcuts import redirect
from .models import Product
from .models import SellEnquiry
from .models import PurchaseEnquiry
from django.http import HttpResponse,request
from .forms import CustomerForm
from .forms import SellEnquiryForm
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse


# -----------------------------------------------------------------------------------------------

@login_required
def profile(request):
    social = SocialAccount.objects.get(provider='google', user=request.user)
    name = social.extra_data['name']
    picture = social.extra_data['picture']
    email = social.extra_data['email']
    location = social.extra_data.get('location', None)
    username = request.user.username
    # enquiries = SellEnquiry.objects.all()


    status = SellEnquiry.objects.filter(username=request.user.username).values('Status')
    enquiries = SellEnquiry.objects.filter(username=request.user.username).select_related('product')

    status_list = [s.Status for s in enquiries]
    kards = []
    product_list = [s.product for s in enquiries]
    cards = []

    for product, Status in zip(product_list, status_list):  #(here we are combining both for loops for product_list and status_list )
        card = f"""
                   <p>{product}</p>                     
               <button type="button" class="btn btn-dark" style="background:maroon;">{Status}</button><br><br> 
               """
        cards.append(card)





    purchasestatus = PurchaseEnquiry.objects.filter(username=request.user.username).values('Status')
    purchaseenq = PurchaseEnquiry.objects.filter(username=request.user.username)

    purchaseproduct_list = [s.Product_Selected for s in purchaseenq]
    pards = []
    purchasestatus_list = [s.Status for s in purchaseenq]
    wards = []


    for Product_Selected, Status in zip(purchaseproduct_list,purchasestatus_list):  # (here we are combining both for loops for product_list and status_list )

        card_2 = f"""
                     <p>{Product_Selected}</p>                     
                 <button type="button" class="btn btn-dark" style="background:maroon;">{Status}</button><br><br> 
                 """
        pards.append(card_2)



    # for product in product_list:
    #     card = f"""
    #     <div class="card">
    #       <div class="card-body">
    #         <p class="card-title">{product}</p>
    #       </div>
    #     </div>
    #     """
    #     cards.append(card)

    # status_list = [s.Status for s in enquiries]
    # kards = []
    # for Status in status_list:
    #     kard = f"""
    #         <div>
    #             <p class="card-title">{Status}</p>
    #
    #         </div>
    #         """
    #     kards.append(kard)




    context = {
        'name': name,
        'picture': picture,
        'email': email,
        'location': location,
        'username': username,
        'cards': cards,
        'kards': kards,
        'wards': wards,
        'pards': pards,

    }

    return render(request, 'shop/profile.html', context)

# -----------------------------------------------------------------------------------------------



# @login_required    (@login_required is a login decorator which can be put before a function, it requires google auth etc to view that particular thing)

def index(request):
    products = Product.objects.all()[:8]
    context = {'products': products}
    return render(request, 'shop/index.html', context)

#
#
# @login_required()
# def sendpurchaseenquiry(request):
#
#     form = CustomerForm()
#     if request.method == 'POST':
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     return render(request, 'shop/purchaseenquiryform.html', context)





def sendpurchaseenquiry(request):
    username = request.user.username
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            purchase_enquiry = form.save(commit=False)
            purchase_enquiry.username = username
            purchase_enquiry.save()
            return redirect('http://weddpparels.com/shop/formsubmitsuccess')
            # return HttpResponse("You have submitted the Purchase enquiry form successfully.")
    else:
        form = CustomerForm(initial={'username': username})
    context = {'form': form,}
    return render(request, 'shop/purchaseenquiryform.html', context)




def formsubmitsuccess(request):
    return render(request, 'shop/formsubmitsuccess.html')



def sellenquiry(request):
    username = request.user.username
    if request.method == 'POST':
        form = SellEnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            sell_enquiry = form.save(commit=False)
            sell_enquiry.username = username
            sell_enquiry.save()
            return redirect('http://weddpparels.com/shop/formsubmitsuccess')
            # return HttpResponse("You have submitted the Sell enquiry form successfully.")
            # button_html = '<a href="http://localhost:8000/shop">You have successfully submitted the sell enquiry. <br><br><br>  Go to Home Page</a>'
            # return HttpResponse(button_html)

    else:
        form = SellEnquiryForm(initial={'username': username})
    context = {'form': form,}
    return render(request, 'shop/Sellform.html', context)




##########################################################################
# Navbar category functions Start


def sherwanifunc(request):
    products = Product.objects.filter(subcategory='Sherwani')
    productsfilter = Product.objects.filter(subcategory='Sherwani')[:1] #To fetch first result and show its subcategory in category pages>> navbarcat html files from base,html (title and para)
    context = {'products':products, 'productsfilter':productsfilter}
    return render(request, 'shop/navbarcategorydisplay.html',context)


def jacketsfunc(request):
    products = Product.objects.filter(subcategory='Jackets')
    productsfilter = Product.objects.filter(subcategory='Jackets')[:1] #To fetch first result and show its subcategory in category pages>> navbarcat html files from base,html (title and para)
    context = {'products':products, 'productsfilter':productsfilter}
    return render(request, 'shop/navbarcatjackets.html',context)

def receptionoutfitsfunc(request):
    products = Product.objects.filter(subcategory='Reception Outfits')
    productsfilter = Product.objects.filter(subcategory='Reception Outfits')[:1]
    context = {'products':products, 'productsfilter':productsfilter}
    return render(request, 'shop/navbarcatreceptionoutfits.html',context)


def bridallehengafunc(request):
    products = Product.objects.filter(subcategory='Bridal Lehenga')
    productsfilter = Product.objects.filter(subcategory='Bridal Lehenga')[:1]
    context = {'products': products, 'productsfilter': productsfilter}
    return render(request, 'shop/navbarcatbridallehenga.html',context)


def gownfunc(request):
    products = Product.objects.filter(subcategory='Gown')
    productsfilter = Product.objects.filter(subcategory='Gown')[:1]
    context = {'products': products, 'productsfilter': productsfilter}
    return render(request, 'shop/navbarcatgown.html',context)


def sareefunc(request):
    products = Product.objects.filter(subcategory='Saree')
    productsfilter = Product.objects.filter(subcategory='Saree')[:1]
    context = {'products': products, 'productsfilter': productsfilter}
    return render(request, 'shop/navbarcatsaree.html',context)


def pagdifunc(request):
    products = Product.objects.filter(subcategory='Pagdi')
    productsfilter = Product.objects.filter(subcategory='Pagdi')[:1]
    context = {'products': products, 'productsfilter': productsfilter}
    return render(request, 'shop/navbarcatpagdi.html',context)




def footwearmenfunc(request):
    products = Product.objects.filter(subcategory='Footwear Men')
    productsfilter = Product.objects.filter(subcategory='Footwear Men')[:1]  #To fetch first result and show its subcategory in category pages>> navbarcat html files from base,html (title and para)
    context = {'products':products, 'productsfilter':productsfilter}
    return render(request, 'shop/navbarcatfootwearmen.html',context)

def jewellerymenfunc(request):
    products = Product.objects.filter(subcategory='Jewellery Men')
    productsfilter = Product.objects.filter(subcategory='Jewellery Men')[:1]  #To fetch first result and show its subcategory in category pages>> navbarcat html files from base,html (title and para)
    context = {'products':products, 'productsfilter':productsfilter}
    return render(request, 'shop/navbarcatjewellerymen.html',context)


def jewellerywomenfunc(request):
    products = Product.objects.filter(subcategory='Jewellery Women')
    productsfilter = Product.objects.filter(subcategory='Jewellery Women')[:1]  #To fetch first result and show its subcategory in category pages>> navbarcat html files from base,html (title and para)
    context = {'products':products, 'productsfilter':productsfilter}
    return render(request, 'shop/navbarcatjewellerywomen.html',context)


# Navbar category functions End
##########################################################################


def sizechart(request):
    return render(request, 'shop/sizechart.html')


def privacypolicy(request):
    return render(request, 'shop/privacypolicy.html')


##########################################  JSON API'S BELOW  ##########################################

def product_api(request):
    products = Product.objects.all()[:8]
    product_list = [
        {
            'frontimage':product.image.url if product.image else None,
            'sideimage':product.sideimage.url if product.sideimage else None,
            'backimage':product.backimage.url if product.backimage else None,
            'name':product.product_name,
            'Size':product.size,
            'PurchaseDate':product.purchase_date,
            'ComparewithNew':product.url
        }
        for product in products
    ]
    # return JsonResponse({'products': product_list})
    return JsonResponse(product_list, safe=False)
