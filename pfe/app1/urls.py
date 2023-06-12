from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [ 
path('update_session_data/',views.update_session_data),
path('dashboard/',views.get_dashboard),
path('extensions/',views.afficher_extensions),
path('SIPTrunks/',views.afficher_SIPTrunks),
path('InboundRules/',views.afficher_InboundRules),
path('OutboundRules/',views.afficher_OutboundRules),
path('DigitalReceptionists/',views.afficher_DigitalReceptionists),
path('RingGroups/',views.afficher_RingGroups),
path('callqueues/',views.afficher_callqueues),


path('', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
path('register/',views.register, name = 'register'),


# path('test/',views.test),


# path('delete/',views.delete_callqueues),

]