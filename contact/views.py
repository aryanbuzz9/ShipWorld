from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages

# def contact(request):
#     subject = 'Welcome to My Site'
#     message = 'Thank you for creating an account!'
#     from_email = 'aryanbuzz9@gmail.com'
#     recipient_list = ['aryanbuzz8@gmail.com']
#     send_mail(subject, message, from_email, recipient_list)
#     return HttpResponse("Thanks")


from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.
# def homepage(request):
# 	return render(request, "main/home.html")

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'],
			'last_name': form.cleaned_data['last_name'],
			'email': form.cleaned_data['email_address'],
			'message':form.cleaned_data['message'],
			}
            
			message = "\n".join(body.values())
			try:     
                
				send_mail(subject, message, 'pushpendrabuzz9@gmail.com', ['pushpendrabuzz9@gmail.com'])
                
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			messages.success(request,"Message sent!")
			return redirect ("contact")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})
#messages.info(request,'Invalid Credentials')