from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('groups/',views.groups,name='groups'),
    path('main_group/',views.main_group,name='main_group'),
    path('ledgers/',views.ledgers,name='ledgers'),
]