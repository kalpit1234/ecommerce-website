from django.shortcuts import render

def eccomerce(request):
    return render(request,'e-commerce.html')
def loginhandle(request):
    return render(request,'login.html')
def signuphandle(request):
    return render(request,'signup.html')
def checkout(request):
    return render(request,'checkout.html')
def cart(request):
    return render(request,'cart.html')
def product_description(request):
    return render(request,'productdescription.html')

def men_html(request):
    return render(request,'men.html')

def contactus(request):
    return render(request,'contact.html')