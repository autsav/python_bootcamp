from django.http.response import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
# Create your views here.
# @login_required
# def home(request):
#     subject = "Test"
#     message = "You have succesfully logged in !!"
#     from_email = "admin@admin.com"
#     recipients = [request.user.email,]
#     send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipients)
#     return render(request, 'userprofile/home.html')

def home(request):
    html_file = get_template('userprofile/mail_template.html')
    html_content = html_file.render()
    subject = "Test"
    # message = "You have succesfully logged in !!"
    from_email = "admin@admin.com"
    to = [request.user.email,]
    msg = EmailMultiAlternatives(subject=subject,from_email=from_email,to=to)
    msg.attach_alternative(html_content,'text/html')
    msg.send()
    return render(request, 'userprofile/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        message = request.POST.get('subject')

        subject = f'Message from {email} . Name : {name}, Country: {country}'
        # message = "You have succesfully logged in !!"
        from_email = "admin@admin.com"
        to = [request.user.email,]
        msg = EmailMultiAlternatives(subject=subject,from_email=from_email,to=to)
        msg.attach_alternative(message,'text/html')
        msg.send()
        return render(request, 'userprofile/contact.html')

    return render(request, 'userprofile/contact.html')

