from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('groups/',views.groups,name='groups'),
    path('m_group/<int:pk>',views.m_group,name='m_group'),
    path('s_group/<int:pk>',views.s_group,name='s_group'),
    path('ledgers/',views.ledgers,name='ledgers'),
    path('grp_alter/<int:pk>',views.grp_alter,name="grp_alter"),

    path('ledger_alter/<int:pk>',views.ledger_alter,name='ledger_alter'),
]