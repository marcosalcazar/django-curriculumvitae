# -*- coding: utf-8 *-*
import traceback

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from curriculumvitae.forms import ContactForm
from curriculumvitae.models import Person


def __get_person():
    try:
        return Person.objects.all()[0]
    except:
        return None


def curriculum(request):
    return render_to_response('index.html', {
        'person': __get_person()
    }, context_instance=RequestContext(request))


def contact(request):
    try:
        if request.method == 'POST':
            cf = ContactForm(request.POST)
            if cf.is_valid():
                subject = cf.cleaned_data['topic']
                message = cf.cleaned_data['message']
                from_email = cf.cleaned_data['email']
                try:
                    send_mail(
                        subject,
                        message,
                        from_email,
                        [__get_person().email]
                    )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return thankyou()
        else:
            cf = ContactForm()
        return render_to_response('contact.html', {
            'form': cf
        }, context_instance=RequestContext(request))
    except:
        print traceback.format_exc()


def thankyou(request):
    return render_to_response('thankyou.html')
