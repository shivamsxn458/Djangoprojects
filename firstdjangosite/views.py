from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
   return render(request, 'index2.html')  #using Templates (template file index2.html)
   # return HttpResponse("<h1> Shivam <h1>")  #without using templates

# def removepunc(request):
#    djtext = request.GET.get('text', 'default')
#    print(djtext)
#    return HttpResponse("remove punc")
   #return render(request, 'index.html')     #using Templates (template file index.html)
   # return HttpResponse("<h1> numberofchar <h1>") #without using templates

def analyze(request):
   djtext = request.GET.get('text', 'default')
   removepunc = request.GET.get('removepunc','off')
   fullcaps = request.GET.get('fullcaps', 'off')

   if djtext != '':

      if removepunc == 'on' and fullcaps == 'on':
         return HttpResponse("Please select only one checkbox at a time!")

      elif removepunc == 'on':
         punctuations = '''!()-[]{};:'"\,<>./…?@#$%^&*_~'''
         analyzed = ''
         for char in djtext:
            if char not in punctuations:
               analyzed = analyzed + char
         return HttpResponse(analyzed)


      elif fullcaps == 'on':
         analyzed = ''
         for char in djtext:
            analyzed = analyzed + char.upper()
         return HttpResponse(analyzed)



      else:
         return HttpResponse("Error! You have not ticked any checkbox")


   else:
      return HttpResponse("Error! You have not entered any text")

def About(request):
   return HttpResponse("<h1> This is About Page </h1>")



def load_text_file(request):
   if request.method == 'POST':
      text_file = request.FILES.get('text_file')
      if text_file:
         contents = text_file.read().decode('utf-8')
         return HttpResponse(contents)
        # return HttpResponse('Success Page')
      return render(request, 'load_text_file.html')

   # print(removepunc)
   # print(djtext)
  # return HttpResponse("Analyze")



