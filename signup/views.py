from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
#import pandas as pd
# Create your views here.
#username_dict={}

# Python program to write JSON
# to a file


# import json
# f = open(r"D:\Django\ShippingWorld\signup\readme.json")
# with open(r"D:\Django\ShippingWorld\signup\readme.json", "r") as read_file:
#    data = json.load(read_file)

# returns JSON object as 
# a dictionary
# data = json.load(f)
# Data to be written
dictionary = {}

def register(request):
    return render(request,'register.html')
def signup(request):
    if(request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
    
        if(password==confirm_password):
            if(User.objects.filter(password__gt=3).values() and  '@' in password):
                messages.info(request,"Password should be greater than three character")
                return redirect('signup')
            elif(User.objects.filter(username=username).exists()):
                messages.info(request,"Username already taken! Try with Another...")
                return redirect('signup')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,"Email Id already taken! Try with another...")
                print("Email already taken!")
                return redirect("signup")
            else:
                user= User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                #messages.info(request,"New User was created!")
                #print(type(user),'type',user)
                print("user_Created")
                
                # readme.first_name.append(first_name)
                # print(readme.first_name,'signup')
                dictionary[username]=first_name
                # with open(r"D:\Django\ShippingWorld\signup\readme.json", "a") as outfile:
                #     json.dump(dictionary, outfile)
                # print()

                # data.update(dictionary)
                # with open(r"D:\Django\ShippingWorld\signup\readme.json" ,'w') as f:
                #     json.dump(data, f)
                # #json.dump(data)
                # df = pd.read_json(data)
                # df=pd.DataFrame([dictionary],index=['A'])
                # df.to_csv(r"D:\Django\ShippingWorld\signup\readme.csv")
                # print(df,'signup_df')
                return redirect('login')
        else:
            messages.info(request,"Password Not Matching...")
            return redirect('signup')

            


    else:
        return render(request,'signup.html')

# def username_fun():
#     print(username_fun,'fun')
#     return username_dict
