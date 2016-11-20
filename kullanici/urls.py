from django.conf.urls import url,include
from allauth.account.views import *

urlpatterns = [
    url(r'^', include('allauth.urls')),
    url(r'^kullanici/giris/$', LoginView.as_view(), name="custom_login"),
    url(r'^kullanici/kayit/$', SignupView.as_view(), name="custom_singup"),
    url(r"^kullanici/cikis/$", LogoutView.as_view(), name="account_logout"),
    #url(r'^kullanici/parola/degistir/$', PasswordChangeView.as_view(), name='account_change_password'),

]
