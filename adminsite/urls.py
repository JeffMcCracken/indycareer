from django.conf.urls import url, include
from .views import IndexView

app_name = 'adminsite'

urlpatterns = [
    url(r'', IndexView.as_view(), name='index'),
    url(r'^jobs/', include('jobs.urls')),
]