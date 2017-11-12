from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
          first_name = form.cleaned_data['first_name']
          last_name = form.cleaned_data['last_name']
          subject = form.cleaned_data['subject']
          from_email = form.cleaned_data['from_email']
          message = form.cleaned_data['message']
          try:
            full_name = first_name + " " + last_name
            final_form = "Full Name: " + full_name + "\n\n" + "From: " + from_email + "\n\n" + message
            send_mail(subject, final_form, 'eribe403@gmail.com', ['eribe403@gmail.com'], fail_silently=False)

          except BadHeaderError:
            return HttpResponse('Invalid header found.')
          return redirect('success')
    return render(request, "contact/contact.html", {'form': form})

def success(request):
    return HttpResponse('Success! Thank you for your message.')
