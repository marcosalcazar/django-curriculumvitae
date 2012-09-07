# -*- coding: utf-8 *-*
import cStringIO as StringIO
import ho.pisa as pisa
import traceback

from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader import render_to_string

from curriculumvitae.forms import ContactForm
from curriculumvitae.models import Person


def __get_person():
    try:
        return Person.objects.all()[0]
    except:
        return None


def curriculum(request):
    return render_to_response('index.html', {
        'person': __get_person(),
        'GOOGLE_ANALYTICS_CODE': settings.GOOGLE_ANALYTICS_CODE
    }, context_instance=RequestContext(request))


def __generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF')


def print_as_pdf(request):
    html = render_to_string('index.html', {
        'pagesize': 'A4',
        'print': True,
        'person': __get_person()
    }, context_instance=RequestContext(request))
    return __generar_pdf(html)


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
