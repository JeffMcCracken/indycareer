from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, CreateView, UpdateView, 
                                    DeleteView, ListView, DetailView)
from django.core.mail import send_mail, BadHeaderError
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import JobPosting

class IndexView(TemplateView):
    template_name = 'publicsite/index.html'

class EducationalResourcesView(TemplateView):
    template_name = 'publicsite/educational-resources.html'

class PersonalityAssessmentView(TemplateView):
    template_name = 'publicsite/personality-assessment.html'

class BusinessPlanView(TemplateView):
    template_name = 'publicsite/business-plan.html'

class TrainingView(TemplateView):
    template_name = 'publicsite/training.html'

class CareersView(TemplateView):
    template_name = 'publicsite/careers.html'

class AboutUsView(TemplateView):
    template_name = 'publicsite/about-us.html'

def emailView(request):
    if request.method == 'GET':
        form = ContactForm
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/')
    return render(request, 'publicsite/contact-us.html', {'form': form})
