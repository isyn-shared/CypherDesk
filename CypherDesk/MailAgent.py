from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied
from django.conf import settings

def send(from_mail, subject, html_content, text_content, to):
    if type(to) is str:
        to = [to, ]

    msg = EmailMultiAlternatives(subject, text_content, from_mail, to)
    connection = msg.get_connection()
    msg.attach_alternative(html_content, "text/html")

    mail_res = True
    if subject and html_content and from_mail and to:
        try:
            msg.send()
            # message: 'Thanks, your email was sent'
        except BadHeaderError:
            # message: 'Invalid header found.'
            mail_res = False
        except AttributeError:
            # Неправильно указана почта
            mail_res = False
        except:
            mail_res = False
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        # message: Make sure all fields are entered and valid
        mail_res = False

    return mail_res