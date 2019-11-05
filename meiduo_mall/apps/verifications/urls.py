from django.conf.urls import url
from . import views
urlpatterns = [
    # 图形验证码
    url(r'^image_codes/(?P<uuid>[\w-]+)/$', views.ImageCodeView.as_view()),
    url(r'^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.SmsCodeView.as_view()),
    url(r'^smscodes/(?P<mobile>1[3-9]\d{9})/$', views.CodeView.as_view()),
    url(r'^sms_codes/$', views.FindPasswordSms.as_view()),


]