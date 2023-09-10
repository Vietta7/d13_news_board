import datetime

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django_apscheduler.models import DjangoJobExecution

from .models import Post, Author
from project_board.settings import SITE_URL, DEFAULT_FROM_EMAIL


def news_sending():
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=1)
    articles = Post.objects.filter(created__gte=yesterday)
    subscribers = Author.objects.filter(is_subscriber=True)
    e_boxes = []
    for person in subscribers:
        e_boxes.append(person.name.email)

    html_content = render_to_string('daily_posts.html', {
        'link': f'{SITE_URL}/',
        'posts': articles,
        'date': yesterday,
    })
    msg = EmailMultiAlternatives(subject='Статьи за неделю',
                                 body='',
                                 from_email=DEFAULT_FROM_EMAIL,
                                 to=e_boxes, )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)
