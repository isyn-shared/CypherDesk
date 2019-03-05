from django.shortcuts import render
from Feedback.models import FeedbackRecord, FeedbackUserIP
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.conf import settings
from g_recaptcha.validate_recaptcha import validate_captcha
import requests, re, distance, simplejson
from datetime import datetime, timezone, timedelta
from CypherDesk.MailAgent import send as sendMail
from CypherDesk.TelegramBot import send as SendTelegram

context = {
    'GOOGLE_RECAPTCHA_SITE_KEY': settings.GOOGLE_RECAPTCHA_SITE_KEY,
}

def now():
    return datetime.now(timezone.utc) + timedelta(minutes=180)

def index (request):
    IP = str(request.META['REMOTE_ADDR'])
    result = {}
    result['ready'] = True
    if FeedbackUserIP.objects.filter(user_ip=IP):
        feedback = FeedbackUserIP.objects.filter(user_ip=IP)[0]
        period = now() - feedback.date
        if period.days == 0 and period.seconds < 60 * 60 and feedback.requests >= 15:
            result['ready'] = False

    return render(request, 'Feedback/wrapper.html', result)

def regexMail(mail):
    p = re.compile(r'([\w\.-]+)@([\w\.-]+)')
    if p.match(mail):
        return True
    return False

def send (request):
    if request.POST:
        ip = str(request.META['REMOTE_ADDR'])
        if FeedbackUserIP.objects.filter(user_ip=ip):
            feedback = FeedbackUserIP.objects.filter(user_ip=ip)[0]

            period = now() - feedback.date
            if period.days >0 or period.seconds > 60 * 10:
                feedback.requests = 0

            if feedback.requests > 15:
                return HttpResponse(2)
            else:
                feedback.requests += 1
                feedback.date = now()
                feedback.save()
        else:
            FeedbackUserIP.objects.create(user_ip=ip, date=now())

        userName = request.POST['user_name']
        userMail = request.POST['user_email'] 
        msgTitle = request.POST['message_title']
        msgText = request.POST['message_text']

        if not userName or not regexMail(userMail) or not msgText or not msgTitle:
            print("ERROR WITH DATA!")
            return HttpResponse(1)

        """sending emails"""
        static_mail_files_path = "/Feedback/templates/Feedback/mail/"
        from_email = settings.EMAIL_HOST_USER
        email_subject = open(settings.BASE_DIR + static_mail_files_path + "title.txt").read()
        email_subject = re.sub("{TITLE}", msgTitle, email_subject)
        email_html_content = open(settings.BASE_DIR + static_mail_files_path + "body.html").read()
        email_html_content = re.sub("{TITLE}", msgTitle, email_html_content)
        email_html_content = re.sub("{USERNAME}", userName, email_html_content)
        email_html_content = re.sub("{CONTACTLINK}", open(settings.BASE_DIR + static_mail_files_path + 'contactlink.txt').read(),
                                    email_html_content)
        email_text_content = ""

        FeedbackRecord.objects.create(title=msgTitle, problem=msgText, answer="", user_name=userName,
                                      user_email=userMail)
        sendMail(from_email, email_subject, email_html_content, email_text_content, userMail)
        telegram_msg = 'Name: ' + userName + '\nTitle: ' + msgTitle + \
                           '\nMessage: ' + msgText + '\nMail: ' + userMail + '\nuser IP: ' + ip
        SendTelegram(settings.FEEDBACK_TELEGRAM_BOT_KEY["feedback"],
                    settings.FEEDBACK_TELEGRAM_CHAT_ID["feedback"], telegram_msg)
        return HttpResponse(0)
    raise Http404()
    
def sort_col(i):
    return i['dis']

def found_titles (request):
    TITLES_LIMIT = 5
    if request.GET:
        records = FeedbackRecord.objects.all()
        current_title = request.GET['message_title']
        result = []

        for record in records:
            if record.answer == "":
                continue
            cnt = ComparsionTitles(current_title, record.title)
            if cnt >= 1:
                result.append({'id': record.id, 'title': record.title, 'dis': cnt})

        result.sort(key=sort_col, reverse=True)

        if len(result) > TITLES_LIMIT:
            result = result[:TITLES_LIMIT]

        result = simplejson.dumps(result)
        return HttpResponse(result)

def ComparsionTitles (s1, s2):
    arr1 = s1.split(' ')
    arr2 = s2.split(' ')

    exc_dict = ['at', 'in', 'is']

    cnt = 0
    for word1 in arr1:
        for word2 in arr2:
            if word1 in exc_dict or word2 in exc_dict or len(word1) < 2  or len(word2) < 2:
                continue
            tmp_dis = 1 - distance.jaccard(word1.lower(), word2.lower())
            if tmp_dis >= 0.8:
                cnt += 1
    return(cnt)

def get_answer(request):
    result = {}
    if request.GET:
        id = request.GET['id']

        if FeedbackRecord.objects.filter(id=id):
            ans = FeedbackRecord.objects.filter(id=id)[0]
            result['ans'] = ans
            return render(request, 'Feedback/full_ans/wrapper.html', result)
    return HttpResponseRedirect(settings.HOSTNAME + '404/')

def faq(request):
    records = FeedbackRecord.objects.all()
    result = {}
    result['faq'] = []

    for record in records:
        if record.answer == "":
            continue
        result['faq'].append({'id': record.id, 'title': record.title})

    print (result['faq'])
    return render(request, 'Feedback/faq/wrapper.html', result)
