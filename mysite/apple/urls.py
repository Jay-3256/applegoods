from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('<int:item_id>/edit/', views.edit, name='edit'),
    path('<int:item_id>/delete/', views.delete, name='delete'),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
