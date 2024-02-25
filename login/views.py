from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
#from login import readme
# Create your views here.
# print(views.s())
#print(signup.first_name)
# Python program to read
# json file
#import pandas as pd

#import json

# Opening JSON file
# f = open(r"D:\Django\ShippingWorld\signup\readme.json")
# with open(r"D:\Django\ShippingWorld\signup\readme.json", "r") as read_file:
#    data = json.load(read_file)

# returns JSON object as 
# a dictionary
# data = json.load(f)

# Iterating through the json
# list
#df=pd.read_csv(r'D:\Django\ShippingWorld\signup\readme.csv')

# Closing file


def login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            print(user,'user')
            #print(signup.first_name)
            #print(readme.first_name,'login')
            #s=readme.first_name[0]
            #print(s)
            #print(type(readme.first_name))
            # 
            # f.close()
            #print(data[username],'data')
            #print(df[username],'df_username')
            # {'user':data[username]}
            #print(df[username], df[username][0],'df_login')
            # return render(request,'demo.html',{'user':df[username][0]})
            return render(request,'demo.html',{'name':request.user.first_name})

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

     #return render(request,'login.html')