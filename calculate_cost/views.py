from django.shortcuts import render,redirect
import pandas as pd
from math import sin, cos, sqrt, atan2, radians
from django.contrib import messages


df=pd.read_csv('pincode1.csv')

df=df.drop_duplicates(subset=['Pincode'],keep='first')
i=[i for i in range(18185)]
index=[i for i in range(18185)]
i=pd.Index(i)
df.dropna(inplace=True)
df.set_index(i,inplace=True)
#print(df)
# print(len(df['Pincode']))
dict={}

print(len(df))
# #print(452010 in df['Pincode'])
for i in index:
    dict[str(df.iloc[i][4])]=[df.iloc[i][7],df.iloc[i][8],float(str(df.iloc[i][9])[:6]),float(str(df.iloc[i][10])[:5])]
print('452010' in dict)
# Create your views here.
# print(dict['452010'])
def cost(request,dis,weight):
    rate=86.56
    if(dis in range(30,100)):
        fixed=86
        if(weight in range(100,501)):
        
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate
    elif(dis in range(100,200)):
        fixed=130
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate

    elif(dis in range(200,300)):
        fixed=190.77
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate

    elif(dis in range(300,400)):
        fixed=200
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate
    elif(dis in range(400,550)):
        fixed=290
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate

    elif(dis in range(550,700)):
        fixed=360
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate

    elif(dis in range(700,850)):
        fixed=400
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate
    elif(dis in range(850,1000)):
        fixed=430
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate

    elif(dis in range(100,1300)):
        fixed=460
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate

    elif(dis in range(1300,1500)):
        fixed=490
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate

    elif(dis in range(1500,1800)):
        fixed=500
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate

    elif(dis in range(1800,2000)):
        fixed=530
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate

    elif(dis>2000):
        fixed=550
        if(weight in range(100,501)):
            rate= (fixed+10)
        elif(weight in range(501,1000)):
            rate= (fixed+50)
        elif(weight in range(1000,1500)):
            rate= (fixed+200)
        elif(weight in range(1500,2000)):
            rate= (fixed+290)
        elif(weight in range(2000,2500)):
            rate= (fixed+360)
        elif(weight in range(2500,3200)):
            rate= (fixed+490)
        else:
            rate='Standard Price'
        return rate
        
    return rate

def distance(request,lat1,lat2,lon1,lon2):
# Approximate radius of earth in km
    R = 6373.0
    # lat1 = radians(14.5689)
    # lon1 = radians(77.85624 )
    # lat2 = radians(23.572935)
    # lon2 = radians(87.2332200 )

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return  distance
def calculate_cost(request):
    pickup=request.GET.get('pickup')
    delivery=request.GET.get('delivery')
    weight=request.GET.get('weight')
    amount=request.GET.get('amount')
    # l=request.GET.get('L')
    # print(pickup)
    if(pickup not in dict.keys() and delivery not in dict.keys()):
        print("Enter Valid pincode")
        messages.info(request,'Enter Valid pincode!')
        return render(request,'calculate_cost.html')
    else:
        print("Valid",pickup)
        # messages.info(request,'From')
        messages.info(request,[dict[pickup][0],dict[pickup][1]])
        # messages.info(request,'To')
        messages.info(request,[dict[delivery][0],dict[delivery][1]])
        lat1=radians(dict[pickup][2])
        lon1=radians(dict[pickup][3])
        lat2=radians(dict[delivery][2])
        lon2=radians(dict[delivery][3])
        # lat1=22.388
        # lat2=22.472
        # lon1=75.74
        # lon2=77.23
        print('lat',lat1,lat2,lon1,lon2)
        print('lat',type(lat1),type(lat2),type(lon1),type(lon2))
        dis=int(distance(request,lat1,lat2,lon1,lon2))
        rate=cost(request,dis,int(weight))
        print('dis',dis,weight,type(weight))
        # messages.info(request,dis)
        return render(request,'calculate_cost.html',{'result':rate})
    
        
    