# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.http import HttpResponse
from forms import ContactForm


def contact(request):
    #if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        send_mail(
            cd['subject'],
            cd['message'],
            cd.get('e_mail', 'noreply@example.com'),
            ['siteowner@example.com'],
        )
        return HttpResponse ('/contacts/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'Мне очень нравится ваш сайт!'}
        )
    return render_to_response('template/contact_form.html', {'form': form})

def contact_thanks(request):
    return render_to_response('template/thanks.html')
