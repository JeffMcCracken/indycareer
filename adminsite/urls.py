from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import DashboardView

app_name = 'adminsite'

urlpatterns = [
    url(r'^$',
        auth_views.LoginView.as_view(template_name='adminsite/login.html'),
        name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^jobs/', include('jobs.urls')),
]