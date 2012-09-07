# -*- coding: utf-8 *-*
import traceback
import logging

from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from curriculumvitae.forms import ContactForm
from curriculumvitae.models import Person

if settings.PDF_AVAILABLE:
    from django_xhtml2pdf.utils import render_to_pdf_response


def __get_person():
    try:
        return Person.objects.all()[0]
    except:
        return None


def curriculum(request):
    return render_to_response('cv_as_html.html', {
        'person': __get_person(),
        'GOOGLE_ANALYTICS_CODE': settings.GOOGLE_ANALYTICS_CODE,
        'PDF_AVAILABLE': settings.PDF_AVAILABLE
    }, context_instance=RequestContext(request))


def print_as_pdf(request):
    context = settings.__dict__.get('_wrapped').__dict__.copy()
    person = __get_person()
    context['person'] = person
    context['print'] = True
    #resp = HttpResponse(content_type='application/pdf')
    #result = generate_pdf('index.html', file_object=resp, context=context)
    #return result
    pdf_name = '%s CV.pdf' % person.full_name
    return render_to_pdf_response('cv_as_pdf.html', context=context,
                                  pdfname=pdf_name)


def contact(request):
    try:
        if request.method == 'POST':
            cf = ContactForm(request.POST)
            if cf.is_valid():
                subject = \
                    "[Email from CV] %s - %s" % (cf.cleaned_data['topic'],
                                                 cf.cleaned_data['email'])
                message = cf.cleaned_data['message']
                from_email = settings.DEFAULT_FROM_EMAIL
                try:
                    send_mail(
                        subject,
                        message,
                        from_email,
                        [__get_person().email]
                    )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return thankyou(request)
        else:
            cf = ContactForm()
        return render_to_response('contact.html', {
            'form': cf
        }, context_instance=RequestContext(request))
    except:
        logger = logging.getLogger('curriculumvitae')
        logger.error(traceback.format_exc())
        print traceback.format_exc()


def thankyou(request):
    return render_to_response('thankyou.html')
