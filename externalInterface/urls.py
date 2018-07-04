from django.conf.urls import url

from . import views

app_names = 'externalInterface'
urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^getAudio$',views.getVoiceVerificationCode,name='getAudio'),
    url(r'^getWordCloud$',views.getWordCloud,name='getWordCloud')
]