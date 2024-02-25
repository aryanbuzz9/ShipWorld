from django.shortcuts import render

def Home(request):
    return render(request,'basic.html')

def About(request):
    return render(request,'about_us.html')

def Dont(request):
    return render(request,'do_not_click.html')

def Contact(request):
    return render(request,'contact.html')

# def Signup(request):
#     return render(request,'signup.html')

# def Login(request):
#     return render(request,'login.html')

def Activate_Pincode(request):
    return render(request,'activate_pincode.html')

def Pricing_Know_More(request):
    return render(request,'pricing_know_more.html')

def Track_Order(request):
    return render(request,'track_order.html')

def Demo(request):
    return render(request,'demo.html')



