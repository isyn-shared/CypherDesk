from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send, name='send_feedback'),
    path('found_titles/', views.found_titles, name='found_titles'),
    path('answer/', views.get_answer, name='answer'),
    path('faq/', views.faq, name='faq'),
]