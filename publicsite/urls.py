from django.conf.urls import url
from .views import (IndexView, EducationalResourcesView, PersonalityAssessmentView,
                    BusinessPlanView, TrainingView, CareersView, AboutUsView, emailView)

app_name = 'publicsite'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^educational-resources', EducationalResourcesView.as_view(), name='educational-resources'),
    url(r'^personality-assessment', PersonalityAssessmentView.as_view(), name='personality-assessment'),
    url(r'^business-plan', BusinessPlanView.as_view(), name='business-plan'),
    url(r'^training', TrainingView.as_view(), name='training'),
    url(r'^careers', CareersView.as_view(), name='careers'),
    url(r'^about-us', AboutUsView.as_view(), name='about-us'),
    url(r'^contact-us', emailView, name='contact-us'),
]