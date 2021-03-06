from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views
app_name = 'apple'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('<int:item_id>/edit/', views.edit, name='edit'),
    path('<int:item_id>/delete/', views.delete, name='delete'),
    path('<int:item_id>/delete/<int:comment_id>/delete', views.comment_delete, name='comment_delete'),
 ]
