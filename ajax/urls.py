from django.urls import path

from . import views

app_name = 'ajax'

urlpatterns = [
    path('', views.ajax, name='ajax'),
    path('get_questions<int:category_pk>', views.get_questions, name='get_questions'),
    path('get_answers', views.get_answers, name='get_answers'),
]
