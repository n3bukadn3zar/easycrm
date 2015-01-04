from django.view.generic.base import TemplateView

class HomePage(TemplateView):

    template_name = 'marketing/home.html'
