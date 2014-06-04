from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
