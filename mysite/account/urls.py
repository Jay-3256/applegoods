from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate, name='activate'),
    path('account_activation_sent/',views.account_activation_sent, name='account_activation_sent'),
 ]
